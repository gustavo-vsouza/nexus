from sqlalchemy.orm import Session
from app.models.usuarios import Usuario
from app.utils.security import hash_password

# CREATE
def criar_usuario(db: Session, nome: str, email: str, senha: str, status: bool = True):
    senha_hash = hash_password(senha)  # 🔑 faz o hash antes de salvar
    db_usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=senha_hash,
        status=status
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# READ
def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def listar_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

# UPDATE
def atualizar_usuario(db: Session, usuario_id: int, nome: str = None, email: str = None,
                      senha_hash: str = None, status: str = None):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None
    if nome is not None:
        usuario.nome = nome
    if email is not None:
        usuario.email = email
    if senha_hash is not None:
        usuario.senha_hash = senha_hash
    if status is not None:
        usuario.status = status
    db.commit()
    db.refresh(usuario)
    return usuario

# DELETE (soft delete -> muda status)
def deletar_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None
    usuario.status = "inativo"
    db.commit()
    db.refresh(usuario)
    return usuario
