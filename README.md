
# 💰 Sistema de Gerenciamento Financeiro

Este projeto é uma **API REST** desenvolvida com **FastAPI + SQLAlchemy** para auxiliar no gerenciamento financeiro de usuários.  
Ele permite controlar **usuários, contas, categorias e transações** de forma organizada e escalável.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** → Framework para criação de APIs rápidas e performáticas.
- **SQLAlchemy** → ORM para comunicação com o banco de dados.
- **PostgreSQL** → Banco de dados relacional (pode ser alterado para outro compatível).
- **Pydantic** → Validação de dados e schemas.
- **Uvicorn** → Servidor ASGI para rodar a aplicação.

---

## ⚙️ Estrutura do Projeto

```
app/
│
├── crud/                 # Regras de CRUD (Create, Read, Update, Delete)
│   ├── usuarios.py
│   ├── contas.py
│   ├── categorias.py
│   └── transacoes.py
│
├── database/             # Conexão e base do banco
│   └── connection.py
│
├── models/               # Modelos SQLAlchemy (tabelas do banco)
│   ├── usuarios.py
│   ├── contas.py
│   ├── categorias.py
│   └── transacoes.py
│
├── routes/               # Rotas da API
│   ├── usuarios.py
│   ├── contas.py
│   ├── categorias.py
│   └── transacoes.py
│
├── schemas/              # Schemas Pydantic (validação e resposta)
│   ├── usuarios.py
│   ├── contas.py
│   ├── categorias.py
│   └── transacoes.py
│
└── main.py               # Arquivo principal da aplicação
```

---

## 🛠️ Como Rodar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/gustavo-vsouza/nexus.git
   cd nexus
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**
   - No arquivo `app/database/connection.py`, ajuste a `DATABASE_URL` com os dados do seu PostgreSQL:
     ```python
     DATABASE_URL = "postgresql://usuario:senha@localhost:5432/nome_banco"
     ```

5. **Crie as tabelas no banco**
   ```bash
   python -m app.database.connection
   ```

6. **Inicie a aplicação**
   ```bash
   uvicorn app.main:app --reload
   ```

7. **Acesse a documentação interativa**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Funcionalidades Principais

### 👤 Usuários
- Criar novo usuário
- Listar usuários
- Buscar usuário por ID
- Atualizar informações do usuário
- Inativar usuário (soft delete)

### 💳 Contas
- Criar contas vinculadas a usuários
- Listar contas de um usuário
- Atualizar nome ou saldo da conta
- Excluir conta

### 🏷️ Categorias
- Criar categorias de transações
- Listar categorias
- Atualizar nome/descrição
- Excluir categoria

### 💸 Transações
- Criar transação vinculada a uma conta e categoria
- Listar transações de uma conta
- Buscar transação por ID
- Atualizar valor, descrição ou data
- Excluir transação

---

## 🔒 Segurança
- As senhas dos usuários são salvas **criptografadas** (`senha_hash`).
- O sistema permite controle de usuários e segregação de dados por conta.

---

## 📂 Próximos Passos
- Implementar autenticação (JWT).
- Criar relatórios financeiros (saldo total, gastos por categoria, etc.).
- Adicionar testes automatizados.

---

👨‍💻 Desenvolvido como parte de um **projeto de aprendizado e gerenciamento financeiro pessoal**.
