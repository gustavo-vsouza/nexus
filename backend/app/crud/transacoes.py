# app/crud/transacoes.py
from typing import Optional, List
from decimal import Decimal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.transacoes import TransacaoBase
from app.models.contas import Conta
from app.models.categorias import Categoria
from app.models.usuarios import Usuario

# CREATE - cria a transação e ajusta o saldo da conta (operação atomica)
def criar_transacao(
    db: Session,
    usuario_id: int,
    conta_id: int,
    categoria_id: Optional[int],
    tipo: str,
    valor: Decimal,
    data,
    descricao: Optional[str] = None,
    total_parcelas: int = 1,
    data_primeira_parcela = None,
) -> Optional[Transacao]:
    # validações simples
    if tipo not in ("receita", "despesa"):
        raise ValueError("tipo deve ser 'receita' ou 'despesa'")
    if valor <= 0:
        raise ValueError("valor deve ser > 0")

    # checar existência das entidades (melhora mensagens de erro)
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise ValueError(f"usuario_id {usuario_id} não encontrado")

    conta = db.query(Conta).filter(Conta.id == conta_id).first()
    if not conta:
        raise ValueError(f"conta_id {conta_id} não encontrada")

    # verifica se a conta pertence ao usuário (boas práticas)
    if conta.usuario_id != usuario_id:
        raise ValueError("a conta informada não pertence ao usuário")

    if categoria_id is not None:
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
        if not categoria:
            raise ValueError(f"categoria_id {categoria_id} não encontrada")

    transacao = Transacao(
        usuario_id=usuario_id,
        conta_id=conta_id,
        categoria_id=categoria_id,
        tipo=tipo,
        valor=valor,
        data=data,
        descricao=descricao,
        total_parcelas=total_parcelas,
        data_primeira_parcela=data_primeira_parcela,
    )

    try:
        # BEGIN TRANSACTION: garante que a criação + ajuste de saldo sejam atômicos
        with db.begin():
            db.add(transacao)
            # ajustar saldo da conta conforme tipo
            # Certifique-se que conta.saldo é Decimal/Numeric no model
            current_saldo = Decimal(conta.saldo or 0)
            if tipo == "receita":
                conta.saldo = current_saldo + Decimal(valor)
            else:
                conta.saldo = current_saldo - Decimal(valor)
            # o commit será realizado pelo context manager
        # depois do commit, refresh da transação
        db.refresh(transacao)
        return transacao
    except IntegrityError:
        db.rollback()
        return None


# READ - listagem com filtros e paginação
def listar_transacoes(
    db: Session,
    usuario_id: Optional[int] = None,
    conta_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    date_from = None,
    date_to = None,
    offset: int = 0,
    limit: int = 100,
) -> List[Transacao]:
    query = db.query(Transacao)
    if usuario_id is not None:
        query = query.filter(Transacao.usuario_id == usuario_id)
    if conta_id is not None:
        query = query.filter(Transacao.conta_id == conta_id)
    if categoria_id is not None:
        query = query.filter(Transacao.categoria_id == categoria_id)
    if date_from is not None:
        query = query.filter(Transacao.data >= date_from)
    if date_to is not None:
        query = query.filter(Transacao.data <= date_to)

    return query.order_by(Transacao.data.desc()).offset(offset).limit(limit).all()


def obter_transacao_por_id(db: Session, transacao_id: int) -> Optional[Transacao]:
    return db.query(Transacao).filter(Transacao.id == transacao_id).first()


# UPDATE - atualiza e ajusta saldo das contas (reverte efeito antigo e aplica o novo)
def atualizar_transacao(
    db: Session,
    transacao_id: int,
    tipo: Optional[str] = None,
    valor: Optional[Decimal] = None,
    conta_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    data = None,
    descricao: Optional[str] = None,
    total_parcelas: Optional[int] = None,
    data_primeira_parcela = None,
) -> Optional[Transacao]:
    transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    if not transacao:
        return None

    # Guardar estado antigo para poder reverter saldo
    old_valor = Decimal(transacao.valor)
    old_tipo = transacao.tipo
    old_conta_id = transacao.conta_id

    # Caso vá trocar conta, buscar ambas contas
    conta_old = db.query(Conta).filter(Conta.id == old_conta_id).first()
    conta_new = conta_old
    if conta_id is not None and conta_id != old_conta_id:
        conta_new = db.query(Conta).filter(Conta.id == conta_id).first()
        if not conta_new:
            raise ValueError("conta_id novo não encontrada")

    # Valida novo tipo/valor
    if tipo is not None and tipo not in ("receita", "despesa"):
        raise ValueError("tipo deve ser 'receita' ou 'despesa'")
    if valor is not None and Decimal(valor) <= 0:
        raise ValueError("valor deve ser > 0")

    try:
        with db.begin():
            # Reverter efeito antigo sobre conta_old
            if old_tipo == "receita":
                conta_old.saldo = Decimal(conta_old.saldo or 0) - old_valor
            else:
                conta_old.saldo = Decimal(conta_old.saldo or 0) + old_valor

            # Aplicar novo efeito na conta_new (pode ser a mesma conta)
            new_tipo = tipo if tipo is not None else old_tipo
            new_valor = Decimal(valor) if valor is not None else old_valor

            if new_tipo == "receita":
                conta_new.saldo = Decimal(conta_new.saldo or 0) + new_valor
            else:
                conta_new.saldo = Decimal(conta_new.saldo or 0) - new_valor

            # Atualizar campos da transação
            if tipo is not None:
                transacao.tipo = tipo
            if valor is not None:
                transacao.valor = valor
            if conta_id is not None:
                transacao.conta_id = conta_id
            if categoria_id is not None:
                transacao.categoria_id = categoria_id
            if data is not None:
                transacao.data = data
            if descricao is not None:
                transacao.descricao = descricao
            if total_parcelas is not None:
                transacao.total_parcelas = total_parcelas
            if data_primeira_parcela is not None:
                transacao.data_primeira_parcela = data_primeira_parcela

        db.refresh(transacao)
        return transacao
    except IntegrityError:
        db.rollback()
        return None


# DELETE - deleta transação e reverte efeito no saldo da conta
def deletar_transacao(db: Session, transacao_id: int) -> bool:
    transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    if not transacao:
        return False

    try:
        with db.begin():
            conta = db.query(Conta).filter(Conta.id == transacao.conta_id).first()
            if conta:
                if transacao.tipo == "receita":
                    conta.saldo = Decimal(conta.saldo or 0) - Decimal(transacao.valor)
                else:
                    conta.saldo = Decimal(conta.saldo or 0) + Decimal(transacao.valor)

            db.delete(transacao)
        return True
    except IntegrityError:
        db.rollback()
        return False
