from app import create_app
import os

# Força produção na Vercel
if os.getenv('VERCEL'):
    os.environ['FLASK_ENV'] = 'production'

# Debug
print("🚀 Iniciando API na Vercel")
print(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")
print(f"POSTGRES_SERVER: {os.getenv('POSTGRES_SERVER', 'NAO_CONFIGURADO')}")
print(f"DATABASE_URL: {'CONFIGURADA' if os.getenv('DATABASE_URL') else 'NAO_CONFIGURADA'}")

# Cria app
app = create_app('config.ProductionConfig')
