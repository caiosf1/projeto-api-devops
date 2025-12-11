from app import create_app
import os

# Na Vercel, sempre queremos produção
if os.getenv('VERCEL'):
    os.environ['FLASK_ENV'] = 'production'

# Debug: Imprimir variáveis de ambiente (CUIDADO COM SENHAS)
print("--- VERCEL DEBUG ---")
print(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")
db_url = os.getenv('DATABASE_URL')
if db_url:
    # Ofusca a senha se houver
    safe_url = db_url.split('@')[-1] if '@' in db_url else 'FORMATO_ATIPICO'
    print(f"DATABASE_URL encontrada: ...@{safe_url}")
else:
    print("DATABASE_URL NAO ENCONTRADA")
    print(f"POSTGRES_SERVER: {os.getenv('POSTGRES_SERVER')}")
    print(f"POSTGRES_HOST: {os.getenv('POSTGRES_HOST')}")

# Detecta ambiente de produção
config_class = 'config.ProductionConfig' if os.getenv('FLASK_ENV') == 'production' else 'config.DevelopmentConfig'

app = create_app(config_class)
