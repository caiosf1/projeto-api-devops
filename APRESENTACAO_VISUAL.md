# 🎨 Apresentação Visual - Projeto API DevOps

## 📱 Slide 1: Introdução

```
╔══════════════════════════════════════════════════╗
║                                                  ║
║      🚀 API DE TAREFAS COM CI/CD NA AZURE       ║
║                                                  ║
║  • API REST completa (Python/Flask)              ║
║  • Deploy automatizado (GitHub Actions)          ║
║  • Em produção com domínio personalizado         ║
║                                                  ║
║  👤 Caio                                         ║
║  🔗 app.caiodev.me                               ║
║  📚 api.caiodev.me/docs                          ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

---

## 🏗️ Slide 2: Arquitetura

```
┌─────────────────────────────────────────────────┐
│                   USUÁRIO                        │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  🎨 FRONTEND (Azure Static Web Apps)            │
│  • HTML/CSS/JavaScript                          │
│  • app.caiodev.me                               │
│  • SSL Automático                               │
└────────────────┬────────────────────────────────┘
                 │ HTTPS
                 ▼
┌─────────────────────────────────────────────────┐
│  ⚙️  BACKEND (Azure Container Apps)             │
│  • Flask API (Python 3.9)                       │
│  • api.caiodev.me                               │
│  • Auto-scaling 1-10                            │
│  • JWT Authentication                           │
└────────────────┬────────────────────────────────┘
                 │ PostgreSQL
                 ▼
┌─────────────────────────────────────────────────┐
│  🗄️  DATABASE (Azure PostgreSQL)                │
│  • Flexible Server B1ms                         │
│  • 32GB Storage                                 │
│  • Backup Automático                            │
└─────────────────────────────────────────────────┘
```

---

## 🔄 Slide 3: Pipeline CI/CD

```
    📝 git push origin main
         │
         ▼
    ┌─────────────┐
    │  🧪 TESTES  │ ← pytest + coverage
    └──────┬──────┘
           │ ✅ Passou
           ▼
    ┌─────────────┐
    │  🐳 BUILD   │ ← Docker build
    └──────┬──────┘
           │ ✅ Criado
           ▼
    ┌─────────────┐
    │  📦 PUSH    │ ← Docker Hub
    └──────┬──────┘
           │ ✅ Publicado
           ▼
    ┌─────────────┐
    │  🚀 DEPLOY  │ ← Azure update
    └──────┬──────┘
           │ ✅ Concluído
           ▼
    ┌─────────────┐
    │  ✅ LIVE!   │ ← api.caiodev.me
    └─────────────┘

    ⏱️  Tempo total: ~8-10 minutos
    🔄 Totalmente automatizado
```

---

## 💻 Slide 4: Stack Técnica

```
┌────────────────┬─────────────────────────────────┐
│   CATEGORIA    │         TECNOLOGIAS             │
├────────────────┼─────────────────────────────────┤
│ Backend        │ Python, Flask, SQLAlchemy       │
│ Autenticação   │ JWT, Bcrypt                     │
│ Validação      │ Pydantic                        │
│ Documentação   │ Swagger (Flask-RESTX)           │
│ Testes         │ Pytest, Pytest-cov              │
│ Containers     │ Docker, Docker Compose          │
│ CI/CD          │ GitHub Actions                  │
│ Cloud          │ Azure (3 serviços)              │
│ Frontend       │ HTML, CSS, JavaScript           │
│ Versionamento  │ Git, GitHub                     │
└────────────────┴─────────────────────────────────┘
```

---

## 🔐 Slide 5: Segurança

```
✅ IMPLEMENTADO:

1. Autenticação JWT
   └─> Token no header Authorization

2. Criptografia de Senhas
   └─> Bcrypt (salt + hash)

3. SSL/HTTPS
   └─> Let's Encrypt automático

4. Secrets Management
   └─> GitHub Secrets (não hardcoded)

5. Firewall Database
   └─> Só Azure services

6. Environment Variables
   └─> Configuração externa

7. CORS Configurado
   └─> Apenas domínios permitidos
```

---

## 📊 Slide 6: Endpoints da API

```
┌──────────────────────────────────────────────────┐
│  AUTENTICAÇÃO (público)                          │
├──────────────────────────────────────────────────┤
│  POST /auth/register  → Criar usuário            │
│  POST /auth/login     → Login (retorna JWT)      │
└──────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────┐
│  TAREFAS (requer JWT)                            │
├──────────────────────────────────────────────────┤
│  GET    /tarefas      → Listar todas             │
│  POST   /tarefas      → Criar nova               │
│  GET    /tarefas/:id  → Buscar específica        │
│  PUT    /tarefas/:id  → Atualizar                │
│  DELETE /tarefas/:id  → Deletar                  │
└──────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────┐
│  MONITORING                                      │
├──────────────────────────────────────────────────┤
│  GET /health          → Status API               │
│  GET /health/db       → Status Database          │
│  GET /health/full     → Detalhado                │
│  GET /docs            → Swagger UI               │
└──────────────────────────────────────────────────┘
```

---

## 🎯 Slide 7: Funcionalidades

```
✨ FEATURES IMPLEMENTADAS:

📝 CRUD Completo de Tarefas
   • Criar, Ler, Atualizar, Deletar

🔐 Sistema de Autenticação
   • Registro de usuários
   • Login com JWT
   • Proteção de rotas

👤 Multi-usuário
   • Cada usuário vê apenas suas tarefas
   • Isolamento de dados

⚡ Performance
   • Auto-scaling (1-10 instâncias)
   • Respostas < 100ms
   • Cache de conexões DB

📚 Documentação
   • Swagger UI interativa
   • Testes executáveis
   • Exemplos de request/response

🔍 Monitoring
   • Health checks em 3 níveis
   • Logs centralizados
   • Métricas de uptime
```

---

## 🐛 Slide 8: Desafio Técnico

```
❌ PROBLEMA ENCONTRADO:

"PostgreSQL em Container Apps perdia dados"

🔍 INVESTIGAÇÃO:
• Dados sumiam após restart
• Container Apps reinicia frequentemente
• Logs mostravam banco "vazio"

💡 CAUSA RAIZ:
Container Apps = STATELESS
PostgreSQL precisa ser STATEFUL

✅ SOLUÇÃO:
Migrar para Azure Database for PostgreSQL
(serviço gerenciado e persistente)

📚 APRENDIZADO:
Cada serviço tem seu propósito:
• Container Apps → Aplicações (stateless)
• Azure Database → Dados (stateful)
```

---

## 📈 Slide 9: Métricas

```
┌─────────────────────────────────────────────────┐
│              MÉTRICAS DO PROJETO                 │
├──────────────────────┬──────────────────────────┤
│ Linhas de Código     │ ~1000 linhas             │
│ Testes               │ 15+ testes               │
│ Cobertura            │ ~70%                     │
│ Uptime               │ 99.9% (SLA Azure)        │
│ Tempo de Deploy      │ 8-10 minutos             │
│ Tempo de Resposta    │ < 100ms                  │
│ Custo Mensal         │ ~$20                     │
│ Commits              │ 50+                      │
│ Branches             │ main + develop           │
│ Workflows            │ 2 (backend + frontend)   │
└──────────────────────┴──────────────────────────┘
```

---

## 🚀 Slide 10: Demo ao Vivo

```
1️⃣  FRONTEND
    → https://app.caiodev.me
    → Criar/editar/deletar tarefa

2️⃣  API DOCS
    → https://api.caiodev.me/docs
    → Testar endpoints
    → Ver esquemas

3️⃣  GITHUB
    → Ver código
    → Ver workflows
    → Ver commits recentes

4️⃣  AZURE PORTAL
    → Ver recursos
    → Ver métricas
    → Ver logs

5️⃣  DEPLOY AO VIVO
    → Alterar código
    → git push
    → Ver pipeline rodar
    → Ver mudança em produção
```

---

## 📚 Slide 11: O Que Aprendi

```
🎓 CONCEITOS:

✅ DevOps
   • CI/CD pipelines
   • Containerização
   • Deploy automatizado

✅ Cloud Computing
   • Serviços gerenciados
   • Auto-scaling
   • Pay-as-you-go

✅ APIs RESTful
   • Verbos HTTP
   • Status codes
   • JSON responses

✅ Segurança
   • Autenticação JWT
   • Criptografia
   • HTTPS/SSL

✅ Arquitetura
   • Separação de camadas
   • Stateless vs Stateful
   • Escalabilidade

✅ Boas Práticas
   • Código limpo
   • Testes automatizados
   • Documentação
```

---

## 🔮 Slide 12: Próximos Passos

```
📋 MELHORIAS PLANEJADAS:

1. Performance
   └─> Redis para cache
   └─> CDN para static files
   └─> Query optimization

2. Features
   └─> Paginação
   └─> Filtros avançados
   └─> Notificações

3. DevOps
   └─> Ambientes separados (dev/staging/prod)
   └─> Testes de carga (Locust)
   └─> Monitoring avançado

4. Frontend
   └─> Migrar para React/Vue
   └─> PWA (Progressive Web App)
   └─> Mobile responsivo

5. Segurança
   └─> Rate limiting
   └─> WAF (Web Application Firewall)
   └─> Testes de penetração
```

---

## 💼 Slide 13: Links & Contato

```
┌─────────────────────────────────────────────────┐
│                   📱 CONTATOS                    │
├─────────────────────────────────────────────────┤
│                                                 │
│  🌐 Frontend:                                   │
│     https://app.caiodev.me                      │
│                                                 │
│  📚 API Docs:                                   │
│     https://api.caiodev.me/docs                 │
│                                                 │
│  💻 GitHub:                                     │
│     github.com/caiosf1/projeto-api-devops       │
│                                                 │
│  🐳 Docker Hub:                                 │
│     hub.docker.com/r/caiosfdev/projeto-api-...  │
│                                                 │
│  📧 Email:                                      │
│     [seu-email]                                 │
│                                                 │
│  💼 LinkedIn:                                   │
│     [seu-linkedin]                              │
│                                                 │
└─────────────────────────────────────────────────┘

         🙏 OBRIGADO PELA OPORTUNIDADE!
```

---

## 🎯 Comandos para Demo Ao Vivo

```bash
# 1. Teste básico da API
curl https://api.caiodev.me/health

# 2. Registrar usuário
curl -X POST https://api.caiodev.me/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"demo@example.com","senha":"test123"}'

# 3. Fazer login
curl -X POST https://api.caiodev.me/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"demo@example.com","senha":"test123"}'

# 4. Criar tarefa (com token)
curl -X POST https://api.caiodev.me/tarefas \
  -H "Authorization: Bearer TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{"descricao":"Demo ao vivo","prioridade":"alta"}'

# 5. Ver logs do Azure
az containerapp logs show \
  --name projeto-api-caio \
  --resource-group rg-projeto-api \
  --tail 20

# 6. Ver status do GitHub Actions
gh run list --limit 5

# 7. Fazer deploy ao vivo
echo "Alterando mensagem..." >> app.py
git add .
git commit -m "demo: atualização ao vivo"
git push origin main
# Aguardar 8 minutos
```

---

## ✅ DICA FINAL

```
╔═══════════════════════════════════════════════╗
║                                               ║
║  🎯 MENSAGEM PRINCIPAL:                       ║
║                                               ║
║  "Sou INICIANTE, mas tenho INICIATIVA.       ║
║                                               ║
║   Desenvolvi esse projeto para APRENDER       ║
║   DevOps e Cloud na prática.                  ║
║                                               ║
║   Não sei tudo, mas sei RESOLVER PROBLEMAS   ║
║   e APRENDO RÁPIDO.                           ║
║                                               ║
║   Busco uma oportunidade para crescer com     ║
║   um time experiente."                        ║
║                                               ║
╚═══════════════════════════════════════════════╝
```
