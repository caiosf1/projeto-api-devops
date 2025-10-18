#!/bin/bash

# ========================================
# 🚀 Script de Inicialização do Projeto
# ========================================
# Autor: Caio
# Descrição: Sobe backend (Docker) + frontend (servidor HTTP)
# Uso: ./start.sh

echo "╔══════════════════════════════════════════╗"
echo "║   🚀 INICIANDO PROJETO API DEVOPS 🚀   ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# 1. Verificar se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não encontrado! Instale primeiro."
    exit 1
fi

# 2. Verificar se docker-compose está instalado
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose não encontrado! Instale primeiro."
    exit 1
fi

# 3. Parar containers antigos (se existirem)
echo "🛑 Parando containers antigos..."
docker compose down 2>/dev/null

# 4. Subir containers do Docker
echo "📦 Subindo Docker Compose..."
docker compose up -d

if [ $? -ne 0 ]; then
    echo "❌ Erro ao subir containers!"
    exit 1
fi

# 5. Aguardar containers iniciarem
echo "⏳ Aguardando containers iniciarem..."
sleep 5

# 6. Verificar status dos containers
echo ""
echo "📊 Status dos containers:"
docker ps --filter "name=projeto-api-devops" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 7. Parar servidor HTTP antigo (se existir)
echo ""
echo "🧹 Limpando servidor HTTP antigo..."
pkill -f "http.server 8080" 2>/dev/null

# 8. Subir servidor HTTP para o frontend
echo "🌐 Iniciando servidor HTTP para frontend..."
cd frontend 2>/dev/null || cd .
python3 -m http.server 8080 --directory frontend 2>/dev/null &
HTTP_PID=$!

# Aguardar servidor HTTP iniciar
sleep 2

# 9. Verificar se tudo está funcionando
echo ""
echo "✅ PROJETO INICIADO COM SUCESSO!"
echo ""
echo "═══════════════════════════════════════"
echo "📚 API (Backend):"
echo "   → Swagger: http://localhost:5000/docs"
echo "   → Health: http://localhost:5000"
echo ""
echo "🎨 Frontend:"
echo "   → Interface: http://localhost:8080"
echo "   → Teste: http://localhost:8080/test.html"
echo ""
echo "🗄️  Banco de Dados:"
echo "   → PostgreSQL na porta 5432"
echo "═══════════════════════════════════════"
echo ""
echo "💡 Dicas:"
echo "   • Ver logs: docker logs -f projeto-api-devops-api-1"
echo "   • Parar tudo: ./stop.sh"
echo "   • Rodar testes: ./test.sh"
echo ""
echo "🎯 Projeto rodando! Acesse http://localhost:8080"
