from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app import crud, schemas
from app.schemas.contas import ContaCreate, ContaResponse, ContaUpdate

router = APIRouter()

# CREATE - POST /contas
@router.post("/", response_model=ContaResponse)
def criar_conta(conta: ContaCreate, db: Session = Depends(get_db)):
    return crud.contas.criar_conta(db, conta.usuario_id, conta.nome, conta.saldo)

# READ - GET /contas/usuario/{usuario_id}
@router.get("/usuario/{usuario_id}", response_model=list[ContaResponse])
def listar_contas(usuario_id: int, db: Session = Depends(get_db)):
    return crud.contas.listar_contas(db, usuario_id)

# READ - GET /contas/{id}
@router.get("/{conta_id}", response_model=ContaResponse)
def listar_conta_por_id(conta_id: int, db: Session = Depends(get_db)):
    conta = crud.contas.listar_conta_por_id(db, conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta

# UPDATE - PUT /contas/{id}
@router.put("/{conta_id}", response_model=ContaResponse)
def atualizar_conta(conta_id: int, conta: ContaUpdate, db: Session = Depends(get_db)):
    conta_db = crud.contas.atualizar_conta(db, conta_id, conta.nome, conta.saldo)
    if not conta_db:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta_db

# DELETE - DELETE /contas/{id}
@router.delete("/{conta_id}", response_model=ContaResponse)
def deletar_conta(conta_id: int, db: Session = Depends(get_db)):
    conta = crud.contas.deletar_conta(db, conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta
