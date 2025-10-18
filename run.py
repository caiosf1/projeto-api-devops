# ===================================================================================
# Entry Point da Aplicação
# ===================================================================================
# Este arquivo é o ponto de entrada para executar a aplicação Flask.
# Ele usa a função factory 'create_app()' para criar a instância da aplicação.

from app import create_app, db
import os

# Determina qual configuração usar baseado na variável de ambiente
# Padrão: DevelopmentConfig
config_name = os.getenv('FLASK_ENV', 'config.DevelopmentConfig')

if config_name == 'production':
    config_class = 'config.ProductionConfig'
elif config_name == 'testing':
    config_class = 'config.TestingConfig'
else:
    config_class = 'config.DevelopmentConfig'

# Cria a aplicação usando a factory function
app = create_app(config_class)

# Este bloco de código verifica se o script está sendo executado diretamente.
if __name__ == '__main__':
    # Cria um contexto de aplicação para operações que precisam do contexto do Flask
    with app.app_context():
        # Cria todas as tabelas no banco de dados se ainda não existirem
        # Em produção, use migrações (flask db upgrade) ao invés disso
        db.create_all()
        print("✅ Banco de dados inicializado!")
        print("🚀 Servidor rodando em http://0.0.0.0:5000")
        print("📚 Documentação Swagger disponível em http://0.0.0.0:5000/docs")

    # Inicia o servidor de desenvolvimento do Flask.
    # host='0.0.0.0' permite acesso de qualquer IP (necessário para Docker)
    # port=5000 é a porta padrão
    # debug=True habilita hot-reload e mensagens de erro detalhadas
    app.run(host='0.0.0.0', port=5000, debug=True)