#!/bin/bash

# Configurações
SOURCE_SUB="9c0a6208-9f71-4518-a821-85c195342b1e"
DEST_SUB="70f584d3-9cf5-423c-84ba-737de293445d"
RESOURCE_GROUP="rg-projeto-api"

echo "========================================================"
echo "🚀 Script de Migração de Recursos Azure"
echo "Origem: $SOURCE_SUB"
echo "Destino: $DEST_SUB"
echo "Grupo: $RESOURCE_GROUP"
echo "========================================================"

# 1. Verificar se estamos na assinatura correta
echo "1. Definindo contexto para assinatura de origem..."
az account set --subscription $SOURCE_SUB

# 2. Coletar IDs dos recursos
echo "2. Coletando IDs dos recursos em $RESOURCE_GROUP..."
IDS=$(az resource list --resource-group $RESOURCE_GROUP --query "[].id" --output tsv)

if [ -z "$IDS" ]; then
    echo "❌ Nenhum recurso encontrado no grupo $RESOURCE_GROUP"
    exit 1
fi

echo "✅ Recursos encontrados:"
echo "$IDS"

# 3. Executar movimentação
echo "========================================================"
echo "⚠️  ATENÇÃO: O grupo de recursos '$RESOURCE_GROUP' DEVE existir na assinatura de destino!"
echo "⚠️  Se não existir, crie-o antes de continuar."
echo "========================================================"
read -p "Pressione Enter para iniciar a movimentação (ou Ctrl+C para cancelar)..."

echo "3. Iniciando comando de movimentação (isso pode demorar)..."
az resource move \
  --destination-group $RESOURCE_GROUP \
  --destination-subscription-id $DEST_SUB \
  --ids $IDS --verbose

echo "✅ Comando finalizado. Verifique o portal Azure."
