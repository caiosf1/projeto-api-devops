#!/bin/bash

# ========================================
# 🧪 Script para Rodar Testes
# ========================================
# Autor: Caio
# Descrição: Executa todos os testes com pytest
# Uso: ./test.sh

echo "╔══════════════════════════════════════════╗"
echo "║      🧪 EXECUTANDO TESTES DO PROJETO    ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# 1. Verificar se está no diretório correto
if [ ! -f "requirements.txt" ]; then
    echo "❌ Erro: Execute este script na raiz do projeto!"
    exit 1
fi

# 2. Verificar se ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "⚠️  Ambiente virtual não encontrado!"
    echo "💡 Criando ambiente virtual..."
    python3 -m venv venv
    
    if [ $? -ne 0 ]; then
        echo "❌ Erro ao criar ambiente virtual!"
        exit 1
    fi
fi

# 3. Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo "❌ Erro ao ativar ambiente virtual!"
    exit 1
fi

# 4. Instalar dependências (se necessário)
echo "📦 Verificando dependências..."
pip install -q -r requirements.txt

# 5. Verificar se pytest está instalado
if ! command -v pytest &> /dev/null; then
    echo "📥 Instalando pytest..."
    pip install -q pytest
fi

# 6. Rodar testes
echo ""
echo "═══════════════════════════════════════"
echo "🧪 INICIANDO TESTES..."
echo "═══════════════════════════════════════"
echo ""

pytest -v --tb=short

# 7. Capturar resultado
TEST_RESULT=$?

echo ""
echo "═══════════════════════════════════════"

# 8. Mostrar resultado final
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ TODOS OS TESTES PASSARAM!"
    echo "═══════════════════════════════════════"
    echo ""
    echo "🎉 Parabéns! Seu código está funcionando perfeitamente!"
    echo "💡 Agora você pode fazer commit com confiança!"
    exit 0
else
    echo "❌ ALGUNS TESTES FALHARAM!"
    echo "═══════════════════════════════════════"
    echo ""
    echo "🔍 Dicas para corrigir:"
    echo "   1. Leia os erros acima com atenção"
    echo "   2. Verifique o arquivo de teste que falhou"
    echo "   3. Corrija o código e rode ./test.sh novamente"
    echo ""
    echo "💡 Para ver mais detalhes: pytest -vv"
    exit 1
fi
