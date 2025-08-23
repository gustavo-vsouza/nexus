from pydantic import BaseModel

class TransacaoSchema(BaseModel):
    valor: float
    tipo: str
    categoria_id: int
