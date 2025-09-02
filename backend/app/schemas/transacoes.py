from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import datetime

# Base comum: campos que sempre vão existir
class TransacaoBase(BaseModel):
    conta_id: int
    valor: condecimal(max_digits=10, decimal_places=2)  # valida valores monetários
    tipo: str  # "entrada" ou "saida"
    descricao: Optional[str] = None
    categoria_id: Optional[int] = None

# Schema para criação - herda do base
class TransacaoCreate(TransacaoBase):
    pass  # aqui não precisamos adicionar nada além da base

# Schema para atualização - todos opcionais
class TransacaoUpdate(BaseModel):
    conta_id: Optional[int] = None
    valor: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    tipo: Optional[str] = None
    descricao: Optional[str] = None
    categoria_id: Optional[int] = None

# Schema de resposta - inclui ID e datas
class TransacaoResponse(TransacaoBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True  # permite converter objetos do SQLAlchemy para JSON
