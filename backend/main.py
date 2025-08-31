from fastapi import FastAPI
from app.database.connection import Base, engine

from app.models.usuarios import Usuario
from app.models.contas import Conta
from app.models.categorias import Categoria
from app.models.transacoes import Transacao

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API Zentavos rodando 🚀"}
