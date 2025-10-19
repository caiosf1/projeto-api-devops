# 📋 Gerenciador de Tarefas Full-Stack

> Sistema completo de gerenciamento de tarefas com backend Flask e frontend Bootstrap 5

[![CI/CD Pipeline](https://github.com/caiosf1/projeto-api-devops/actions/workflows/ci-cd-azure.yml/badge.svg)](https://github.com/caiosf1/projeto-api-devops/actions)
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

## 🔒 Segurança & Boas Práticas

### 🛡️ Segurança de Dados
- ✅ **Senhas hasheadas** com Bcrypt (nunca texto plano)
- ✅ **Autenticação JWT** stateless e segura
- ✅ **Validação rigorosa** com Pydantic
- ✅ **Proteção SQL Injection** via SQLAlchemy ORM
- ✅ **Headers de segurança** configurados

### 🔐 Gestão de Credenciais
- ✅ **Variáveis de ambiente** para todas as senhas
- ✅ **GitHub Secrets** para CI/CD (nunca hardcoded)
- ✅ **Arquivo .env.example** como template seguro
- ✅ **.gitignore** protege credenciais locais
- 🚫 **ZERO senhas** no código fonte ou README

### 📋 Como Configurar Credenciais

**1️⃣ Desenvolvimento Local:**
```bash
# Copie o template
cp .env.example .env

# Gere chaves seguras
python3 -c 'import secrets; print("SECRET_KEY:", secrets.token_hex(32))'
python3 -c 'import secrets; print("JWT_SECRET_KEY:", secrets.token_hex(32))'

# Configure no .env (nunca commite!)
```

**2️⃣ GitHub Actions (CI/CD):**
- Configure todas as secrets em: `Settings → Secrets and variables → Actions`
- Required: `DOCKER_USERNAME`, `DOCKER_TOKEN`, `SECRET_KEY`, `JWT_SECRET_KEY`

**3️⃣ Azure Container Apps (Produção):**
- Credenciais via `Environment Variables` no Container App
- Conexão PostgreSQL via rede interna (mais segura)

---

## 🚀 CI/CD Pipeline

**Integração e Deploy Contínuos** com GitHub Actions - automatiza testes e build a cada mudança no código:

### 📋 Como Funciona:

**1️⃣ Desenvolvedor faz push do código**  
↓

**2️⃣ GitHub Actions detecta a mudança automaticamente**  
↓

**3️⃣ INTEGRAÇÃO CONTÍNUA (CI)**
- 🔧 Instala dependências Python
- 🧪 Roda 12 testes automatizados (pytest)
- ✅ **Testes passaram?** → Continua para próxima etapa
- ❌ **Testes falharam?** → PARA AQUI (não faz deploy de código quebrado)

↓

**4️⃣ BUILD & DEPLOY (CD)**
- 🐳 Constrói imagem Docker da aplicação
- 📦 Publica no Docker Hub (pronta para deploy em produção)

---

💡 **Benefício:** Garante que apenas código testado e funcionando vai para produção, automatizando todo o processo de build e validação.

---

## 🌐 **Domínio Personalizado**

Quer usar seu próprio domínio? É simples!

### **🚀 Configuração Automática:**
```bash
# Execute o script de configuração
./scripts/setup-custom-domain.sh meuapp.com.br
```

### **⚙️ Configuração Manual:**
1. Configure DNS: `CNAME api.meuapp.com.br → projeto-api-caio.gentleisland-7ad00bd6.eastus.azurecontainerapps.io`
2. Adicione secret `CUSTOM_DOMAIN` no GitHub  
3. Próximo deploy configurará SSL automaticamente!

📖 **[Guia Completo de Domínio Personalizado](docs/DOMINIO-PERSONALIZADO.md)**

---

## � Deploy em Produção

### 🚀 Aplicação no Ar

**Frontend:** [https://app.caiodev.me](https://app.caiodev.me)  
**API Backend:** [https://api.caiodev.me](https://api.caiodev.me)  
**Documentação:** [https://api.caiodev.me/docs](https://api.caiodev.me/docs)

### ✅ Infraestrutura Azure

**Backend (Azure Container Apps):**
- Container Apps com auto-scaling
- Domínio personalizado com SSL automático
- 0.5 CPU / 1Gi RAM (Consumption tier)
- CI/CD via GitHub Actions

**Frontend (Azure Static Web Apps):**
- Hospedagem estática (Free tier)
- Domínio personalizado configurado
- Deploy automático via GitHub Actions
- CDN global integrado

**Banco de Dados (Azure Database for PostgreSQL):**
- PostgreSQL 14 Flexible Server
- Standard_B1ms (1 vCore, 2GB RAM)
- 32GB storage com backup automático
- SSL/TLS obrigatório

**Registry:** Docker Hub `caiosfdev/projeto-api-devops:latest`

### 🔒 Segurança em Produção

- ✅ Todas as credenciais via GitHub Secrets
- ✅ SSL/TLS automático (Let's Encrypt)
- ✅ Senhas hasheadas com Bcrypt
- ✅ Autenticação JWT stateless
- ✅ PostgreSQL com SSL obrigatório
- ✅ Variáveis de ambiente protegidas

---

---

## 🌐 **Deploy em Produção**

### ✅ **Azure Container Apps** - Sistema Completo Funcionando

**🚀 API Backend:** `https://projeto-api-caio.gentleisland-7ad00bd6.eastus.azurecontainerapps.io`
- ✅ PostgreSQL Container Apps (interno)
- ✅ Autenticação JWT funcionando
- ✅ CRUD completo de tarefas
- ✅ Documentação Swagger ativa

**🔧 Infraestrutura:**
- **Backend:** Azure Container Apps (0.5 CPU / 1Gi RAM)
- **Database:** PostgreSQL 14-Alpine (Container Apps interno)
- **CI/CD:** GitHub Actions (Build → Test → Deploy)
- **Registry:** Docker Hub `caiosfdev/projeto-api-devops:latest`

**🗃️ Configurações PostgreSQL (Produção):**
```bash
POSTGRES_SERVER=postgres-app.internal.[azure-domain]
POSTGRES_USER=[configurado via secrets]
POSTGRES_DB=apitodo
POSTGRES_PORT=5432
# 🔐 Credenciais via variáveis de ambiente (GitHub Secrets)
```

### 🔗 **Domínio Personalizado**
Domain: `caiodev.me` (em configuração)
- DNS configurado e propagado ✅
- SSL automático via Container Apps ⏳

### �📈 Próximos Passos

- [x] **Deploy na Azure** - ✅ Funcionando com Azure Container Apps
- [x] **PostgreSQL** - ✅ Rodando em Container Apps interno  
- [x] **CI/CD Completo** - ✅ GitHub Actions funcionando
- [ ] **Monitoramento** - Application Insights + métricas
- [ ] **CDN** - Azure CDN para frontend estático

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
