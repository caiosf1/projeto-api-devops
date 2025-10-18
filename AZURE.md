# ☁️ Azure DevOps - Guia de Migração

## 🎯 Objetivo

Migrar o pipeline de CI/CD do **GitHub Actions** para **Azure DevOps** para demonstrar conhecimento na stack completa da vaga Deloitte.

---

## 📋 Pré-requisitos

1. ✅ Conta Azure (GitHub Student Pack - $100 de créditos)
2. ✅ Projeto criado no Azure DevOps
3. ✅ Repositório conectado ao Azure DevOps
4. ✅ Service Connection configurado

---

## 🚀 Passo a Passo

### 1️⃣ Criar Organização e Projeto no Azure DevOps

1. Acesse: https://dev.azure.com
2. Crie uma **Organization** (ex: `caiosf1`)
3. Crie um **Project** (ex: `projeto-api-devops`)
4. Escolha: **Git** como controle de versão

### 2️⃣ Conectar Repositório GitHub

**Opção A: Import do GitHub para Azure Repos**
```bash
# No Azure DevOps -> Repos -> Import Repository
# URL: https://github.com/caiosf1/projeto-api-devops
```

**Opção B: Manter no GitHub e integrar** (Recomendado)
- Azure DevOps pode ler diretamente do GitHub
- Configurar no Pipeline: **GitHub** como source

### 3️⃣ Criar Pipeline YAML

Criar arquivo: `azure-pipelines.yml` na raiz do projeto

```yaml
# ===================================================================================
# Azure DevOps Pipeline - CI/CD
# ===================================================================================

trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  pythonVersion: '3.9'
  dockerRegistryServiceConnection: 'DockerHubConnection'
  imageRepository: 'caiosfdev/api-tarefas'
  dockerfilePath: '$(Build.SourcesDirectory)/Dockerfile'
  tag: '$(Build.BuildId)'

stages:
  # ===================================================================================
  # STAGE 1: Build e Testes
  # ===================================================================================
  - stage: Build
    displayName: 'Build and Test'
    jobs:
      - job: Test
        displayName: 'Run Tests'
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '$(pythonVersion)'
            displayName: 'Use Python $(pythonVersion)'

          - script: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt
              pip install pytest pytest-cov
            displayName: 'Install dependencies'

          - script: |
              pytest --junitxml=junit/test-results.xml --cov=app --cov-report=xml
            displayName: 'Run tests with pytest'

          - task: PublishTestResults@2
            condition: succeededOrFailed()
            inputs:
              testResultsFiles: '**/test-results.xml'
              testRunTitle: 'Python $(pythonVersion)'
            displayName: 'Publish test results'

          - task: PublishCodeCoverageResults@1
            inputs:
              codeCoverageTool: Cobertura
              summaryFileLocation: '$(System.DefaultWorkingDirectory)/**/coverage.xml'
            displayName: 'Publish code coverage'

  # ===================================================================================
  # STAGE 2: Build Docker Image
  # ===================================================================================
  - stage: Docker
    displayName: 'Build and Push Docker Image'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - job: BuildPush
        displayName: 'Build and Push'
        steps:
          - task: Docker@2
            displayName: 'Build Docker Image'
            inputs:
              command: build
              repository: $(imageRepository)
              dockerfile: $(dockerfilePath)
              tags: |
                $(tag)
                latest

          - task: Docker@2
            displayName: 'Push to Docker Hub'
            inputs:
              command: push
              repository: $(imageRepository)
              containerRegistry: $(dockerRegistryServiceConnection)
              tags: |
                $(tag)
                latest

  # ===================================================================================
  # STAGE 3: Deploy para Azure (Opcional - quando ativar)
  # ===================================================================================
  - stage: Deploy
    displayName: 'Deploy to Azure'
    dependsOn: Docker
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployWeb
        displayName: 'Deploy to Azure App Service'
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebAppContainer@1
                  displayName: 'Deploy to Azure App Service'
                  inputs:
                    azureSubscription: 'AzureServiceConnection'
                    appName: 'api-tarefas-app'
                    containers: $(imageRepository):$(tag)
```

### 4️⃣ Configurar Service Connections

#### Docker Hub Connection
1. **Project Settings** → **Service connections**
2. **New service connection** → **Docker Registry**
3. **Docker Hub**
4. Informar:
   - Docker ID: `caiosfdev`
   - Password/Token: (seu token do Docker Hub)
   - Service connection name: `DockerHubConnection`

#### Azure Service Connection (para deploy)
1. **New service connection** → **Azure Resource Manager**
2. **Service principal (automatic)**
3. Selecionar subscription
4. Nome: `AzureServiceConnection`

### 5️⃣ Criar Pipeline no Azure DevOps

1. **Pipelines** → **Create Pipeline**
2. **Where is your code?** → GitHub (ou Azure Repos)
3. **Select a repository** → `caiosf1/projeto-api-devops`
4. **Configure your pipeline** → **Existing Azure Pipelines YAML file**
5. Selecionar: `/azure-pipelines.yml`
6. **Run**

---

## 🎯 Recursos Azure para Deploy

### Opção 1: Azure App Service (Recomendado para começar)

**Vantagens:**
- ✅ Fácil de configurar
- ✅ Suporte a containers Docker
- ✅ Auto-scaling
- ✅ Monitoramento integrado

**Criar via Azure CLI:**
```bash
# Login
az login

# Criar Resource Group
az group create --name rg-api-tarefas --location brazilsouth

# Criar App Service Plan
az appservice plan create \
  --name plan-api-tarefas \
  --resource-group rg-api-tarefas \
  --is-linux \
  --sku B1

# Criar Web App com Container
az webapp create \
  --resource-group rg-api-tarefas \
  --plan plan-api-tarefas \
  --name api-tarefas-app \
  --deployment-container-image-name caiosfdev/api-tarefas:latest

# Configurar variáveis de ambiente
az webapp config appsettings set \
  --resource-group rg-api-tarefas \
  --name api-tarefas-app \
  --settings \
    SECRET_KEY="sua-chave-aqui" \
    JWT_SECRET_KEY="sua-chave-jwt" \
    POSTGRES_USER="usuario" \
    POSTGRES_PASSWORD="senha" \
    POSTGRES_DB="apitodo" \
    POSTGRES_HOST="seu-postgres.database.windows.net"
```

### Opção 2: Azure Container Apps (Mais moderno)

**Vantagens:**
- ✅ Serverless
- ✅ Auto-scaling agressivo (scale to zero)
- ✅ Melhor para microservices
- ✅ Mais barato

### Opção 3: Azure Kubernetes Service (Avançado)

**Vantagens:**
- ✅ Full Kubernetes
- ✅ Escalabilidade máxima
- ✅ Melhor para produção enterprise

**Desvantagens:**
- ⚠️ Mais complexo
- ⚠️ Mais caro

---

## 📊 Dashboards e Monitoramento

### Application Insights
```bash
# Criar Application Insights
az monitor app-insights component create \
  --app api-tarefas-insights \
  --location brazilsouth \
  --resource-group rg-api-tarefas \
  --application-type web
```

### Adicionar no código Python:
```python
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

# Configurar Application Insights
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=...'
))
```

---

## 🎯 Checklist Final

- [ ] Pipeline criado no Azure DevOps
- [ ] Testes rodando automaticamente
- [ ] Build Docker funcionando
- [ ] Push para Docker Hub automático
- [ ] Service Connections configurados
- [ ] App Service criado na Azure
- [ ] Deploy automático funcionando
- [ ] Application Insights configurado
- [ ] Variáveis de ambiente configuradas
- [ ] PostgreSQL na Azure (opcional)

---

## 💰 Estimativa de Custos (com $100 de créditos)

| Recurso | Tier | Custo/mês | Nota |
|---------|------|-----------|------|
| App Service | B1 | ~$13 | Básico, suficiente |
| PostgreSQL | B1 | ~$25 | Single Server |
| Application Insights | Free | $0 | 5GB/mês grátis |
| **TOTAL** | | **~$38/mês** | **2.5 meses com $100** |

**Dica:** Use tier Free/Basic para estudos!

---

## 📚 Recursos Úteis

- Documentação Azure DevOps: https://docs.microsoft.com/en-us/azure/devops/
- Azure App Service: https://docs.microsoft.com/en-us/azure/app-service/
- Azure CLI: https://docs.microsoft.com/en-us/cli/azure/
- Pricing Calculator: https://azure.microsoft.com/en-us/pricing/calculator/

---

## 🎯 Próximos Passos

1. ✅ Criar conta Azure (GitHub Student Pack)
2. ✅ Criar organização no Azure DevOps
3. ✅ Criar `azure-pipelines.yml`
4. ✅ Configurar Service Connections
5. ✅ Rodar primeiro pipeline
6. ✅ Criar App Service
7. ✅ Configurar deploy automático
8. ✅ Adicionar no README: badges do Azure DevOps

---

**Tempo estimado: 4-6 horas** (incluindo aprendizado) 🚀
