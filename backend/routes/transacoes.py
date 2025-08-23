from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_transacoes():
    return [{"id": 1, "valor": 100.50, "tipo": "entrada"}]
