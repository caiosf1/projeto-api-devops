# 📋 Gerenciador de Tarefas Full-Stack

> Sistema completo de gerenciamento de tarefas com backend Flask, frontend React e **infraestrutura 100% Azure Cloud**

[![CI/CD Pipeline](https://github.com/caiosf1/projeto-api-devops/actions/workflows/ci-cd-azure.yml/badge.svg)](https://github.com/caiosf1/projeto-api-devops/actions)
[![Azure](https://img.shields.io/badge/Azure-Container%20Apps-0078D4?logo=microsoftazure)](https://azure.microsoft.com/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18-61dafb.svg)](https://react.dev/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)

🌐 **[Ver Aplicação ao Vivo](https://app.caiodev.me)** | 📚 **[Documentação API](https://api.caiodev.me/docs)** | ☁️ **Hospedado em Azure**

---

## 🎯 Sobre o Projeto

Aplicação **full-stack** para gerenciamento de tarefas (To-Do List) desenvolvida como projeto de estudos em **desenvolvimento web, DevOps e Azure Cloud**. 

🔷 **Destaques Azure:**
- **100% hospedado na nuvem Azure** (Container Apps + Static Web Apps + PostgreSQL Flexible Server)
- **CI/CD automatizado** via GitHub Actions → Azure
- **Domínio personalizado** (`caiodev.me`) com SSL/TLS automático
- **Infraestrutura escalável** e pronta para produção

O sistema permite que usuários criem contas, façam login e gerenciem suas tarefas com diferentes níveis de prioridade através de uma interface web moderna e responsiva.

### 🌟 O Que Foi Implementado

**🔥 Backend (API REST) - Foco Principal:**
- ✅ **Autenticação JWT** - Login seguro com tokens (Flask-JWT-Extended)
- ✅ **CRUD Completo** - Endpoints RESTful com validação
- ✅ **Validação Pydantic** - Schemas com tipos e constraints
- ✅ **Documentação Swagger** - Flask-RESTX com UI interativa
- ✅ **Testes Automatizados** - 12 testes com pytest (100% das rotas)
- ✅ **ORM SQLAlchemy** - Migrations com Alembic
- ✅ **PostgreSQL** - Banco de dados em produção

**🚀 DevOps & Azure Cloud - Destaque Principal:**
- ✅ **Azure Container Apps** - Deploy backend containerizado com auto-scaling
- ✅ **Azure Static Web Apps** - Hospedagem React com CDN global
- ✅ **Azure Database for PostgreSQL** - Banco gerenciado (Flexible Server)
- ✅ **Docker** - Containerização completa (API + PostgreSQL)
- ✅ **CI/CD Pipeline** - GitHub Actions integrado com Azure
- ✅ **Domínio Personalizado** - `caiodev.me` com SSL/TLS automático via Azure
- ✅ **Infraestrutura como Código** - Configurações versionadas
- ✅ **Health Checks** - Monitoramento de disponibilidade

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

### DevOps & Cloud (Azure)
- ✅ **Azure Container Apps** - Serverless containers
- ✅ **Azure Static Web Apps** - Hospedagem frontend
- ✅ **Azure PostgreSQL Flexible Server** - Banco gerenciado
- ✅ **Azure CDN** - Distribuição global de conteúdo
- ✅ Docker + Docker Compose
- ✅ CI/CD com GitHub Actions integrado ao Azure
- ✅ Configuração de domínios personalizados com SSL/TLS
- ✅ SSL/TLS automático (Let's Encrypt via Azure)
- ✅ Environment variables e secrets management
- ✅ Health checks e monitoramento
- ✅ Auto-scaling e alta disponibilidade

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
- **GitHub Actions** (CI/CD integrado com Azure)
- **pytest** (Testes automatizados)
- **Alembic** (Migrações de banco)
- **Azure CLI** (Automação de deploy)

### Azure Cloud Services
- **Azure Container Apps** - Backend containerizado
- **Azure Static Web Apps** - Frontend React
- **Azure Database for PostgreSQL** - Flexible Server
- **Azure Container Registry / Docker Hub** - Imagens Docker
- **Azure DNS** - Gerenciamento de domínio

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

✅ **Este projeto já usa domínio personalizado:** `caiodev.me` configurado e funcionando!

**Quer usar seu próprio domínio no Azure?** É simples:

### **🚀 Configuração Automática:**
```bash
# Execute o script de configuração
./scripts/setup-custom-domain.sh meuapp.com.br
```

### **⚙️ Configuração Manual:**
1. Configure DNS: `CNAME api.meuapp.com.br → [seu-container-app].azurecontainerapps.io`
2. No Azure Portal: Container App → Custom domains → Add custom domain
3. Adicione secret `CUSTOM_DOMAIN` no GitHub (opcional para CI/CD)
4. SSL/TLS é configurado automaticamente (Let's Encrypt)

---

## 🌐 Deploy em Produção (Azure Cloud)

### 🎯 Aplicação ao Vivo

- 🎨 **Frontend React**: https://app.caiodev.me (Azure Static Web Apps)
- 🔌 **API Backend**: https://api.caiodev.me (Azure Container Apps)
- 📚 **Documentação**: https://api.caiodev.me/docs (Swagger UI)

### ☁️ Infraestrutura Azure

**🔷 Azure Container Apps (Backend)**
- Hospedagem de containers serverless (0.5 CPU / 1Gi RAM)
- Auto-scaling baseado em demanda
- Domínio personalizado (`caiodev.me`) com SSL/TLS gerenciado
- Deploy automatizado via GitHub Actions
- Zero downtime deployments
- Health checks automáticos

**🔷 Azure Static Web Apps (Frontend)**
- Hospedagem React com CDN global integrado
- Deploy automático a cada commit (GitHub Actions)
- Domínio personalizado (`app.caiodev.me`) com SSL/TLS incluído
- Free tier (sem custos)

**🔷 Azure Database for PostgreSQL (Flexible Server)**
- PostgreSQL 14 gerenciado
- Backup automático diário (7 dias de retenção)
- SSL/TLS obrigatório
- Firewall configurado (apenas Azure Container Apps)

**🔷 Recursos Adicionais**
- **Azure DNS**: Gerenciamento domínio `caiodev.me`
- **Docker Hub**: Registry de imagens
- **GitHub Actions**: CI/CD integrado

### 🔄 CI/CD Pipeline (GitHub Actions → Azure)

**Fluxo Automatizado** a cada push para `main`:

```
📝 Commit & Push
    ↓
🔍 GitHub Actions detecta mudança
    ↓
🧪 Roda 12 testes (pytest)
    ↓
✅ Testes passaram?
    ↓
🐳 Build imagem Docker
    ↓
📤 Push Docker Hub (caiosfdev/projeto-api-devops:latest)
    ↓
🔍 Scan segurança (Trivy - vulnerabilidades)
    ↓
☁️ Deploy Azure Container Apps
    ↓
✅ Health checks automáticos
    ↓
🎉 Aplicação atualizada em produção!
```

**Benefícios:**
- ⚡ Deploy em ~5 minutos
- 🛡️ Apenas código testado vai para produção
- 🔄 Rollback automático se falhar
- 📊 Logs completos no GitHub Actions

### 🔐 Secrets Necessários (GitHub)

Configure em `Settings → Secrets → Actions`:

**Docker Hub:**
- `DOCKERHUB_USERNAME` - Usuário Docker Hub
- `DOCKERHUB_TOKEN` - Token de acesso

**Azure:**
- `AZURE_CREDENTIALS` - Service Principal JSON
- `AZURE_STATIC_WEB_APPS_API_TOKEN` - Token Static Web Apps

**Aplicação:**
- `SECRET_KEY` - Chave secreta Flask
- `JWT_SECRET_KEY` - Chave JWT
- `POSTGRES_PASSWORD` - Senha PostgreSQL Azure

💡 **Nunca commite secrets no código!** Sempre use GitHub Secrets ou Azure Key Vault.

### 📈 Status e Roadmap

**✅ Funcionando:**
- [x] Azure Container Apps + PostgreSQL
- [x] Autenticação JWT completa
- [x] CI/CD automatizado
- [x] Domínio personalizado (`caiodev.me`) com SSL/TLS
- [x] Frontend em Azure Static Web Apps

**🔜 Próximos Passos:**
- [ ] Application Insights (monitoramento avançado)
- [ ] Azure CDN para otimização global
- [ ] Auto-scaling baseado em métricas

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
