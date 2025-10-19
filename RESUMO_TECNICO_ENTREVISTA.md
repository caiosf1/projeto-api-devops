# 📋 Resumo Técnico - Projeto API DevOps

## 🎯 Elevator Pitch (30s)
"API REST completa de tarefas em Python/Flask com autenticação JWT, deploy automatizado via GitHub Actions na Azure. Container Apps com auto-scaling, PostgreSQL gerenciado, frontend com domínio personalizado e SSL."

---

## 🏗️ Arquitetura Simplificada

```
Usuário
  ↓
app.caiodev.me (Frontend - Azure Static Web Apps)
  ↓
api.caiodev.me (Backend - Azure Container Apps)
  ↓
PostgreSQL (Azure Database)
```

---

## 💻 Stack Técnica

### Backend
- **Python 3.9** com **Flask 2.3+**
- **SQLAlchemy 2.0** (ORM)
- **Flask-JWT-Extended** (autenticação)
- **Bcrypt** (criptografia de senhas)
- **Pydantic** (validação de dados)
- **Flask-RESTX** (Swagger automático)

### Frontend
- **HTML/CSS/JavaScript** (vanilla)
- **Fetch API** para requisições
- **LocalStorage** para tokens

### DevOps
- **Docker** (containerização)
- **GitHub Actions** (CI/CD)
- **Pytest** (testes automatizados)
- **Docker Hub** (registry)

### Cloud (Azure)
- **Container Apps** (0.5 CPU, 1GB RAM, auto-scale 1-10)
- **Database for PostgreSQL** (Flexible Server B1ms, 32GB)
- **Static Web Apps** (tier free)

---

## 🔄 Pipeline CI/CD (4 Etapas)

```
1. TESTES
   └─> pytest, flake8, coverage

2. BUILD
   └─> Docker build, Trivy scan

3. PUSH
   └─> Docker Hub (tag: latest + SHA)

4. DEPLOY
   └─> Azure update + health checks
```

**Tempo total:** ~8-10 minutos
**Trigger:** Push no main

---

## 🔐 Segurança

- ✅ JWT com expiração
- ✅ Bcrypt (hash de senhas)
- ✅ SSL/HTTPS (Let's Encrypt)
- ✅ Secrets no GitHub (não hardcoded)
- ✅ Firewall no PostgreSQL
- ✅ Environment variables

---

## 🚀 Features da API

### Autenticação
- `POST /auth/register` - Criar usuário
- `POST /auth/login` - Login (retorna JWT)

### Tarefas (requer JWT)
- `GET /tarefas` - Listar tarefas do usuário
- `POST /tarefas` - Criar tarefa
- `GET /tarefas/<id>` - Buscar tarefa
- `PUT /tarefas/<id>` - Atualizar tarefa
- `DELETE /tarefas/<id>` - Deletar tarefa

### Health Checks
- `GET /health` - API básica
- `GET /health/db` - API + Banco
- `GET /health/full` - Detalhado

### Documentação
- `GET /docs` - Swagger UI

---

## 📊 Métricas do Projeto

- **Linhas de código:** ~800 (Python) + ~200 (JS)
- **Cobertura de testes:** ~70%
- **Uptime:** 99.9% (SLA Azure)
- **Tempo de deploy:** ~8 minutos
- **Tempo de resposta:** <100ms
- **Custo mensal:** ~$20

---

## 🎓 Conceitos Aplicados

1. **Stateless vs Stateful**
   - Container Apps: stateless (API)
   - PostgreSQL: stateful (dados)

2. **RESTful API**
   - Verbos HTTP corretos
   - Status codes apropriados
   - JSON responses

3. **Autenticação Stateless**
   - JWT no header
   - Não guarda sessões
   - Token auto-validável

4. **CI/CD**
   - Testes antes de deploy
   - Deploy automático
   - Rollback se falhar

5. **Containerização**
   - Isolamento
   - Portabilidade
   - Reprodutibilidade

---

## 🐛 Problema Difícil Resolvido

**PROBLEMA:**
PostgreSQL em Container Apps perdia dados ao reiniciar.

**CAUSA:**
Container Apps são stateless (sem persistência).

**SOLUÇÃO:**
Migrei para Azure Database for PostgreSQL (stateful).

**APRENDIZADO:**
Cada serviço tem seu propósito. Use ferramenta certa para cada problema.

---

## 📈 Possíveis Melhorias

- [ ] Cache com Redis
- [ ] Rate limiting
- [ ] Paginação
- [ ] Filtros avançados
- [ ] Testes de carga
- [ ] Monitoring (Application Insights)
- [ ] Múltiplos ambientes (dev/staging/prod)

---

## 🔗 Links Importantes

- **Frontend:** https://app.caiodev.me
- **API Docs:** https://api.caiodev.me/docs
- **GitHub:** https://github.com/caiosf1/projeto-api-devops
- **Docker Hub:** https://hub.docker.com/r/caiosfdev/projeto-api-devops

---

## 💬 Perguntas Frequentes

**"Fez sozinho?"**
→ "Usei documentação oficial e ferramentas modernas como GitHub Copilot. Todo código eu entendo e consigo explicar."

**"Por que Azure e não AWS?"**
→ "Créditos estudantis + boa documentação. Conceitos são transferíveis (ECS=Container Apps, RDS=Azure Database)."

**"Quanto tempo levou?"**
→ "~2-3 semanas. 1 semana desenvolvimento, 1 semana DevOps/Cloud, 1 semana refinamento."

**"Está em produção?"**
→ "Sim! app.caiodev.me está rodando 24/7 com domínio personalizado e SSL."

---

## ✅ Checklist Demo

- [ ] app.caiodev.me funciona?
- [ ] api.caiodev.me/docs abre?
- [ ] Consigo criar uma tarefa?
- [ ] GitHub Actions está verde?
- [ ] Sei explicar cada camada?

---

## 🎯 Mensagem Final

**Para RH:** "Aplicação web completa com deploy automatizado na nuvem."

**Para Tech Lead:** "API REST em Flask com CI/CD, containers, PostgreSQL gerenciado, auto-scaling."

**Para Sênior:** "Arquitetura 3 camadas, pipeline 4 estágios, autenticação stateless JWT, health checks multi-nível, SSL end-to-end."
