# 🚀 Frontend React

## Status: ✅ Funcional!

Esta é uma versão **moderna** do frontend usando **React 18 + Vite + Bootstrap**, demonstrando habilidades em desenvolvimento frontend com tecnologias atuais do mercado.

### 🎯 Objetivo

Demonstrar conhecimento em:
- ⚛️ React (useState, useEffect, Context API)
- 🎨 React Bootstrap  
- 📡 Integração com API REST
- 🔐 Autenticação JWT no frontend
- 🛣️ Roteamento SPA com React Router
- 🎨 CSS moderno (gradients, animations)

### 📦 Como Rodar

```bash
# Instalar dependências
npm install

# Rodar em desenvolvimento
npm run dev

# Build para produção
npm run build
```

**Acesse**: http://localhost:3000

**Acesse**: http://localhost:3000

### 🏗️ Arquitetura

```
src/
├── components/          # Componentes React
│   ├── Auth/           # Login e Register (useState)
│   ├── Dashboard/      # TaskList, TaskForm (useEffect)
│   └── Layout/         # Header, Toast
├── context/            # Context API (AuthContext)
├── services/           # Axios com JWT interceptors
└── index.css           # CSS moderno com animations
```

### 🛠️ Stack

- **React 18** - Framework frontend
- **Vite** - Build tool (ultra-rápido)
- **React Bootstrap** - Componentes UI
- **React Router** - Navegação SPA
- **Axios** - HTTP client com interceptors
- **Context API** - Gerenciamento de estado global

### ⚡ Funcionalidades

✅ **Login/Register** - Autenticação com JWT  
✅ **Dashboard** - Lista de tarefas com filtros  
✅ **CRUD Tarefas** - Criar, editar, deletar  
✅ **Prioridades** - Alta, Média, Baixa  
✅ **Estados** - Pendente, Concluída  
✅ **Persistência** - Token salvo no localStorage  
✅ **Design Moderno** - Gradients, animations, glassmorphism

### 🎓 Conceitos React Demonstrados

- **useState**: Gerenciamento de estado local (formulários, loading, erros)
- **useEffect**: Side effects (carregar tarefas da API)
- **Context API**: Estado global de autenticação
- **Custom Hooks**: useAuth para acessar contexto
- **Controlled Components**: Formulários controlados
- **Async/Await**: Chamadas assíncronas para API
- **Conditional Rendering**: Exibir/ocultar elementos
- **Event Handlers**: onClick, onSubmit, onChange

### 📝 Nota

O frontend principal (Vanilla JS) em `/frontend` está **completo e funcional** em produção.  
Esta versão React é um projeto de aprendizado e modernização do frontend.

### 🔗 Links

- Frontend Produção (Vanilla): https://app.caiodev.me
- API Backend: https://api.caiodev.me
- Documentação API: https://api.caiodev.me/docs
