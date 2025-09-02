from sqlalchemy import Column, Integer, String, TIMESTAMP, func, CheckConstraint
from app.database.connection import Base

# Classe que representa a tabela "usuarios" no banco
class Usuario(Base):
    __tablename__ = "usuarios"  # nome da tabela no banco

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)  # chave primária, auto incremento
    nome = Column(String(100), nullable=False)  # nome do usuário (obrigatório)
    email = Column(String(150), unique=True, nullable=False, index=True)  # email único
    senha_hash = Column(String(255), nullable=False)  # senha já criptografada
    status = Column(String(20), nullable=False, default="ativo")  # status do usuário
    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())  # data de criação

    # Restrição: status só pode ser "ativo", "inativo" ou "banido"
    __table_args__ = (
        CheckConstraint("status IN ('ativo','inativo','banido')", name="check_status_usuario"),
    )
