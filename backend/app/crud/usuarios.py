from sqlalchemy.orm import Session
from app.models.transacoes import Transacao

# CREATE - cria uma nova transação no banco
def criar_transacao(db: Session, conta_id: int, valor: int, tipo: str,
                    descricao: str = None, categoria_id: int = None):
    transacao = Transacao(
        conta_id=conta_id,
        categoria_id=categoria_id,
        valor=valor,
        descricao=descricao,
        tipo=tipo
    )  # cria o objeto da transação
    db.add(transacao)  # adiciona à sessão
    db.commit()  # confirma no banco
    db.refresh(transacao)  # atualiza com dados do banco (ex: id gerado)
    return transacao

# READ - lista todas as transações
def listar_transacoes(db: Session):
    return db.query(Transacao).all()

# READ - busca uma transação por id
def listar_transacao_por_id(db: Session, transacao_id: int):
    return db.query(Transacao).filter(Transacao.id == transacao_id).first()

# UPDATE - atualiza os dados de uma transação
def atualizar_transacao(db: Session, transacao_id: int, conta_id: int = None,
                        valor: int = None, tipo: str = None,
                        descricao: str = None, categoria_id: int = None):
    transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    if not transacao:
        return None
    # só atualiza os campos enviados
    if conta_id is not None:
        transacao.conta_id = conta_id
    if valor is not None:
        transacao.valor = valor
    if tipo is not None:
        transacao.tipo = tipo
    if descricao is not None:
        transacao.descricao = descricao
    if categoria_id is not None:
        transacao.categoria_id = categoria_id
    db.commit()
    db.refresh(transacao)  # pega os dados atualizados
    return transacao

# DELETE - remove de vez a transação do banco
def deletar_transacao(db: Session, transacao_id: int):
    transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    if not transacao:
        return None
    db.delete(transacao)  # deleta de verdade (não soft delete)
    db.commit()
    return transacao
