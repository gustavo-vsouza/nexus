from fastapi import FastAPI
from routes import *
from database.connection import Base, engine

app = FastAPI(title="Zentavos API")

# Criar tabelas automaticamente
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Bem-vindo ao backend do Zentavos 🚀"}
