from sqlalchemy.orm import Session
from app.models.contas import Conta

# CREATE - cria nova conta
def criar_conta(db: Session, usuario_id: int, nome: str, saldo: int = 0):
    conta = Conta(usuario_id=usuario_id, nome=nome, saldo=saldo)  # cria o objeto
    db.add(conta)  # adiciona na sessão
    db.commit()  # confirma no banco
    db.refresh(conta)  # atualiza com id gerado
    return conta

# READ - lista todas as contas de um usuário
def listar_contas(db: Session, usuario_id: int):
    return db.query(Conta).filter(Conta.usuario_id == usuario_id).all()

# READ - busca uma conta pelo id
def listar_conta_por_id(db: Session, conta_id: int):
    return db.query(Conta).filter(Conta.id == conta_id).first()

# UPDATE - altera nome ou saldo
def atualizar_conta(db: Session, conta_id: int, nome: str = None, saldo: int = None):
    conta = db.query(Conta).filter(Conta.id == conta_id).first()
    if not conta:
        return None
    if nome is not None:
        conta.nome = nome
    if saldo is not None:
        conta.saldo = saldo
    db.commit()
    db.refresh(conta)
    return conta

# DELETE - remove do banco
def deletar_conta(db: Session, conta_id: int):
    conta = db.query(Conta).filter(Conta.id == conta_id).first()
    if not conta:
        return None
    db.delete(conta)
    db.commit()
    return conta
