# 📋 Gerenciador de Tarefas Full-Stack

> Sistema completo de gerenciamento de tarefas com backend Flask, frontend React e DevOps na Azure

[![CI/CD Pipeline](https://github.com/caiosf1/projeto-api-devops/actions/workflows/ci-cd-azure.yml/badge.svg)](https://github.com/caiosf1/projeto-api-devops/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18-61dafb.svg)](https://react.dev/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)

🌐 **[Ver Aplicação ao Vivo](https://app.caiodev.me)** | 📚 **[Documentação API](https://api.caiodev.me/docs)**

---

## 🎯 Sobre o Projeto

Aplicação **full-stack** para gerenciamento de tarefas (To-Do List) desenvolvida como projeto de estudos em desenvolvimento web e DevOps. O sistema permite que usuários criem contas, façam login e gerenciem suas tarefas com diferentes níveis de prioridade através de uma interface web moderna e responsiva.

### 🌟 O Que Foi Implementado

**🔥 Backend (API REST) - Foco Principal:**
- ✅ **Autenticação JWT** - Login seguro com tokens (Flask-JWT-Extended)
- ✅ **CRUD Completo** - Endpoints RESTful com validação
- ✅ **Validação Pydantic** - Schemas com tipos e constraints
- ✅ **Documentação Swagger** - Flask-RESTX com UI interativa
- ✅ **Testes Automatizados** - 12 testes com pytest (100% das rotas)
- ✅ **ORM SQLAlchemy** - Migrations com Alembic
- ✅ **PostgreSQL** - Banco de dados em produção

**🚀 DevOps & Infraestrutura - Destaque:**
- ✅ **Docker** - Containerização completa (API + PostgreSQL)
- ✅ **CI/CD Pipeline** - GitHub Actions (Test → Build → Deploy)
- ✅ **Azure Container Apps** - Deploy automatizado
- ✅ **Azure PostgreSQL** - Banco gerenciado
- ✅ **Domínio Personalizado** - SSL automático (Let's Encrypt)
- ✅ **Health Checks** - Endpoints de monitoramento

**💻 Frontend (Interface Web):**
- ✅ **React 18** - Hooks, Context API, React Router
- ✅ **Vite** - Build tool moderno e rápido
- ✅ **React Bootstrap** - Componentes responsivos
- ✅ **Framer Motion** - Animações suaves
- ✅ **React Toastify** - Notificações toast
- ✅ **Custom Hooks** - useForm, useApi, useLocalStorage
- ✅ **Axios Interceptors** - JWT automático

---

---

## 💪 Habilidades Técnicas Demonstradas

### Backend & APIs
- ✅ Python 3.9+ com Flask
- ✅ Arquitetura REST (CRUD completo)
- ✅ Autenticação JWT (stateless)
- ✅ ORM SQLAlchemy com Migrations
- ✅ Validação de dados (Pydantic V2)
- ✅ Documentação automática (Swagger/OpenAPI)
- ✅ Tratamento de erros e exceções
- ✅ Segurança (bcrypt, CORS, SQL injection prevention)

### DevOps & Cloud
- ✅ Docker + Docker Compose
- ✅ CI/CD com GitHub Actions
- ✅ Deploy Azure Container Apps
- ✅ Azure Database for PostgreSQL
- ✅ Configuração de domínios personalizados
- ✅ SSL/TLS automático
- ✅ Environment variables e secrets management
- ✅ Health checks e monitoramento

### Testes & Qualidade
- ✅ Testes automatizados com pytest
- ✅ Test fixtures e mocks
- ✅ Cobertura de código
- ✅ Testes de integração (API + DB)
- ✅ Testes de autenticação e autorização

### Banco de Dados
- ✅ Modelagem relacional
- ✅ PostgreSQL em produção
- ✅ SQLite para desenvolvimento/testes
- ✅ Migrations versionadas
- ✅ Relacionamentos 1:N com cascade

### Frontend Moderno (React)
- ✅ React 18 com Hooks (useState, useEffect)
- ✅ Context API para gerenciamento de estado
- ✅ React Router (navegação SPA)
- ✅ React Bootstrap (componentes)
- ✅ Axios com interceptors (JWT automático)
- ✅ Vite (build tool moderno)
- ✅ Formulários controlados
- ✅ CSS moderno (gradients, animations)

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.9+** | **Flask 2.3+** | **Flask-RESTx** (API REST + Swagger)
- **SQLAlchemy** (ORM) | **PostgreSQL** (Produção) | **SQLite** (Testes)
- **Flask-JWT-Extended** (Autenticação) | **Bcrypt** (Hash de senhas)
- **Pydantic** (Validação de dados)

### Frontend
- **React 18** - Hooks (useState, useEffect, useContext)
- **React Router v6** - Navegação SPA com rotas protegidas
- **React Bootstrap** - Componentes UI responsivos
- **Vite 5** - Build tool ultrarrápido
- **Axios** - HTTP client com interceptors JWT
- **Framer Motion** - Animações declarativas
- **React Toastify** - Sistema de notificações

### DevOps
- **Docker** + **Docker Compose** (Containerização)
- **GitHub Actions** (CI/CD)
- **pytest** (Testes automatizados)
- **Alembic** (Migrações de banco)

---

## 🚀 Como Usar

### 🌐 Versão em Produção

**A aplicação está ao vivo!**

- 🎨 **Frontend React**: https://app.caiodev.me
- 🔌 **API REST**: https://api.caiodev.me
- 📚 **Swagger Docs**: https://api.caiodev.me/docs

Crie sua conta e comece a usar imediatamente!

---

### 💻 Rodar Localmente (Desenvolvimento)

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.9+ (para desenvolvimento local)
- Git

### Opção 1: Com Docker (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/caiosf1/projeto-api-devops.git
cd projeto-api-devops

# 2. Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas credenciais

# 3. Suba o ambiente completo
docker-compose up --build

# 4. Acesse a aplicação:
# - API: http://localhost:5000
# - API Docs: http://localhost:5000/docs
# - Frontend React: http://localhost:3000 (se rodar npm run dev em frontend-react/)
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

### Endpoints Principais

#### Autenticação
- `POST /auth/register` - Criar nova conta
- `POST /auth/login` - Login (retorna JWT token)

#### Tarefas (🔒 Requer autenticação JWT)
- `GET /tarefas` - Listar tarefas do usuário
- `POST /tarefas` - Criar nova tarefa
- `GET /tarefas/{id}` - Buscar tarefa específica
- `PUT /tarefas/{id}` - Atualizar tarefa
- `DELETE /tarefas/{id}` - Deletar tarefa

### Exemplo de Uso

```bash
# 1. Registrar usuário
curl -X POST https://api.caiodev.me/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "senha": "SenhaForte123!"}'

# 2. Fazer login
curl -X POST https://api.caiodev.me/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "senha": "SenhaForte123!"}'

# Resposta: {"access_token": "eyJ0eXAiOiJKV1QiLCJh..."}

# 3. Criar tarefa (usar o token obtido)
curl -X POST https://api.caiodev.me/tarefas \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJh..." \
  -d '{"descricao": "Estudar Flask", "prioridade": "alta"}'

# 4. Listar tarefas
curl -X GET https://api.caiodev.me/tarefas \
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
├── frontend-react/          # Frontend React 18
│   ├── src/
│   │   ├── components/      # Componentes React
│   │   ├── context/         # Context API (AuthContext)
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # API service (Axios)
│   │   └── App.jsx          # App principal
│   ├── package.json
│   └── vite.config.js
├── app.py                   # Backend - API REST Flask
├── config.py                # Configurações ambiente
├── schemas.py               # Validação Pydantic
├── requirements.txt         # Dependências Python
├── Dockerfile               # Container da aplicação
├── docker-compose.yml       # Orquestração (API + PostgreSQL)
├── tests/                   # Testes automatizados
│   └── test_api.py
└── .github/workflows/       # CI/CD Pipeline
    ├── ci-cd-azure.yml      # Deploy backend
    └── azure-static-web-apps-*.yml  # Deploy frontend
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

📖 **Para configurar domínio personalizado**, veja a documentação completa no projeto.

---

## 🌐 Deploy em Produção

### Aplicação no Ar

- 🎨 **Frontend React**: https://app.caiodev.me
- 🔌 **API Backend**: https://api.caiodev.me
- 📚 **Documentação**: https://api.caiodev.me/docs

### Infraestrutura Azure

**Backend (Azure Container Apps)**
- Container Apps com auto-scaling  
- Domínio personalizado + SSL automático
- CI/CD via GitHub Actions
- Registry: Docker Hub

**Frontend (Azure Static Web Apps)**
- Hospedagem React com CDN global
- Deploy automático de cada commit
- Free tier

**Banco de Dados (Azure PostgreSQL)**
- PostgreSQL 14 Flexible Server
- Backup automático diário
- SSL/TLS obrigatório
- Credenciais via environment variables

### CI/CD Pipeline

Cada push para `main` automaticamente:
1. 🧪 Roda 12 testes (pytest)
2. 🐳 Builda imagem Docker
3. 📤 Push para Docker Hub
4. 🔍 Scan de segurança (Trivy)
5. 🚀 Deploy Azure Container Apps
6. ✅ Health checks automáticos

### Secrets Necessários

Configure no GitHub (`Settings → Secrets → Actions`):
- `DOCKERHUB_USERNAME` / `DOCKERHUB_TOKEN`
- `AZURE_CREDENTIALS` (Service Principal)
- `SECRET_KEY` / `JWT_SECRET_KEY`
- `POSTGRES_PASSWORD`

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
