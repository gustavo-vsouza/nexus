from sqlalchemy import Column, Integer, Numeric, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.database.connection import Base

class Conta(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    nome = Column(String(100), nullable=False)
    saldo = Column(Numeric(12,2), default=0)
    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())