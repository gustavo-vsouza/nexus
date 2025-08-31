from sqlalchemy import Column, Integer, Numeric, String, TIMESTAMP, ForeignKey, DATE, Text, CheckConstraint
from sqlalchemy.sql import func
from app.database.connection import Base

class Transacao(Base):
    __tablename__ = "transacoes"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    conta_id = Column(Integer, ForeignKey("contas.id", ondelete="CASCADE"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    valor = Column(Numeric(12,2), nullable=False)
    data = Column(DATE, nullable=False)
    descricao = Column(Text)
    tipo = Column(String(10), nullable=False)
    total_parcelas = Column(Integer, default=1)
    data_primeira_parcela = Column(DATE)
    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())
    
    __table_args__ = (
        CheckConstraint("tipo IN ('receita', 'despesa')", name="check_tipo_transacao"),
)