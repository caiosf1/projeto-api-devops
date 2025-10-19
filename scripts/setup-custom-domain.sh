#!/bin/bash

# ===================================================================================
# 🌐 SCRIPT PARA CONFIGURAR DOMÍNIO PERSONALIZADO
# ===================================================================================
# Este script configura um domínio personalizado no Azure Container Apps
# 
# Uso: ./setup-custom-domain.sh meudominio.com.br
# ===================================================================================

set -e  # Para na primeira erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configurações do Azure
AZURE_RESOURCE_GROUP="rg-projeto-api"
AZURE_CONTAINER_APP="projeto-api-caio"
AZURE_CONTAINER_ENV="env-projeto-api"

# Função para log colorido
log() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se domínio foi fornecido
if [ -z "$1" ]; then
    error "Uso: $0 <seu-dominio.com>"
    echo ""
    echo "Exemplos:"
    echo "  $0 api.meuapp.com.br"
    echo "  $0 meuapp.tech"
    echo "  $0 projeto.site"
    exit 1
fi

CUSTOM_DOMAIN="$1"

echo "=========================================="
echo "🌐 CONFIGURAÇÃO DE DOMÍNIO PERSONALIZADO"
echo "=========================================="
echo ""

log "Domínio a configurar: $CUSTOM_DOMAIN"
log "Container App: $AZURE_CONTAINER_APP"
log "Resource Group: $AZURE_RESOURCE_GROUP"
echo ""

# Verificar se Azure CLI está logado
log "Verificando login no Azure..."
if ! az account show >/dev/null 2>&1; then
    error "Você não está logado no Azure CLI!"
    echo "Execute: az login"
    exit 1
fi

SUBSCRIPTION=$(az account show --query name -o tsv)
success "Logado na subscription: $SUBSCRIPTION"
echo ""

# Verificar se Container App existe
log "Verificando se Container App existe..."
if ! az containerapp show --name $AZURE_CONTAINER_APP --resource-group $AZURE_RESOURCE_GROUP >/dev/null 2>&1; then
    error "Container App '$AZURE_CONTAINER_APP' não encontrado!"
    exit 1
fi

success "Container App encontrado!"
echo ""

# Obter URL atual
CURRENT_URL=$(az containerapp show --name $AZURE_CONTAINER_APP --resource-group $AZURE_RESOURCE_GROUP --query "properties.configuration.ingress.fqdn" -o tsv)
log "URL atual: https://$CURRENT_URL"
echo ""

# Adicionar hostname
log "Adicionando hostname personalizado..."
if az containerapp hostname add \
    --name $AZURE_CONTAINER_APP \
    --resource-group $AZURE_RESOURCE_GROUP \
    --hostname $CUSTOM_DOMAIN; then
    success "Hostname adicionado com sucesso!"
else
    warning "Hostname pode já existir, continuando..."
fi
echo ""

# Obter informações para configurar DNS
log "Obtendo informações para configurar DNS..."
HOSTNAME_INFO=$(az containerapp hostname list \
    --name $AZURE_CONTAINER_APP \
    --resource-group $AZURE_RESOURCE_GROUP \
    --query "[?name=='$CUSTOM_DOMAIN']" -o json)

if [ "$HOSTNAME_INFO" = "[]" ]; then
    error "Falha ao obter informações do hostname!"
    exit 1
fi

# Extrair valores para DNS
VALIDATION_TOKEN=$(echo $HOSTNAME_INFO | jq -r '.[0].customDomainVerificationId')
CNAME_TARGET=$CURRENT_URL

echo "=========================================="
echo "📋 CONFIGURAÇÃO DNS NECESSÁRIA"
echo "=========================================="
echo ""
echo "Configure estes registros no seu provedor de DNS:"
echo ""
echo "1. REGISTRO CNAME:"
echo "   Nome: $CUSTOM_DOMAIN"
echo "   Valor: $CNAME_TARGET"
echo ""
echo "2. REGISTRO TXT (para validação):"
echo "   Nome: asuid.$CUSTOM_DOMAIN"
echo "   Valor: $VALIDATION_TOKEN"
echo ""

warning "IMPORTANTE: Aguarde a propagação DNS (5-30 minutos) antes de continuar!"
echo ""

# Perguntar se quer continuar com certificado SSL
read -p "Já configurou o DNS e quer gerar certificado SSL? (y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    log "Configurando certificado SSL..."
    echo ""
    
    if az containerapp hostname bind \
        --name $AZURE_CONTAINER_APP \
        --resource-group $AZURE_RESOURCE_GROUP \
        --hostname $CUSTOM_DOMAIN \
        --environment $AZURE_CONTAINER_ENV; then
        
        success "Certificado SSL configurado com sucesso!"
        echo ""
        echo "=========================================="
        echo "🎉 CONFIGURAÇÃO COMPLETA!"
        echo "=========================================="
        echo ""
        echo "🔗 Sua API agora está disponível em:"
        echo "   https://$CUSTOM_DOMAIN"
        echo ""
        echo "📚 Documentação:"
        echo "   https://$CUSTOM_DOMAIN/docs"
        echo ""
        echo "🧪 Teste a API:"
        echo "   curl https://$CUSTOM_DOMAIN/auth/register \\"
        echo "     -H 'Content-Type: application/json' \\"
        echo "     -d '{\"email\":\"test@test.com\",\"senha\":\"123456\"}'"
        echo ""
    else
        error "Falha ao configurar certificado SSL!"
        echo ""
        echo "Possíveis causas:"
        echo "1. DNS ainda não propagou (aguarde mais tempo)"
        echo "2. Registros DNS incorretos"
        echo "3. Problemas de conectividade"
        echo ""
        echo "Tente novamente em alguns minutos!"
    fi
else
    echo ""
    echo "=========================================="
    echo "⏳ PRÓXIMOS PASSOS"
    echo "=========================================="
    echo ""
    echo "1. Configure os registros DNS mostrados acima"
    echo "2. Aguarde propagação DNS (5-30 minutos)"
    echo "3. Execute novamente: $0 $CUSTOM_DOMAIN"
    echo ""
    echo "Para verificar propagação DNS:"
    echo "   nslookup $CUSTOM_DOMAIN"
    echo "   nslookup asuid.$CUSTOM_DOMAIN"
fi