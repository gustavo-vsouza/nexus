from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app import crud, schemas
from app.schemas.categorias import CategoriaCreate, CategoriaResponse, CategoriaUpdate


router = APIRouter()

# CREATE - POST /categorias/
@router.post("/", response_model=CategoriaResponse)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return crud.categorias.criar_categoria(db, categoria.nome, categoria.descricao)

# READ - GET /categorias/
@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.categorias.listar_categorias(db)

# READ - GET /categorias/{id}
@router.get("/{categoria_id}", response_model=CategoriaResponse)
def listar_categoria_por_id(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.categorias.listar_categoria_por_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

# UPDATE - PUT /categorias/{id}
@router.put("/{categoria_id}", response_model=CategoriaResponse)
def atualizar_categoria(categoria_id: int, categoria: CategoriaUpdate, db: Session = Depends(get_db)):
    categoria_db = crud.categorias.atualizar_categoria(db, categoria_id, categoria.nome, categoria.descricao)
    if not categoria_db:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria_db

# DELETE - DELETE /categorias/{id}
@router.delete("/{categoria_id}", response_model=CategoriaResponse)
def deletar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.categorias.deletar_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria
