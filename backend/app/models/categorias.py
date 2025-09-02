from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Categoria(Base):
    __tablename__ = "categorias"  # nome da tabela no banco

    # Colunas principais
    id = Column(Integer, primary_key=True, index=True)  # chave primária
    nome = Column(String(100), unique=True, nullable=False)  # nome da categoria (único)
    descricao = Column(String(255), nullable=True)  # descrição opcional
    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())  # data de criação

    # Relacionamento futuro (transações podem ter categoria)
    transacoes = relationship("Transacao", back_populates="categoria", cascade="all, delete")
