#!/bin/bash

# ========================================
# 🛑 Script para Parar o Projeto
# ========================================
# Autor: Caio
# Descrição: Para backend (Docker) + frontend (servidor HTTP)
# Uso: ./stop.sh

echo "╔══════════════════════════════════════════╗"
echo "║      🛑 PARANDO PROJETO API DEVOPS      ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# 1. Parar containers Docker
echo "📦 Parando containers Docker..."
docker compose down

if [ $? -eq 0 ]; then
    echo "✅ Containers parados com sucesso!"
else
    echo "⚠️  Erro ao parar containers (talvez já estivessem parados)"
fi

# 2. Parar servidor HTTP do frontend
echo "🌐 Parando servidor HTTP..."
pkill -f "http.server 8080"

if [ $? -eq 0 ]; then
    echo "✅ Servidor HTTP parado!"
else
    echo "⚠️  Servidor HTTP não estava rodando"
fi

# 3. Verificar se tudo foi parado
echo ""
echo "🔍 Verificando processos..."

# Verifica containers
CONTAINERS=$(docker ps --filter "name=projeto-api-devops" --format "{{.Names}}" | wc -l)
if [ $CONTAINERS -eq 0 ]; then
    echo "✅ Nenhum container rodando"
else
    echo "⚠️  Ainda há $CONTAINERS container(s) rodando:"
    docker ps --filter "name=projeto-api-devops" --format "  • {{.Names}}"
fi

# Verifica servidor HTTP
HTTP_PROCESS=$(pgrep -f "http.server 8080" | wc -l)
if [ $HTTP_PROCESS -eq 0 ]; then
    echo "✅ Servidor HTTP parado"
else
    echo "⚠️  Servidor HTTP ainda rodando (PID: $(pgrep -f 'http.server 8080'))"
fi

echo ""
echo "═══════════════════════════════════════"
echo "✅ PROJETO PARADO COM SUCESSO!"
echo "═══════════════════════════════════════"
echo ""
echo "💡 Para iniciar novamente: ./start.sh"
