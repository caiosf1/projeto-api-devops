#!/bin/bash

# ===================================================================================
# 🚀 SCRIPT DE CONFIGURAÇÃO AZURE (CONTAINER APPS - STUDENT FRIENDLY)
# ===================================================================================
# Este script usa Azure Container Apps, que é mais amigável para cotas de estudantes
# do que o App Service Plan B1.

# --- CONFIGURAÇÕES ---
RESOURCE_GROUP="rg-projeto-api"
LOCATION="brazilsouth" # Brazil South está permitida para Azure for Students
ACR_NAME="acrprojetoapi$(date +%s)"
ACA_ENV_NAME="env-projeto-api-devops"
API_APP_NAME="api-backend"
FRONT_APP_NAME="frontend-nextjs"
DB_SERVER_NAME="psql-api-devops-$(date +%s)"
DB_NAME="apitodo"
DB_USER="pgadmin"
DB_PASSWORD="SuaSenhaForte123!"

echo "🚀 Iniciando configuração da infraestrutura Azure (Container Apps)..."

# 1. Verificar Resource Group (Criado pelo usuário)
echo "📦 Verificando Resource Group: $RESOURCE_GROUP..."
if ! az group show --name $RESOURCE_GROUP &>/dev/null; then
    echo "❌ Erro: Resource Group '$RESOURCE_GROUP' não encontrado!"
    echo "⚠️  Por favor, crie o Resource Group na sua assinatura de estudante antes de rodar este script."
    exit 1
fi
echo "✅ Resource Group encontrado!"

# 2. Criar Azure Container Registry (ACR)
echo "🐳 Criando ACR: $ACR_NAME..."
az acr create --resource-group $RESOURCE_GROUP --name $ACR_NAME --sku Basic --admin-enabled true

# Obter credenciais do ACR
ACR_USERNAME=$(az acr credential show --name $ACR_NAME --query "username" -o tsv)
ACR_PASSWORD=$(az acr credential show --name $ACR_NAME --query "passwords[0].value" -o tsv)
ACR_LOGIN_SERVER=$(az acr show --name $ACR_NAME --query "loginServer" -o tsv)

echo "✅ ACR Criado: $ACR_LOGIN_SERVER"

# 3. Criar Ambiente Container Apps
echo "🏗️ Criando Log Analytics e Container Apps Environment..."
LOG_ANALYTICS_WORKSPACE="log-$ACA_ENV_NAME"
az monitor log-analytics workspace create --resource-group $RESOURCE_GROUP --workspace-name $LOG_ANALYTICS_WORKSPACE --location $LOCATION

LOG_ANALYTICS_CUSTOMER_ID=$(az monitor log-analytics workspace show --query customerId -g $RESOURCE_GROUP -n $LOG_ANALYTICS_WORKSPACE -o tsv)
LOG_ANALYTICS_SHARED_KEY=$(az monitor log-analytics workspace get-shared-keys --query primarySharedKey -g $RESOURCE_GROUP -n $LOG_ANALYTICS_WORKSPACE -o tsv)

az containerapp env create --name $ACA_ENV_NAME --resource-group $RESOURCE_GROUP --location $LOCATION --logs-workspace-id $LOG_ANALYTICS_CUSTOMER_ID --logs-workspace-key $LOG_ANALYTICS_SHARED_KEY

# 4. Criar Banco de Dados PostgreSQL (Flexible Server)
echo "🐘 Criando PostgreSQL Flexible Server: $DB_SERVER_NAME..."
# Usando Standard_B1ms que é geralmente disponível para estudantes (Burstable)
az postgres flexible-server create --resource-group $RESOURCE_GROUP --name $DB_SERVER_NAME --location $LOCATION --admin-user $DB_USER --admin-password $DB_PASSWORD --sku-name Standard_B1ms --tier Burstable --version 13 --storage-size 32 --yes

# Criar banco de dados específico
az postgres flexible-server db create --resource-group $RESOURCE_GROUP --server-name $DB_SERVER_NAME --database-name $DB_NAME

# Permitir acesso de serviços Azure
az postgres flexible-server firewall-rule create --resource-group $RESOURCE_GROUP --name $DB_SERVER_NAME --rule-name AllowAzureIPs --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0

DB_HOST=$(az postgres flexible-server show --resource-group $RESOURCE_GROUP --name $DB_SERVER_NAME --query "fullyQualifiedDomainName" -o tsv)
echo "✅ Banco de Dados Criado: $DB_HOST"

# 5. Criar Container App para API (Backend)
# Usamos uma imagem hello-world temporária pois a nossa ainda não foi buildada
echo "🐍 Criando Container App (API): $API_APP_NAME..."
az containerapp create --name $API_APP_NAME --resource-group $RESOURCE_GROUP --environment $ACA_ENV_NAME --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest --target-port 8000 --ingress external --min-replicas 1 --max-replicas 1 --env-vars FLASK_ENV=production POSTGRES_HOST=$DB_HOST POSTGRES_USER=$DB_USER POSTGRES_PASSWORD=$DB_PASSWORD POSTGRES_DB=$DB_NAME SECRET_KEY="SuaSecretKey" JWT_SECRET_KEY="SuaJwtSecret" PORT=8000

API_URL=$(az containerapp show --resource-group $RESOURCE_GROUP --name $API_APP_NAME --query properties.configuration.ingress.fqdn -o tsv)
echo "✅ API URL: https://$API_URL"

# 6. Criar Container App para Frontend
echo "⚛️ Criando Container App (Frontend): $FRONT_APP_NAME..."
az containerapp create --name $FRONT_APP_NAME --resource-group $RESOURCE_GROUP --environment $ACA_ENV_NAME --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest --target-port 3000 --ingress external --min-replicas 1 --max-replicas 1 --env-vars NEXT_PUBLIC_API_URL="https://$API_URL" PORT=3000

FRONTEND_URL=$(az containerapp show --resource-group $RESOURCE_GROUP --name $FRONT_APP_NAME --query properties.configuration.ingress.fqdn -o tsv)
echo "✅ Frontend URL: https://$FRONTEND_URL"

# Atualizar CORS na API com a URL do Frontend
echo "🔄 Atualizando CORS na API..."
az containerapp update --name $API_APP_NAME --resource-group $RESOURCE_GROUP --set-env-vars CORS_ORIGIN="https://$FRONTEND_URL"

echo "🎉 Infraestrutura (Container Apps) criada com sucesso!"
echo "--------------------------------------------------"
echo "Resource Group: $RESOURCE_GROUP"
echo "ACR Name: $ACR_NAME"
echo "API App Name: $API_APP_NAME"
echo "Frontend App Name: $FRONT_APP_NAME"
echo "API URL: https://$API_URL"
echo "Frontend URL: https://$FRONTEND_URL"
echo "DB Host: $DB_HOST"
echo "--------------------------------------------------"
