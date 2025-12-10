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
    Configurações para produção no Azure.
    
    DEBUG = False:
    --------------
    ⚠️  NUNCA deixe DEBUG=True em produção!
    ✅ Erros genéricos (não expõe código)
    ✅ Performance otimizada
    ✅ Logs controlados
    
    POSTGRESQL:
    -----------
    POR QUE NÃO SQLITE EM PRODUÇÃO?
    ❌ SQLite não aguenta múltiplas conexões simultâneas
    ❌ Não tem performance para alta carga
    ✅ PostgreSQL suporta milhares de conexões
    ✅ ACID completo (transações seguras)
    ✅ Suporte oficial do Azure
    
    VARIÁVEIS DE AMBIENTE NO AZURE:
    -------------------------------
    POSTGRES_SERVER = nome-do-servidor.postgres.database.azure.com
    POSTGRES_USER = seu_usuario
    POSTGRES_PASSWORD = [obtida de variável de ambiente - NUNCA no código!]
    POSTGRES_DB = nome_do_banco
    POSTGRES_PORT = 5432 (padrão PostgreSQL)
    POSTGRES_SSL_MODE = require (Azure obriga SSL para segurança)
    
    CONNECTION STRING:
    ------------------
    Formato: postgresql://usuario:senha@servidor:porta/banco?sslmode=require
    Exemplo: postgresql://user:***@server.postgres.database.azure.com:5432/db?sslmode=require
    (senha é URL-encoded automaticamente pelo quote_plus)
    """
    DEBUG = False
    
    # Tenta obter DATABASE_URL diretamente (algumas plataformas fornecem pronto)
    database_url = os.getenv('DATABASE_URL')
    
    if database_url:
        # Se DATABASE_URL existe, usa diretamente
        # Exemplo: Heroku, Railway, Azure Container Apps fornecem assim
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Monta connection string a partir de variáveis individuais
        # Usado quando você configura variáveis manualmente no Azure Portal
        
        db_server = os.getenv('POSTGRES_SERVER', 'localhost')
        db_user = os.getenv('POSTGRES_USER', 'postgres')
        db_password = os.getenv('POSTGRES_PASSWORD')  # Sem padrão (segurança!)
        db_name = os.getenv('POSTGRES_DB', 'apitodo')
        db_port = os.getenv('POSTGRES_PORT', '5432')
        
        # SSL Mode:
        # 'require' = obrigatório SSL (Azure Database for PostgreSQL)
        # 'prefer' = tenta SSL, fallback sem SSL (flexível)
        # 'disable' = sem SSL (NUNCA use em produção!)
        ssl_mode = os.getenv('POSTGRES_SSL_MODE', 'prefer')
        
    # 🔐 VALIDAÇÃO DE SEGURANÇA
    # Falha rápido se senha não estiver configurada
    # Melhor falhar no startup do que rodar sem banco!
    # MAS: Só falha se estivermos realmente em produção (FLASK_ENV=production)
    # Isso evita erro ao importar config.py em desenvolvimento
    
    # Suporte a DATABASE_URL direta (padrão Vercel/Neon/Supabase)
    database_url = os.getenv('DATABASE_URL')
    
    if database_url:
        # Corrige postgres:// para postgresql:// se necessário (SQLAlchemy requer postgresql://)
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    elif not db_password:
        if os.getenv('FLASK_ENV') == 'production':
            raise ValueError(
                "❌ ERRO CRÍTICO: POSTGRES_PASSWORD ou DATABASE_URL não está configurada!\n"
                "Configure no Azure Portal: Container Apps → Environment variables\n"
                "Ou via Azure CLI: az containerapp update --name <app> "
                "--set-env-vars POSTGRES_PASSWORD=<senha>"
            )
        else:
            # Se não for produção, define URI inválida/vazia para não quebrar import
            # Se alguém tentar usar ProductionConfig sem senha, vai falhar na conexão
            SQLALCHEMY_DATABASE_URI = None
    else:
        # 🔒 URL ENCODING
        # Por que quote_plus?
        # Senhas podem ter caracteres especiais: @, !, #, &
        # Esses caracteres quebram URL: postgres://user:p@ss@host → interpreta @ como separador
        # quote_plus('p@ss') → 'p%40ss' (@ vira %40)
        db_password_encoded = quote_plus(db_password)
        
        # MONTA CONNECTION STRING
        # Formato: driver://user:pass@host:port/db?opcoes
        
        if ssl_mode == 'require':
            # Azure Database for PostgreSQL (serviço gerenciado)
            # Requer SSL para conexões externas (segurança)
            # connect_timeout=60 → espera 60s antes de falhar (rede lenta)
            # application_name → identificação na monitoramento (Azure Monitor)
            SQLALCHEMY_DATABASE_URI = (
                f"postgresql://{db_user}:{db_password_encoded}@{db_server}:{db_port}/{db_name}"
                f"?sslmode=require&connect_timeout=60&application_name=projeto-api-devops"
            )
        else:
            # Container Apps interno ou desenvolvimento sem SSL
            # Não adiciona sslmode=require
            SQLALCHEMY_DATABASE_URI = (
                f"postgresql://{db_user}:{db_password_encoded}@{db_server}:{db_port}/{db_name}"
                f"?connect_timeout=60&application_name=projeto-api-devops"
            )
            
    # CORS - Origens permitidas em produção
    # Deve ser configurado para o domínio do frontend (ex: https://meu-app.azurestaticapps.net)
    # Em desenvolvimento, permite localhost:3000
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://127.0.0.1:3000').split(',')
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