# ===================================================================================
# 🔧 CONFIGURAÇÕES DA APLICAÇÃO - PADRÃO DE MÚLTIPLOS AMBIENTES
# ===================================================================================
# Este arquivo gerencia configurações para DESENVOLVIMENTO, TESTES e PRODUÇÃO.
#
# POR QUE SEPARAR CONFIGURAÇÕES?
# --------------------------------
# 1. SEGURANÇA: Produção usa banco real, dev usa SQLite local
# 2. PERFORMANCE: Testes usam SQLite em memória (mais rápido)
# 3. DEBUG: Dev mostra erros detalhados, produção esconde (segurança)
# 4. FLEXIBILIDADE: Muda ambiente sem alterar código (só variável)
#
# HIERARQUIA DE CLASSES:
# ----------------------
# Config (base)
#   ├─ DevelopmentConfig (herda Config)
#   ├─ TestingConfig (herda Config)
#   └─ ProductionConfig (herda Config)

import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# ===================================================================================
# 📦 DOTENV - CARREGA VARIÁVEIS DE AMBIENTE
# ===================================================================================
# O QUE É .env?
# Arquivo local que armazena segredos (senhas, chaves API) fora do código
# Exemplo de .env:
# SECRET_KEY=minhaChaveSecreta123
# DATABASE_URL=postgresql://user:pass@localhost/db
#
# POR QUE USAR?
# ✅ Segredos não vão pro Git (segurança)
# ✅ Cada desenvolvedor tem seus próprios valores
# ✅ CI/CD injeta variáveis sem alterar código
#
# IMPORTANTE: .env deve estar no .gitignore!
load_dotenv()


# ===================================================================================
# 🔐 CLASSE BASE - CONFIGURAÇÕES COMUNS A TODOS AMBIENTES
# ===================================================================================
class Config:
    """
    Configurações base herdadas por todos os ambientes.
    
    CHAVES SECRETAS:
    ----------------
    SECRET_KEY: Usado pelo Flask para criptografar sessões e cookies
        - Geração: python -c "import secrets; print(secrets.token_hex(32))"
        - NUNCA commite chave real no Git!
        - Produção: variável de ambiente obrigatória
        
    JWT_SECRET_KEY: Usado para assinar tokens JWT (autenticação)
        - Tokens são assinados com essa chave
        - Backend valida assinatura antes de confiar no token
        - Se mudar a chave, todos tokens ficam inválidos (força re-login)
    
    SQLALCHEMY_TRACK_MODIFICATIONS:
    -------------------------------
    False = Desabilita sistema de eventos do SQLAlchemy
    - Economiza memória
    - Flask-SQLAlchemy recomenda desabilitar (causa warnings se True)
    - Só útil se você usa sinais (signals) do SQLAlchemy
    """
    
    # os.getenv('CHAVE', 'valor_padrão') → busca variável de ambiente, usa padrão se não achar
    # Padrões aqui são APENAS para desenvolvimento/testes
    # Produção SEMPRE usa variáveis de ambiente reais (segurança)
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-NUNCA-USE-EM-PRODUCAO')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'dev-jwt-key-NUNCA-USE-EM-PRODUCAO')
    
    # Desabilita tracking de modificações (economia de memória)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# ===================================================================================
# 💻 DESENVOLVIMENTO - AMBIENTE LOCAL DO PROGRAMADOR
# ===================================================================================
class DevelopmentConfig(Config):
    """
    Configurações para desenvolvimento local.
    
    DEBUG = True:
    -------------
    ✅ Hot reload (código muda, servidor reinicia automaticamente)
    ✅ Erros detalhados no navegador (stacktrace completo)
    ✅ Debugger interativo (console Python no erro)
    ⚠️  NUNCA use DEBUG=True em produção (expõe código fonte!)
    
    # SQLite:
    -------
    Banco de dados em arquivo único (dev.db)
    ✅ Não precisa instalar PostgreSQL
    ✅ Simples para testar localmente
    ✅ Portável (commit dev.db no .gitignore)
    ❌ Não suporta múltiplas conexões simultâneas (produção precisa PostgreSQL)
    """
    DEBUG = True
    
    # Reduz rounds do Bcrypt para desenvolvimento (login instantâneo)
    # Padrão é 12 (lento para segurança). 4 é o mínimo (rápido para dev).
    BCRYPT_LOG_ROUNDS = 4
    
    # SQLite para desenvolvimento local
    # 'sqlite:///dev.db' cria arquivo dev.db na pasta do projeto
    # Três barras (///) = caminho relativo
    # Quatro barras (////) = caminho absoluto: sqlite:////home/user/db.db
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')


# ===================================================================================
# 🧪 TESTES - AMBIENTE DE PYTEST
# ===================================================================================
class TestingConfig(Config):
    """
    Configurações para testes automatizados (pytest).
    
    TESTING = True:
    ---------------
    ✅ Desabilita CSRF (Cross-Site Request Forgery) em formulários
    ✅ Muda comportamento de exceções (não captura para debug)
    ✅ Flask-Login desabilita requisito de login real
    
    SQLite in-memory:
    -----------------
    'sqlite:///:memory:' cria banco TEMPORÁRIO na RAM
    ✅ Muito mais rápido (não grava disco)
    ✅ Limpa automaticamente após teste
    ✅ Isolamento total (cada teste cria banco novo)
    ❌ Perde dados ao encerrar (OK para testes!)
    
    USO:
    ----
    pytest → usa TestingConfig automaticamente (ver conftest.py)
    """
    TESTING = True
    
    # SQLite em memória (temporário, rápido)
    # :memory: = especial do SQLite, não cria arquivo
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# ===================================================================================
# 🚀 PRODUÇÃO - AZURE CLOUD (PostgreSQL + Container Apps)
# ===================================================================================
class ProductionConfig(Config):
    """
    Configurações para produção (Vercel/Azure).
    
    Suporta dois métodos de configuração:
    1. DATABASE_URL completa (ex: Vercel, Heroku)
    2. Variáveis individuais (POSTGRES_SERVER, POSTGRES_PASSWORD, etc.)
    """
    DEBUG = False
    
    # Tenta DATABASE_URL primeiro (padrão Vercel/Heroku/Railway)
    database_url = os.getenv('DATABASE_URL')
    
    if database_url:
        # Corrige postgres:// para postgresql:// se necessário
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Monta a partir de variáveis individuais
        db_server = os.getenv('POSTGRES_SERVER') or os.getenv('POSTGRES_HOST')
        db_user = os.getenv('POSTGRES_USER', 'postgres')
        db_password = os.getenv('POSTGRES_PASSWORD')
        db_name = os.getenv('POSTGRES_DB', 'apitodo')
        db_port = os.getenv('POSTGRES_PORT', '5432')
        ssl_mode = os.getenv('POSTGRES_SSL_MODE', 'prefer')
        
        if db_password and db_server:
            # Codifica senha para URL (@ vira %40, etc)
            db_password_encoded = quote_plus(db_password)
            
            if ssl_mode == 'require':
                SQLALCHEMY_DATABASE_URI = (
                    f"postgresql://{db_user}:{db_password_encoded}@{db_server}:{db_port}/{db_name}"
                    f"?sslmode=require&connect_timeout=60&application_name=projeto-api-devops"
                )
            else:
                SQLALCHEMY_DATABASE_URI = (
                    f"postgresql://{db_user}:{db_password_encoded}@{db_server}:{db_port}/{db_name}"
                    f"?connect_timeout=60&application_name=projeto-api-devops"
                )
        elif os.getenv('FLASK_ENV') == 'production':
            raise ValueError(
                "❌ ERRO: Configure DATABASE_URL ou (POSTGRES_SERVER + POSTGRES_PASSWORD)"
            )
        else:
            SQLALCHEMY_DATABASE_URI = None
            
    # CORS
    # Padrão agora é liberar geral (*) para evitar bloqueios em produção; se quiser restringir,
    # defina CORS_ORIGINS com lista separada por vírgula.
    CORS_ORIGINS = os.getenv(
        'CORS_ORIGINS',
        '*'
    ).split(',')
# ===================================================================================
# 🗺️ MAPEAMENTO DE AMBIENTES
# ===================================================================================
# Dicionário que mapeia nome do ambiente → classe de configuração
# Usado em create_app(config_class) e get_config()
config_by_name = {
    'development': DevelopmentConfig,  # Desenvolvimento local
    'testing': TestingConfig,          # Pytest
    'production': ProductionConfig     # Azure Cloud
}


def get_config():
    """
    Retorna classe de configuração baseada em variável de ambiente.
    
    USO:
    ----
    # No código:
    from config import get_config
    app.config.from_object(get_config())
    
    # No terminal:
    export FLASK_ENV=production  # Linux/Mac
    set FLASK_ENV=production     # Windows
    
    # No Docker/Azure:
    docker run -e FLASK_ENV=production myapp
    
    ORDEM DE PRECEDÊNCIA:
    ---------------------
    1. Variável de ambiente FLASK_ENV
    2. Padrão 'development' (se FLASK_ENV não existe)
    
    RETORNO:
    --------
    Classe de configuração (DevelopmentConfig, TestingConfig ou ProductionConfig)
    
    EXEMPLO:
    --------
    >>> os.environ['FLASK_ENV'] = 'production'
    >>> config = get_config()
    >>> print(config.__name__)
    'ProductionConfig'
    """
    env = os.getenv('FLASK_ENV', 'development')  # Padrão: development
    
    # Busca classe no dicionário, fallback para DevelopmentConfig
    # dict.get(key, default) retorna default se key não existe
    return config_by_name.get(env, DevelopmentConfig)