#!/bin/bash

# Script de inicialização para Azure App Service
echo "🚀 Iniciando aplicação no Azure App Service..."

# Instalar dependências (caso não estejam no container)
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Executar migrações do banco de dados
echo "🗄️ Executando migrações do banco..."
python -m flask db upgrade

# Iniciar aplicação Flask
echo "✅ Iniciando servidor Flask..."
python run.py