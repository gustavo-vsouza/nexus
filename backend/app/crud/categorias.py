from sqlalchemy.orm import Session
from app.models.categorias import Categoria

# CREATE
def criar_categoria(db: Session, nome: str, descricao: str = None):
    categoria = Categoria(nome=nome, descricao=descricao)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

# READ - lista todas as categorias
def listar_categorias(db: Session):
    return db.query(Categoria).all()

# READ - busca uma categoria pelo ID
def listar_categoria_por_id(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

# UPDATE
def atualizar_categoria(db: Session, categoria_id: int, nome: str = None, descricao: str = None):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        return None
    if nome is not None:
        categoria.nome = nome
    if descricao is not None:
        categoria.descricao = descricao
    db.commit()
    db.refresh(categoria)
    return categoria

# DELETE
def deletar_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        return None
    db.delete(categoria)
    db.commit()
    return categoria
