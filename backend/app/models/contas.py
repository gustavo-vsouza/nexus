from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Conta(Base):
    __tablename__ = "contas"  # nome da tabela

    # Colunas
    id = Column(Integer, primary_key=True, index=True)  # chave primária
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)  
    # chave estrangeira -> cada conta pertence a um usuário

    nome = Column(String(100), nullable=False)  # nome da conta
    saldo = Column(Integer, default=0)  # saldo inicial
    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())  # data de criação

    # Relacionamento (opcional): permite acessar o usuário dono da conta
    usuario = relationship("Usuario", backref="contas")
