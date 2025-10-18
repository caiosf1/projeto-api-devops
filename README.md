# 📋 Gerenciador de Tarefas Full-Stack

> Sistema completo de gerenciamento de tarefas com backend Flask e frontend Bootstrap 5

[![CI/CD Pipeline](https://github.com/caiosf1/projeto-api-devops/actions/workflows/main.yml/badge.svg)](https://github.com/caiosf1/projeto-api-devops/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)

---

## 🎯 Sobre o Projeto

Aplicação **full-stack** para gerenciamento de tarefas (To-Do List) desenvolvida como projeto de estudos em desenvolvimento web e DevOps. O sistema permite que usuários criem contas, façam login e gerenciem suas tarefas com diferentes níveis de prioridade através de uma interface web moderna e responsiva.

### 🌟 O Que Foi Implementado

**Backend (API REST):**
- ✅ **Autenticação JWT** - Login seguro com tokens
- ✅ **CRUD de Tarefas** - Criar, listar, atualizar e deletar
- ✅ **Validação de Dados** - Pydantic para validação de entrada
- ✅ **Documentação Swagger** - API documentada automaticamente
- ✅ **Testes Automatizados** - 12 testes com pytest

**Frontend (Interface Web):**
- ✅ **Dashboard Interativo** - Visualização de tarefas em tempo real
- ✅ **Sistema de Login/Registro** - Interface de autenticação
- ✅ **Cards de Estatísticas** - Total, pendentes e concluídas
- ✅ **Filtros de Tarefas** - Por status (todas/pendentes/concluídas)
- ✅ **Design Responsivo** - Bootstrap 5 com gradientes modernos

**DevOps:**
- ✅ **Docker** - Containerização completa (API + PostgreSQL)
- ✅ **CI/CD** - GitHub Actions com testes automatizados
- ✅ **Scripts de Automação** - Start, stop, test e reset

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.9+** | **Flask 2.3+** | **Flask-RESTx** (API REST + Swagger)
- **SQLAlchemy** (ORM) | **PostgreSQL** (Produção) | **SQLite** (Testes)
- **Flask-JWT-Extended** (Autenticação) | **Bcrypt** (Hash de senhas)
- **Pydantic** (Validação de dados)

### Frontend
- **HTML5** | **CSS3** | **JavaScript ES6+**
- **Bootstrap 5** (Framework CSS responsivo)
- **Bootstrap Icons** (Ícones)
- **Fetch API** (Comunicação com backend)

### DevOps
- **Docker** + **Docker Compose** (Containerização)
- **GitHub Actions** (CI/CD)
- **pytest** (Testes automatizados)
- **Alembic** (Migrações de banco)

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

# 3. Suba o backend (API + Banco)
docker-compose up --build

# 4. Em outro terminal, suba o frontend
cd frontend
python3 -m http.server 8080

# 5. Acesse a aplicação:
# Frontend: http://localhost:8080
# API Docs: http://localhost:5000/docs
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

## 🏗️ Estrutura do Projeto

```
projeto-api-devops/
├── frontend/              # Interface web
│   ├── index.html         # Página principal
│   ├── app.js             # Lógica JavaScript
│   └── style.css          # Estilos customizados
├── app.py                 # Backend - API REST
├── config.py              # Configurações de ambiente
├── schemas.py             # Validação de dados
├── requirements.txt       # Dependências Python
├── Dockerfile             # Container da aplicação
├── docker-compose.yml     # Orquestração (API + DB)
├── tests/                 # Testes automatizados
│   └── test_api.py        # 12 testes com pytest
└── .github/workflows/     # CI/CD Pipeline
    └── main.yml
```

### Fluxo de Funcionamento

```
Frontend (Browser)
    ↓ HTTP/JSON
Backend (Flask API)
    ↓ JWT + Validação
Banco de Dados (PostgreSQL)
```

---

## 🔒 Segurança

- ✅ Senhas hasheadas com **Bcrypt**
- ✅ Autenticação stateless com **JWT**
- ✅ Validação de entrada com **Pydantic**
- ✅ Proteção contra SQL Injection (SQLAlchemy ORM)
- ✅ Headers de segurança configurados

---

## 🚀 CI/CD Pipeline

**GitHub Actions** executa automaticamente a cada push:

```
git push → GitHub Actions → Testes (pytest) → Build Docker → Deploy
```

✅ Se os testes passarem → Build da imagem Docker  
❌ Se os testes falharem → Pipeline interrompido

---

## 📈 Próximos Passos

- [ ] **Deploy na Azure** - Utilizando Azure App Service com CI/CD
- [ ] **Kubernetes** - Orquestração de containers em produção
- [ ] **Monitoramento** - Grafana + Prometheus para métricas
- [ ] **Frontend Aprimorado** - Melhorias na UI/UX com animações

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
- LinkedIn: [Caio Santos](https://www.linkedin.com/in/caio-santos-555119247/)

---

## 🙏 Agradecimentos

Projeto desenvolvido como parte dos estudos em desenvolvimento backend, DevOps e boas práticas de engenharia de software.

---

<p align="center">Feito com ❤️ e Python</p>
