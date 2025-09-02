from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey, CheckConstraint
from app.database.connection import Base

# Classe que representa a tabela "transacoes" no banco
class Transacao(Base):
    __tablename__ = "transacoes"  # nome da tabela no banco

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)  # chave primária
    conta_id = Column(Integer, ForeignKey("contas.id", ondelete="CASCADE"), nullable=False)  # FK para contas
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="SET NULL"), nullable=True)  # FK para categorias (pode ser nula)
    valor = Column(Integer, nullable=False)  # valor da transação
    descricao = Column(String(255), nullable=True)  # descrição opcional
    tipo = Column(String(10), nullable=False)  # tipo da transação (ex: entrada ou saída)
    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())  # data de criação

    # Restrição: tipo só pode ser "entrada" ou "saida"
    __table_args__ = (
        CheckConstraint("tipo IN ('entrada','saida')", name="check_tipo_transacao"),
    )
