from app import create_app
import os

# Detecta ambiente de produção
config_class = 'config.ProductionConfig' if os.getenv('FLASK_ENV') == 'production' else 'config.DevelopmentConfig'

app = create_app(config_class)
