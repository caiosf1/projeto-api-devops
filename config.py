import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """Configurações base da aplicação."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'uma-chave-secreta-bem-segura')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'outra-chave-secreta-para-jwt')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configurações para ambiente de desenvolvimento."""
    DEBUG = True
    # SQLite para desenvolvimento local
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')

class TestingConfig(Config):
    """Configurações para ambiente de testes."""
    TESTING = True
    # SQLite em memória para testes (mais rápido)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """Configurações para ambiente de produção (Azure)."""
    DEBUG = False
    
    # Configuração PostgreSQL para produção no Azure Container Apps
    database_url = os.getenv('DATABASE_URL')
    
    if database_url:
        # Azure fornece DATABASE_URL diretamente
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Container Apps PostgreSQL interno - SEMPRE use variáveis de ambiente!
        db_server = os.getenv('POSTGRES_SERVER', 'localhost')
        db_user = os.getenv('POSTGRES_USER', 'postgres')
        db_password = os.getenv('POSTGRES_PASSWORD')  # ⚠️ OBRIGATÓRIA via env vars!
        db_name = os.getenv('POSTGRES_DB', 'apitodo')
        db_port = os.getenv('POSTGRES_PORT', '5432')
        
        # 🔐 Falha se não tiver senha configurada (segurança!)
        if not db_password:
            raise ValueError("❌ POSTGRES_PASSWORD deve ser definida via variável de ambiente!")
        
        # Container Apps internal não usa SSL por padrão + timeout aumentado
        SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}?connect_timeout=30"

# Mapeia nomes de ambiente para classes de configuração
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

def get_config():
    """Retorna configuração baseada na variável FLASK_ENV."""
    env = os.getenv('FLASK_ENV', 'development')
    return config_by_name.get(env, DevelopmentConfig)