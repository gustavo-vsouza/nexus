from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)  # entrada ou saída
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario")
