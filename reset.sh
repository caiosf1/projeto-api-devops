#!/bin/bash

# ========================================
# 🧹 Script de Reset Completo
# ========================================
# Autor: Caio
# Descrição: Para tudo, limpa banco de dados e reconstrói
# Uso: ./reset.sh
# ⚠️  CUIDADO: Apaga TODOS os dados do banco!

echo "╔══════════════════════════════════════════╗"
echo "║  ⚠️  RESET COMPLETO DO PROJETO  ⚠️       ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "⚠️  ATENÇÃO: Este script irá:"
echo "   • Parar todos os containers"
echo "   • APAGAR o banco de dados"
echo "   • Remover volumes Docker"
echo "   • Reconstruir tudo do zero"
echo ""

# Pedir confirmação
read -p "🤔 Tem certeza? (digite 'SIM' para continuar): " confirmacao

if [ "$confirmacao" != "SIM" ]; then
    echo "❌ Operação cancelada!"
    exit 0
fi

echo ""
echo "🧹 Iniciando reset..."
echo ""

# 1. Parar servidor HTTP
echo "🌐 Parando servidor HTTP..."
pkill -f "http.server 8080" 2>/dev/null

# 2. Parar e remover containers + volumes
echo "📦 Parando containers e removendo volumes..."
docker compose down -v

if [ $? -ne 0 ]; then
    echo "❌ Erro ao parar containers!"
    exit 1
fi

# 3. Remover imagem antiga
echo "🗑️  Removendo imagem antiga..."
docker rmi projeto-api-devops-api 2>/dev/null

# 4. Rebuild completo
echo "🔨 Reconstruindo projeto..."
docker compose build --no-cache

if [ $? -ne 0 ]; then
    echo "❌ Erro ao construir imagem!"
    exit 1
fi

# 5. Subir containers
echo "🚀 Subindo containers..."
docker compose up -d

if [ $? -ne 0 ]; then
    echo "❌ Erro ao subir containers!"
    exit 1
fi

# 6. Aguardar inicialização
echo "⏳ Aguardando inicialização..."
sleep 7

# 7. Verificar status
echo ""
echo "📊 Status final:"
docker ps --filter "name=projeto-api-devops" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 8. Subir frontend
echo ""
echo "🌐 Subindo frontend..."
python3 -m http.server 8080 --directory frontend &

sleep 2

echo ""
echo "═══════════════════════════════════════"
echo "✅ RESET COMPLETO COM SUCESSO!"
echo "═══════════════════════════════════════"
echo ""
echo "📚 API: http://localhost:5000/docs"
echo "🎨 Frontend: http://localhost:8080"
echo ""
echo "⚠️  BANCO DE DADOS VAZIO - Crie um novo usuário!"
echo ""
