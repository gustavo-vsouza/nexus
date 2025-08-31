from sqlalchemy import Column, Integer, String, ForeignKey,CheckConstraint
from app.database.connection import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(10), nullable=False)
    
    __table_args__ = (
    CheckConstraint("tipo IN ('receita','despesa')", name="check_tipo_categoria"),
)
