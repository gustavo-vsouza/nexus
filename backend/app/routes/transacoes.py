from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app import crud
from app.schemas.transacoes import TransacaoCreate, TransacaoResponse, TransacaoUpdate

router = APIRouter()

# CREATE - POST /transacoes
@router.post("/", response_model=TransacaoResponse)
def criar_transacao(transacao: TransacaoCreate, db: Session = Depends(get_db)):
    return crud.transacoes.criar_transacao(
        db,
        conta_id=transacao.conta_id,
        valor=transacao.valor,
        tipo=transacao.tipo,
        descricao=transacao.descricao,
        categoria_id=transacao.categoria_id
    )

# READ - GET /transacoes
@router.get("/", response_model=list[TransacaoResponse])
def listar_transacoes(db: Session = Depends(get_db)):
    return crud.transacoes.listar_transacoes(db)

# READ - GET /transacoes/{id}
@router.get("/{transacao_id}", response_model=TransacaoResponse)
def listar_transacao_por_id(transacao_id: int, db: Session = Depends(get_db)):
    transacao = crud.transacoes.listar_transacao_por_id(db, transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacao

# UPDATE - PUT /transacoes/{id}
@router.put("/{transacao_id}", response_model=TransacaoResponse)
def atualizar_transacao(transacao_id: int, transacao: TransacaoUpdate, db: Session = Depends(get_db)):
    transacao_db = crud.transacoes.atualizar_transacao(
        db,
        transacao_id=transacao_id,
        conta_id=transacao.conta_id,
        valor=transacao.valor,
        tipo=transacao.tipo,
        descricao=transacao.descricao,
        categoria_id=transacao.categoria_id
    )
    if not transacao_db:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacao_db

# DELETE - DELETE /transacoes/{id}
@router.delete("/{transacao_id}", response_model=TransacaoResponse)
def deletar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    transacao = crud.transacoes.deletar_transacao(db, transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacao
