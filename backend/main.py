from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes import usuarios, contas, categorias, transacoes

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cria a aplicação FastAPI
app = FastAPI(title="Zentavos API")


app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(contas.router, prefix="/contas", tags=["Contas"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
app.include_router(transacoes.router, prefix="/transacoes", tags=["Transacoes"])