from pydantic import BaseModel
from typing import Optional

# Base: comum a criação, atualização e resposta
class ContaBase(BaseModel):
    nome: str
    saldo: Optional[int] = 0

# Para criar conta - exige usuário_id
class ContaCreate(ContaBase):
    usuario_id: int

# Para atualização - todos os campos opcionais
class ContaUpdate(BaseModel):
    nome: Optional[str] = None
    saldo: Optional[int] = None

# Para resposta da API
class ContaResponse(ContaBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True  # permite converter objetos SQLAlchemy em JSON
