from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.crud import usuarios as crud_usuarios
from app.schemas.usuarios import UsuarioCreate, UsuarioResponse, UsuarioUpdate

router = APIRouter()

# CREATE - POST /usuarios
@router.post("/", response_model=UsuarioResponse)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crud_usuarios.criar_usuario(db, usuario.nome, usuario.email, usuario.senha_hash, usuario.status)


# READ - GET /usuarios
@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud_usuarios.listar_usuarios(db)

# READ - GET /usuarios/{id}
@router.get("/{usuario_id}", response_model=UsuarioResponse)
def listar_usuario_por_id(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud_usuarios.listar_usuario_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# UPDATE - PUT /usuarios/{id}
@router.put("/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_db = crud_usuarios.atualizar_usuario(db, usuario_id, usuario.nome, usuario.email, usuario.senha_hash, usuario.status)
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario_db

# DELETE (soft) - DELETE /usuarios/{id}
@router.delete("/{usuario_id}", response_model=UsuarioResponse)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud_usuarios.deletar_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
