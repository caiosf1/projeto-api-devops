# 🚀 TaskMaster: Arquitetura DevOps & Fullstack Cloud-Native

> **Projeto de Portfólio** desenvolvido para demonstrar competências avançadas em **Engenharia de Software**, **Cloud Computing (Azure)** e **DevOps**.

[![CI/CD Pipeline](https://github.com/caiosf1/projeto-api-devops/actions/workflows/ci-cd-azure.yml/badge.svg)](https://github.com/caiosf1/projeto-api-devops/actions)
[![Azure Container Apps](https://img.shields.io/badge/Azure-Container%20Apps-0078D4?logo=microsoftazure)](https://azure.microsoft.com/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-black?logo=next.js)](https://nextjs.org/)
[![Python Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)](https://www.docker.com/)

🌐 **[Ver Demo Online](https://app.caiodev.me)** | 📚 **[Documentação da API](https://api.caiodev.me/docs)**

---

## 🎯 Sobre o Projeto

O **TaskMaster** é uma aplicação Fullstack robusta projetada para ir além do código básico. Este projeto serve como um laboratório prático para implementação de uma arquitetura **Cloud-Native** completa, focando em:

1.  **Modernidade**: Uso das versões mais recentes de frameworks (Next.js 16, React 19, Tailwind v4).
2.  **Automação**: Pipelines de CI/CD configurados para deploy contínuo.
3.  **Qualidade de Código**: Tipagem, validação de dados (Pydantic) e componentização.
4.  **UX/UI**: Interface moderna com Glassmorphism e animações fluidas.

Este repositório demonstra minha capacidade de entregar soluções de ponta a ponta, desde o design do banco de dados até o deploy automatizado na nuvem.

---

## 🛠️ Tech Stack & Arquitetura

### 🎨 Frontend (Client-Side)
Construído para ser rápido, responsivo e visualmente impactante.
- **Framework**: [Next.js 16](https://nextjs.org/) (App Router & Server Components).
- **Estilização**: [Tailwind CSS v4](https://tailwindcss.com/) com design system customizado e **Glassmorphism**.
- **Interatividade**: [Framer Motion](https://www.framer.com/motion/) para animações de lista e transições de página.
- **Estado & Auth**: Context API para gerenciamento global de sessão e JWT.
- **Integração**: Custom Hooks (`useTarefas`) para abstração da comunicação com a API.

### ⚙️ Backend (Server-Side)
API RESTful focada em segurança e performance.
- **Framework**: Python [Flask](https://flask.palletsprojects.com/).
- **ORM**: SQLAlchemy com suporte a migrações (Flask-Migrate).
- **Validação**: [Pydantic](https://docs.pydantic.dev/) para garantia de integridade de dados (Schemas rigorosos).
- **Segurança**: Autenticação via **JWT (JSON Web Tokens)**, Hashing de senhas com **Bcrypt** e CORS configurado.
- **Documentação**: Swagger UI (OpenAPI) gerado automaticamente via Flask-RESTX.

### ☁️ Infraestrutura & DevOps
- **Containerização**: Docker & Docker Compose (Multi-stage builds).
- **Cloud Provider**: **Microsoft Azure**.
  - Frontend: Azure Static Web Apps.
  - Backend: Azure Container Apps (Serverless Containers).
  - Banco de Dados: Azure Database for PostgreSQL (Flexible Server).
- **CI/CD**: GitHub Actions para Build, Test e Deploy automáticos.

---

## 🚀 Funcionalidades Principais

- [x] **Autenticação Segura**: Login e Registro com validação visual e feedback em tempo real.
- [x] **Gestão de Tarefas**: CRUD completo (Criar, Ler, Atualizar, Deletar).
- [x] **Interface Reativa**: Atualizações otimistas (Optimistic UI) para sensação de instantaneidade.
- [x] **Design Responsivo**: Layout adaptável para Mobile e Desktop com tema "Glass".
- [x] **Proteção de Rotas**: Middleware para redirecionamento de usuários não autenticados.

---

## 🔧 Como Executar Localmente

Siga estes passos para rodar o projeto completo em sua máquina.

### Pré-requisitos
- **Docker** e **Docker Compose** instalados.
- **Git** instalado.

### Passo a Passo Rápido (Docker)

1. **Clone o repositório**
   ```bash
   git clone https://github.com/caiosf1/projeto-api-devops.git
   cd projeto-api-devops
   ```

2. **Suba o ambiente com Docker Compose**
   ```bash
   docker-compose up -d --build
   ```
   *Isso irá construir as imagens do Frontend, Backend e Banco de Dados.*

3. **Acesse a aplicação**
   - **Frontend**: [http://localhost:3000](http://localhost:3000)
   - **API/Swagger**: [http://localhost:5000/docs](http://localhost:5000/docs)

---

## 👨‍💻 Desenvolvimento Manual

Caso prefira rodar sem Docker para desenvolvimento:

### Backend (Python)
```bash
# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt

# Configure o banco (SQLite local)
flask db upgrade

# Rode o servidor
python run.py
```

### Frontend (Node.js)
```bash
cd frontend-nextjs

# Instale dependências (Node v20+)
npm install

# Rode o servidor de desenvolvimento
npm run dev
```

---

## 📚 Estrutura do Repositório

```
/
├── app.py                  # Entrypoint da API Flask
├── config.py               # Configurações de Ambiente (Factory Pattern)
├── schemas.py              # Schemas de Validação Pydantic
├── Dockerfile              # Configuração de Imagem Otimizada
├── docker-compose.yml      # Orquestração de Containers
│
├── frontend-nextjs/        # Aplicação Next.js 16
│   ├── app/                # App Router (Pages & Layouts)
│   ├── components/         # UI Components (Glassmorphism)
│   ├── context/            # Auth Provider
│   └── hooks/              # Lógica de Negócio (Custom Hooks)
│
├── .github/workflows/      # Pipelines de CI/CD (Azure)
└── tests/                  # Testes Automatizados (Pytest)
```

---

## 📬 Contato

**Caio** - *Desenvolvedor Fullstack & Entusiasta DevOps*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/caio-santos-555119247/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/caiosf1)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:scaio2500@gmail.com)

---
*Este projeto é mantido como parte do meu portfólio profissional.*
