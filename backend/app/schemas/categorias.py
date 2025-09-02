from pydantic import BaseModel
from typing import Optional

# Base - campos comuns
class CategoriaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

# Create - herda da base
class CategoriaCreate(CategoriaBase):
    pass

# Update - todos opcionais
class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None

# Response - inclui ID
class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        orm_mode = True  # permite retornar objetos SQLAlchemy
