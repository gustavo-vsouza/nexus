from app.database.connection import SessionLocal
from app.models.usuarios import Usuario

# Criar sessão
db = SessionLocal()

# Criar um novo usuário
novo_usuario = Usuario(
    nome="Gustavo Souza",
    email="gustavovsouza90@gmail.com",
    senha_hash="Falsidade03"
)

# Adicionar ao banco
db.add(novo_usuario)
db.commit()
db.refresh(novo_usuario)

print(f"Usuário criado com ID: {novo_usuario.id}")

# Fechar sessão
db.close()
