# 📋 API de Gerenciamento de Tarefas

> API RESTful completa com autenticação JWT, validação de dados e arquitetura DevOps

[![CI/CD Pipeline](https://github.com/caiosf1/projeto-api-devops/actions/workflows/main.yml/badge.svg)](https://github.com/caiosf1/projeto-api-devops/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)

---

## 🎯 Sobre o Projeto

Este projeto é uma **API RESTful** desenvolvida em Python com Flask, focada em demonstrar boas práticas de desenvolvimento backend e DevOps. A aplicação implementa um sistema completo de gerenciamento de tarefas (To-Do List) com autenticação JWT, validação de dados, containerização e CI/CD automatizado.

### 🌟 Principais Características

- ✅ **Autenticação JWT** - Sistema seguro de login e autorização
- ✅ **CRUD Completo** - Create, Read, Update, Delete de tarefas
- ✅ **Validação de Dados** - Usando Pydantic para garantir integridade
- ✅ **Documentação Automática** - Swagger/OpenAPI integrado
- ✅ **Containerização** - Docker e Docker Compose
- ✅ **CI/CD** - Pipeline automatizado com GitHub Actions
- ✅ **Testes Automatizados** - Suite de testes com pytest
- ✅ **Migrações de Banco** - Controle de versão do schema com Alembic

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.9+** - Linguagem principal
- **Flask** - Framework web minimalista e poderoso
- **Flask-RESTx** - Extensão para APIs REST com Swagger
- **SQLAlchemy** - ORM para interação com banco de dados
- **PostgreSQL** - Banco de dados relacional (produção)
- **SQLite** - Banco de dados para testes

### Segurança & Validação
- **Flask-JWT-Extended** - Autenticação e autorização JWT
- **Flask-Bcrypt** - Hash seguro de senhas
- **Pydantic** - Validação de schemas e tipos

### DevOps & Infraestrutura
- **Docker** - Containerização da aplicação
- **Docker Compose** - Orquestração de containers
- **GitHub Actions** - CI/CD automatizado
- **pytest** - Framework de testes

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.9+ (para desenvolvimento local)
- Git

### Opção 1: Com Docker (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/caiosf1/projeto-api-devops.git
cd projeto-api-devops

# 2. Crie o arquivo .env (use o .env.example como base)
cp .env.example .env

# 3. Suba a aplicação
docker-compose up --build

# 4. Acesse a documentação Swagger
# http://localhost:5000/docs
```

### Opção 2: Desenvolvimento Local

```bash
# 1. Clone e entre no diretório
git clone https://github.com/caiosf1/projeto-api-devops.git
cd projeto-api-devops

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure variáveis de ambiente
export FLASK_APP=run.py
export FLASK_ENV=development

# 5. Execute as migrações
flask db upgrade

# 6. Rode a aplicação
python run.py
```

---

## 📚 Documentação da API

### Swagger UI
Acesse `http://localhost:5000/docs` para a documentação interativa completa.

### Endpoints Principais

#### Autenticação

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| POST | `/auth/register` | Registrar novo usuário | Não |
| POST | `/auth/login` | Fazer login e obter token JWT | Não |

#### Tarefas

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/tarefas` | Listar todas as tarefas | JWT |
| POST | `/tarefas` | Criar nova tarefa | JWT |
| GET | `/tarefas/{id}` | Buscar tarefa específica | JWT |
| PUT | `/tarefas/{id}` | Atualizar tarefa | JWT |
| DELETE | `/tarefas/{id}` | Deletar tarefa | JWT |

### Exemplo de Uso

```bash
# 1. Registrar usuário
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "senha": "senha123"}'

# 2. Fazer login
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "senha": "senha123"}'

# Resposta: {"access_token": "eyJ0eXAiOiJKV1QiLCJh..."}

# 3. Criar tarefa (usar o token obtido)
curl -X POST http://localhost:5000/tarefas \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJh..." \
  -d '{"descricao": "Estudar Flask", "prioridade": "alta"}'

# 4. Listar tarefas
curl -X GET http://localhost:5000/tarefas \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJh..."
```

---

## 🧪 Testes

```bash
# Rodar todos os testes
pytest

# Com cobertura
pytest --cov=app --cov-report=html

# Rodar testes específicos
pytest tests/test_api.py -v
```

---

## 🏗️ Arquitetura

```
projeto-api-devops/
├── app.py                 # Aplicação principal e rotas
├── config.py              # Configurações (dev, test, prod)
├── schemas.py             # Validação com Pydantic
├── run.py                 # Entry point da aplicação
├── requirements.txt       # Dependências Python
├── Dockerfile             # Imagem Docker
├── docker-compose.yml     # Orquestração de containers
├── migrations/            # Migrações do banco de dados
│   └── versions/          # Histórico de migrações
├── tests/                 # Suite de testes
│   ├── conftest.py        # Configuração dos testes
│   └── test_api.py        # Testes da API
└── .github/
    └── workflows/
        └── main.yml       # Pipeline CI/CD
```

### Fluxo de Dados

```
Cliente → API (Flask) → Validação (Pydantic) → ORM (SQLAlchemy) → PostgreSQL
           ↓
    Autenticação JWT
           ↓
    Documentação Swagger
```

---

## 🔒 Segurança

- ✅ Senhas hasheadas com **Bcrypt**
- ✅ Autenticação stateless com **JWT**
- ✅ Validação de entrada com **Pydantic**
- ✅ Proteção contra SQL Injection (SQLAlchemy ORM)
- ✅ Headers de segurança configurados

---

## 🚀 CI/CD

O projeto utiliza **GitHub Actions** para:

1. ✅ **Testes Automatizados** - Executa pytest a cada push
2. ✅ **Build Docker** - Constrói imagem Docker
3. ✅ **Push para Docker Hub** - Publica imagem automaticamente
4. ⏳ **Deploy Automático** - (Em implementação)

### Pipeline

```yaml
Push → GitHub → Testes → Build → Docker Hub → Deploy
```

---

## 📈 Melhorias Futuras

- [ ] Implementar relacionamento User ↔ Tarefas (cada usuário vê apenas suas tarefas)
- [ ] Adicionar paginação nas listagens
- [ ] Implementar filtros e busca
- [ ] Adicionar rate limiting
- [ ] Logs estruturados (JSON)
- [ ] Métricas e monitoramento
- [ ] Deploy na Azure
- [ ] Frontend em TypeScript/React

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Caio Santos**

- GitHub: [@caiosf1](https://github.com/caiosf1)
- LinkedIn: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)

---

## 🙏 Agradecimentos

Projeto desenvolvido como parte dos estudos em desenvolvimento backend, DevOps e boas práticas de engenharia de software.

---

<p align="center">Feito com ❤️ e Python</p>
