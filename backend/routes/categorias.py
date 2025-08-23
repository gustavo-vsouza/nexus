from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_categorias():
    return [{"id": 1, "nome": "Alimentação"}, {"id": 2, "nome": "Transporte"}]
