from passlib.context import CryptContext

# Define o algoritmo de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Recebe uma senha em texto puro e retorna a senha hasheada"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compara a senha fornecida com a senha salva"""
    return pwd_context.verify(plain_password, hashed_password)
