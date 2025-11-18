# ===================================================================================
# 🚀 RUN.PY - ENTRYPOINT DA APLICAÇÃO
# ===================================================================================
# Este arquivo é o PONTO DE ENTRADA para iniciar o servidor Flask.
# Quando você roda 'python run.py', este código é executado.
#
# RESPONSABILIDADES:
# ------------------
# 1. Determinar ambiente (dev/test/prod)
# 2. Criar aplicação com create_app()
# 3. Inicializar banco de dados
# 4. Iniciar servidor web
#
# QUANDO USAR:
# ------------
# ✅ Desenvolvimento local: python run.py
# ✅ Debug no IDE: configura run.py como entrypoint
# ❌ Produção Azure: usa gunicorn app:app (não run.py)
#
# POR QUE NÃO RODAR app.py DIRETAMENTE?
# --------------------------------------
# app.py tem factory create_app() → retorna app
# run.py instancia app e roda servidor
# Separação de responsabilidades (boas práticas)

from app import create_app, db
import os

# ===================================================================================
# 🌍 DETERMINAR AMBIENTE (Development, Testing ou Production)
# ===================================================================================

# Lê variável de ambiente FLASK_ENV
# Valores possíveis:
# - 'development' → DevelopmentConfig (SQLite, Debug ON)
# - 'testing' → TestingConfig (SQLite in-memory, Testing ON)
# - 'production' → ProductionConfig (PostgreSQL, Debug OFF)
# - Qualquer outra coisa → DevelopmentConfig (padrão)
config_name = os.getenv('FLASK_ENV', 'config.DevelopmentConfig')

# Mapeia nome do ambiente para string da classe de config
# Isso é usado pelo create_app() para carregar configuração correta
if config_name == 'production':
    config_class = 'config.ProductionConfig'
elif config_name == 'testing':
    config_class = 'config.TestingConfig'
else:
    config_class = 'config.DevelopmentConfig'  # Padrão

print(f"🌍 Ambiente detectado: {config_class}")


# ===================================================================================
# 🏭 CRIAR APLICAÇÃO COM FACTORY PATTERN
# ===================================================================================

# create_app(config_class) retorna instância configurada do Flask
# Factory Pattern permite:
# - Múltiplas instâncias (cada teste cria sua app)
# - Configurações diferentes sem alterar código
# - Evita imports circulares
app = create_app(config_class)

print(f"✅ Aplicação criada: {app.name}")


# ===================================================================================
# 🎬 ENTRYPOINT - EXECUTA SE RODAR DIRETAMENTE
# ===================================================================================

# if __name__ == '__main__':
# Este bloco SÓ executa se você rodar: python run.py
# Não executa se importar: from run import app (usado em gunicorn)
if __name__ == '__main__':
    # ===================================================================================
    # 🗄️ INICIALIZAÇÃO DO BANCO DE DADOS
    # ===================================================================================
    
    # app.app_context() cria contexto necessário para operações do Flask
    # Dentro do contexto, extensões como db, jwt, bcrypt funcionam
    with app.app_context():
        # db.create_all() cria TODAS as tabelas definidas nos models
        # Se tabela já existe, não faz nada (idempotente)
        #
        # IMPORTANTE EM DESENVOLVIMENTO:
        # ✅ Primeira execução: cria tabelas usuario e tarefa
        # ✅ Execuções seguintes: ignora (tabelas já existem)
        #
        # IMPORTANTE EM PRODUÇÃO:
        # ⚠️  NÃO use db.create_all()! Use migrações:
        #    flask db migrate -m "mensagem"
        #    flask db upgrade
        # Migrações permitem:
        # - Adicionar colunas sem perder dados
        # - Histórico de mudanças (versionamento)
        # - Rollback se der problema
        # - Aplicar em produção sem downtime
        try:
            db.create_all()
            print("✅ Banco de dados inicializado!")
            print("📊 Tabelas disponíveis: usuario, tarefa")
        except Exception as e:
            print(f"⚠️  Erro ao inicializar banco: {e}")
            print("💡 Verifique configuração do banco em config.py")
        
        # ===================================================================================
        # 📝 INFORMAÇÕES ÚTEIS NO TERMINAL
        # ===================================================================================
        print("\n" + "="*70)
        print("🚀 SERVIDOR FLASK INICIADO COM SUCESSO!")
        print("="*70)
        print(f"📡 URL Local: http://0.0.0.0:5000")
        print(f"📡 URL Localhost: http://localhost:5000")
        print(f"📡 URL Rede: http://<seu-ip>:5000")
        print(f"📚 Documentação Swagger: http://localhost:5000/docs")
        print(f"🏥 Health Check: http://localhost:5000/health")
        print("="*70)
        print(f"⚙️  Ambiente: {config_class}")
        print(f"🐛 Debug Mode: {app.config.get('DEBUG', False)}")
        print(f"💾 Database: {app.config.get('SQLALCHEMY_DATABASE_URI', 'N/A')[:50]}...")
        print("="*70)
        print("💡 Dicas:")
        print("   - Ctrl+C para parar o servidor")
        print("   - Mudanças no código reiniciam automaticamente (debug=True)")
        print("   - Acesse /docs para testar API diretamente no navegador")
        print("="*70 + "\n")

    # ===================================================================================
    # 🌐 INICIAR SERVIDOR WEB
    # ===================================================================================
    
    # app.run() inicia servidor de desenvolvimento do Flask
    #
    # PARÂMETROS:
    # -----------
    # host='0.0.0.0' → Escuta em TODAS as interfaces de rede
    #   - 127.0.0.1 (localhost) → só acessa do próprio computador
    #   - 0.0.0.0 → acessa de qualquer IP (necessário para Docker)
    #   - Exemplo: pode acessar de outro PC na rede
    #
    # port=5000 → Porta TCP onde servidor escuta
    #   - Padrão Flask: 5000
    #   - Frontend geralmente usa: 3000, 8000, 8080
    #   - Produção HTTP: 80, HTTPS: 443
    #
    # debug=True → Modo debug (APENAS DESENVOLVIMENTO!)
    #   ✅ Hot reload: muda código → servidor reinicia
    #   ✅ Debugger interativo no navegador (em erros)
    #   ✅ Stacktrace detalhado (mostra linha do erro)
    #   ⚠️  NUNCA use em produção (expõe código fonte!)
    #
    # PRODUÇÃO USA GUNICORN AO INVÉS DE app.run():
    # --------------------------------------------
    # gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
    #   - Gunicorn é WSGI server (production-ready)
    #   - app.run() é só para desenvolvimento (single-threaded)
    #   - Workers paralelos = suporta múltiplas requisições
    app.run(
        host='0.0.0.0',  # Escuta em todas interfaces
        port=5000,       # Porta padrão Flask
        debug=True       # Debug ON (só dev!)
    )