from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import Base, engine
from app.routes import usuarios, contas, categorias, transacoes

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cria a aplicação FastAPI
app = FastAPI(title="Zentavos API")

# Configuração de CORS
origins = [
    "http://localhost:5173",  # frontend Vue
    "http://127.0.0.1:5173", # caso rode pelo 127 também
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # quem pode acessar
    allow_credentials=True,
    allow_methods=["*"],          # métodos permitidos (GET, POST, PUT, DELETE...)
    allow_headers=["*"],          # headers permitidos
)

# Rotas
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(contas.router, prefix="/contas", tags=["Contas"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
app.include_router(transacoes.router, prefix="/transacoes", tags=["Transacoes"])