from fastapi import FastAPI
from routes import usuarios, transacoes, categorias
from database.connection import Base, engine

app = FastAPI(title="Zentavos API")

# # Incluindo as rotas
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(transacoes.router, prefix="/transacoes", tags=["Transações"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])


# Criar tabelas automaticamente
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Bem-vindo ao backend do Zentavos 🚀"}
