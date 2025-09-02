from pydantic import BaseModel, EmailStr
from typing import Optional

# Base comum: nome, email e status
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr  # valida automaticamente formato de email
    status: Optional[str] = "ativo"

# Schema para criação - exige senha
class UsuarioCreate(UsuarioBase):
    senha_hash: str

# Schema para atualização - todos opcionais
class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha_hash: Optional[str] = None
    status: Optional[str] = None

# Schema de resposta - inclui o ID
class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True  # permite que objetos do SQLAlchemy virem JSON automaticamente
