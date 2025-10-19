# 🔥 PROBLEMAS REAIS E SOLUÇÕES - EXPERIÊNCIA DEVOPS
## *Arsenal para Entrevistas Técnicas*

> **"Conte-me sobre um problema complexo que você resolveu"**  
> **Resposta:** "Deixe-me contar sobre um pipeline CI/CD que tive que debuggar..."

---

## 🎯 **RESUMO EXECUTIVO**
**Projeto:** API Flask + PostgreSQL no Azure Container Apps  
**Problema:** Pipeline falhava sistematicamente no health check  
**Resultado:** 7 problemas críticos resolvidos + pipeline 100% funcional  
**Tempo:** ~4 horas de debugging intensivo  
**Stack:** Docker, Azure Container Apps, GitHub Actions, Flask, PostgreSQL

---

## 🚨 **PROBLEMAS ENCONTRADOS E SOLUÇÕES**

### **1. 🔐 PROBLEMA: Autenticação Docker Hub**
```bash
# ERRO:
Error: buildx failed with: ERROR: failed to solve: 
failed to authorize: rpc error: authentication required
```

**💡 DIAGNÓSTICO:**
- Secrets do GitHub Actions com nomes incorretos
- DOCKER_USERNAME/DOCKER_TOKEN vs DOCKERHUB_USERNAME/DOCKERHUB_TOKEN

**✅ SOLUÇÃO:**
```yaml
# ANTES (errado):
username: ${{ secrets.DOCKER_USERNAME }}
password: ${{ secrets.DOCKER_TOKEN }}

# DEPOIS (correto):
username: ${{ secrets.DOCKERHUB_USERNAME }}  
password: ${{ secrets.DOCKERHUB_TOKEN }}
```

**🎓 LIÇÃO:** Sempre verificar nomes exatos dos secrets no GitHub

---

### **2. 🔑 PROBLEMA: Credenciais Azure Missing**
```bash
# ERRO:
Error: No subscription found. 
Please run 'az login' to set up account.
```

**💡 DIAGNÓSTICO:**
- AZURE_CREDENTIALS secret não configurado
- Service Principal mal configurado

**✅ SOLUÇÃO:**
```bash
# Criação correta do Service Principal:
az ad sp create-for-rbac \
  --name "github-actions-projeto-api" \
  --role contributor \
  --scopes /subscriptions/{subscription-id} \
  --sdk-auth
```

**🎓 LIÇÃO:** Service Principal precisa de escopo correto + formato JSON

---

### **3. 📝 PROBLEMA: Sintaxe Azure CLI Deprecated**
```bash
# ERRO:
argument --environment-variables: expected at least one argument
```

**💡 DIAGNÓSTICO:**
- `--environment-variables` foi deprecado
- Azure CLI mudou sintaxe sem backward compatibility

**✅ SOLUÇÃO:**
```bash
# ANTES (deprecated):
az containerapp update --environment-variables KEY=value

# DEPOIS (atual):
az containerapp update --set-env-vars KEY=value
```

**🎓 LIÇÃO:** Azure CLI muda rapidamente, sempre checar docs atuais

---

### **4. 🐍 PROBLEMA: Flask 2.3+ Deprecation**
```python
# ERRO:
AttributeError: 'Flask' object has no attribute 'before_first_request'
```

**💡 DIAGNÓSTICO:**
- `@app.before_first_request` removido no Flask 2.3+
- Container crashava na inicialização

**✅ SOLUÇÃO:**
```python
# ANTES (deprecated):
@app.before_first_request
def create_tables():
    db.create_all()

# DEPOIS (Flask 2.3+):
with app.app_context():
    db.create_all()
```

**🎓 LIÇÃO:** Sempre testar com versões atuais das dependências

---

### **5. 🔄 PROBLEMA: Container Apps Zero Replicas**
```bash
# SINTOMA:
Status: 504 Gateway Timeout
Replicas: 0 (sempre zerava)
```

**💡 DIAGNÓSTICO:**
- `minReplicas: null` permitia scale-to-zero
- App crashava = Azure matava todas as réplicas

**✅ SOLUÇÃO:**
```bash
az containerapp update \
  --min-replicas 1 \
  --max-replicas 10
```

**🎓 LIÇÃO:** Sempre definir minReplicas > 0 para apps críticos

---

### **6. 🐳 PROBLEMA: Docker Image Cache Issues**
```bash
# SINTOMA:
Container funcionava local, falhava no Azure
Image no Docker Desktop não estava "em uso"
```

**💡 DIAGNÓSTICO:**
- Azure Container Apps usava imagem cached antiga
- Variáveis de ambiente não chegavam no container

**✅ SOLUÇÃO:**
```dockerfile
# Dockerfile melhorado:
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1  # ← Logs em tempo real!
```

**🎓 LIÇÃO:** PYTHONUNBUFFERED=1 é essencial para debugging

---

### **7. 🗄️ PROBLEMA: Database Connection Timeout**
```python
# ERRO:
psycopg2.OperationalError: connection to server at "localhost" failed
```

**💡 DIAGNÓSTICO:**
- POSTGRES_SERVER não definido localmente = fallback localhost
- Container tentava conectar localhost em vez do PostgreSQL interno

**✅ SOLUÇÃO:**
```python
# Config.py melhorado com fallbacks inteligentes:
class ProductionConfig(Config):
    db_server = os.getenv('POSTGRES_SERVER', 'localhost')
    # + validação obrigatória de POSTGRES_PASSWORD
    if not db_password:
        raise ValueError("❌ POSTGRES_PASSWORD obrigatória!")
```

**🎓 LIÇÃO:** Sempre validar variáveis críticas na inicialização

---

## 🛠️ **METODOLOGIA DE DEBUGGING APLICADA**

### **1. Debugging Sistemático:**
```bash
# Sempre seguir essa ordem:
1. Logs do pipeline (GitHub Actions)
2. Logs do Container App (az containerapp logs)
3. Teste local da imagem Docker
4. Validação de variáveis de ambiente
5. Teste de conectividade (curl/telnet)
```

### **2. Ferramentas Utilizadas:**
- **GitHub Actions Logs** → Pipeline debugging
- **Azure CLI** → Container Apps management  
- **Docker Desktop** → Local testing
- **curl com timeouts** → Connectivity testing
- **az containerapp revision list** → Version tracking

### **3. Técnicas de Isolamento:**
```bash
# Isolação de problemas:
1. Testar componente por componente
2. Docker run local vs Azure deploy
3. Variáveis env uma por uma
4. Network connectivity tests
```

---

## 💪 **SKILLS DEMONSTRADAS**

### **DevOps:**
- ✅ CI/CD Pipeline troubleshooting
- ✅ Docker containerization + debugging
- ✅ Azure Container Apps deep knowledge
- ✅ Infrastructure as Code (YML workflows)

### **Backend:**
- ✅ Flask production configuration
- ✅ PostgreSQL connection management
- ✅ Environment variables best practices
- ✅ Application lifecycle management

### **Problem Solving:**
- ✅ Systematic debugging approach
- ✅ Root cause analysis
- ✅ Version compatibility issues
- ✅ Cloud platform specifics

---

## 🎤 **COMO USAR EM ENTREVISTAS**

### **Pergunta Típica:**
*"Conte sobre um problema técnico complexo que você resolveu"*

### **Sua Resposta:**
> *"Recentemente trabalhei em um pipeline CI/CD que falhava sistematicamente. Era um projeto Flask + PostgreSQL no Azure Container Apps. O interessante é que eram múltiplos problemas encadeados..."*
> 
> *"Primeiro, descobri que os secrets do Docker Hub estavam com nomes errados - DOCKER_* vs DOCKERHUB_*. Depois, o Azure CLI tinha mudado a sintaxe de --environment-variables para --set-env-vars. Mas o mais interessante foi quando descobri que o Flask 2.3+ removeu @before_first_request..."*
>
> *"O que me impressionou foi como um problema mascarava o outro. Container zerava réplicas porque crashava, crashava porque Flask não encontrava método deprecated, e eu só descobri isso debuggando container por container..."*

### **Follow-up Questions & Answers:**
- **"Como você debuggou isso?"** → Metodologia sistemática: pipeline → container → local → network
- **"O que você aprendeu?"** → Importância de testar em múltiplas camadas + PYTHONUNBUFFERED para logs
- **"Como evitaria no futuro?"** → Testing matrix com múltiplas versões + better monitoring

---

## 🏆 **RESULTADO FINAL**

```bash
✅ Pipeline 100% funcional
✅ Health checks passando
✅ Auto-scaling configurado (min=1, max=10)  
✅ Logs em tempo real (PYTHONUNBUFFERED)
✅ Security scan integrado (Trivy)
✅ Documentação Swagger automática

🚀 Deploy time: ~3min
🔄 Zero downtime deployments
📊 Monitoring & health checks
```

---

## 🎯 **TAKEAWAYS para ENTREVISTAS**

1. **Mostre processo systematic debugging** - não foi sorte, foi método
2. **Destaque multiple layers** - não foi só código, foi infra + app + pipeline  
3. **Enfatize learning mindset** - cada erro virou conhecimento
4. **Prove business impact** - pipeline funcional = deploys confiáveis
5. **Show future thinking** - como evitar problemas similares

---

> **💡 DICA:** Este documento é seu **arsenal de histórias reais**. Cada seção pode virar uma resposta completa em entrevistas. Mostra experiência prática com problemas que **todo DevOps Engineer enfrenta**!