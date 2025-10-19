# ===================================================================================
# 📦 IMPORTAÇÕES E EXPLICAÇÕES
# ===================================================================================

# FLASK - Framework web minimalista para Python
# Documentação: https://flask.palletsprojects.com/
from flask import Flask, jsonify, request

# Flask → Classe principal para criar aplicação web
# jsonify → Converte dicionário Python em JSON (formato para APIs)
# request → Objeto global com dados da requisição HTTP (body, headers, etc)

# SQLALCHEMY - ORM (Object-Relational Mapping)
# Traduz classes Python em tabelas SQL
# Exemplo: Usuario() vira linha na tabela "usuario"
from flask_sqlalchemy import SQLAlchemy

# MIGRATE - Gerencia mudanças no banco de dados
# Cria arquivos de "migração" quando você muda models
# Ex: adiciona coluna "prioridade" → cria migration → aplica no banco
from flask_migrate import Migrate

# PYDANTIC - Validação de dados
# Valida JSON enviado pelo usuário
# Ex: descricao mínimo 3 caracteres, prioridade enum [baixa, media, alta]
from pydantic import ValidationError

# BCRYPT - Criptografia de senhas
# NUNCA salve senha em texto plano!
# bcrypt.hash("senha123") → "$2b$12$NaXz..." (hash seguro)
from flask_bcrypt import Bcrypt

# JWT - JSON Web Tokens (autenticação stateless)
# Após login, retorna token: "eyJhbGci..." 
# Cliente envia token no header: Authorization: Bearer eyJhbGci...
# Servidor valida token e identifica usuário
from flask_jwt_extended import (
    JWTManager,           # Gerenciador JWT
    create_access_token,  # Cria token após login
    jwt_required,         # Decorator: rota precisa de token
    get_jwt_identity      # Extrai email do token
)

# FLASK-RESTX - Documentação Swagger automática
# Cria interface /docs com todos endpoints
# Resource → Classe que representa endpoint REST
# fields → Define tipos de dados (string, int, bool)
from flask_restx import Api, Resource, fields

# CORS - Cross-Origin Resource Sharing
# Permite frontend (localhost:8000) acessar backend (localhost:5000)
# Sem CORS → navegador bloqueia requisição (política same-origin)
from flask_cors import CORS

# SCHEMAS - Nossos schemas Pydantic customizados
# Importa validações que criamos em schemas.py
from schemas import TarefaCreateSchema, TarefaUpdateSchema

# ===================================================================================
# 🌍 INSTÂNCIAS GLOBAIS (Padrão Application Factory)
# ===================================================================================

# Por que criar aqui e não dentro de create_app()?
# Resposta: Para poder importar em outros arquivos (ex: models.py, tests/)
# As extensões são inicializadas depois com .init_app(app)

db = SQLAlchemy()        # ORM - comunica com banco de dados
bcrypt = Bcrypt()        # Hashing de senhas
jwt = JWTManager()       # Gerenciamento de tokens JWT
migrate = Migrate()      # Migrações do banco


# ===================================================================================
# 🗄️ MODELOS DO BANCO DE DADOS (ORM)
# ===================================================================================

# O QUE É ORM?
# Object-Relational Mapping = mapeia classes Python → tabelas SQL
# Benefícios:
# - Escreve Python em vez de SQL
# - Banco portável (muda PostgreSQL → SQLite mudando só config)
# - Migrações automáticas
# - Type safety


class Usuario(db.Model):
    """
    Modelo de Usuário - representa tabela 'usuario' no banco.
    
    Relacionamento: 1 usuário → N tarefas (one-to-many)
    Cascade: ao deletar usuário, deleta suas tarefas automaticamente
    """
    
    # PRIMARY KEY - identificador único, auto-incremento
    # Ex: primeiro usuário id=1, segundo id=2, etc
    id = db.Column(db.Integer, primary_key=True)
    
    # EMAIL - único (não permite duplicados), obrigatório
    # String(120) = VARCHAR(120) em SQL
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # SENHA - hash bcrypt (200 chars), obrigatório
    # NUNCA armazene senha em texto plano!
    # Exemplo hash: "$2b$12$NaXz8Gh5..." (60 chars, mas deixamos 200 para segurança)
    senha = db.Column(db.String(200), nullable=False)
    
    # RELACIONAMENTO - Permite acessar usuario.tarefas
    # backref='usuario' - Permite acessar tarefa.usuario
    # lazy=True - Carrega tarefas só quando acessar usuario.tarefas (não automaticamente)
    # cascade='all, delete-orphan' - Ao deletar usuario, deleta suas tarefas
    tarefas = db.relationship(
        'Tarefa',                   # Modelo relacionado
        backref='usuario',          # Tarefa.usuario acessa o usuário dono
        lazy=True,                  # Lazy loading (performance)
        cascade='all, delete-orphan'  # Deleção em cascata
    )


class Tarefa(db.Model):
    """
    Modelo de Tarefa - representa tabela 'tarefa' no banco.
    
    Relacionamento: N tarefas → 1 usuário (many-to-one)
    Cada tarefa DEVE ter um dono (user_id obrigatório)
    """
    
    # PRIMARY KEY
    id = db.Column(db.Integer, primary_key=True)
    
    # DESCRIÇÃO - texto da tarefa, obrigatório
    # Ex: "Estudar algoritmos de ordenação"
    descricao = db.Column(db.String(200), nullable=False)
    
    # CONCLUÍDA - Boolean, padrão False
    # Permite marcar tarefa como feita
    concluida = db.Column(db.Boolean, default=False)
    
    # PRIORIDADE - enum-like (baixa, media, alta)
    # Default = 'baixa' (se não informar, assume baixa)
    prioridade = db.Column(db.String(50), nullable=False, default='baixa')
    
    # FOREIGN KEY - Chave estrangeira para tabela Usuario
    # db.ForeignKey('usuario.id') = referencia coluna "id" da tabela "usuario"
    # nullable=False = toda tarefa DEVE ter um dono
    # Isso cria relacionamento N:1 (muitas tarefas → 1 usuário)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)



# ===================================================================================
# 🏭 APPLICATION FACTORY (Padrão de Projeto)
# ===================================================================================

def create_app(config_class='config.DevelopmentConfig'):
    """
    Factory Function - Cria e configura instância da aplicação Flask.
    
    POR QUE USAR FACTORY AO INVÉS DE app = Flask(__name__) NO TOPO?
    
    ✅ Vantagens do Factory Pattern:
    1. Múltiplos ambientes: Development, Testing, Production
    2. Testes isolados: cada teste cria app própria
    3. Evita circular imports (models importa db, app importa models)
    4. Facilita CI/CD: muda config via variável de ambiente
    
    Analogia: Fábrica de carros
    - create_app('SportConfig') → Carro esportivo
    - create_app('TruckConfig') → Caminhão
    - Mesma fábrica, produtos diferentes
    
    Args:
        config_class (str): Classe de configuração a usar
            - 'config.DevelopmentConfig': SQLite, Debug ON
            - 'config.ProductionConfig': PostgreSQL, Debug OFF
            - 'config.TestingConfig': SQLite in-memory, Testing ON
    
    Returns:
        Flask: Aplicação configurada e pronta para rodar
    """
    
    # ==================
    # 1. CRIAR APP
    # ==================
    app = Flask(__name__)  # __name__ = nome do módulo (usado para localizar templates/static)
    
    # ==================
    # 2. CARREGAR CONFIGURAÇÃO
    # ==================
    # config.from_object() carrega variáveis da classe de config
    # Ex: DevelopmentConfig tem SQLALCHEMY_DATABASE_URI = "sqlite:///..."
    app.config.from_object(config_class)

    # ==================
    # 3. INICIALIZAR EXTENSÕES
    # ==================
    # Por que .init_app() e não passar app no construtor?
    # Resposta: Permite usar mesma instância (db, bcrypt) em múltiplas apps
    # Útil para testes (cada teste cria app separada)
    
    db.init_app(app)          # ORM - conecta ao banco configurado
    bcrypt.init_app(app)      # Hashing - usa SECRET_KEY do config
    jwt.init_app(app)         # JWT - usa JWT_SECRET_KEY do config
    migrate.init_app(app, db) # Migrations - conecta Flask-Migrate ao banco
    
    # ==================
    # 4. CORS - CRUCIAL PARA FRONTEND
    # ==================
    # Por que CORS é necessário?
    # Problema: Navegadores bloqueiam requisições cross-origin (segurança)
    # Cenário: frontend em localhost:8000 quer acessar API em localhost:5000
    # Sem CORS: Navegador bloqueia → erro "CORS policy"
    # Com CORS: Servidor diz "pode acessar" → requisição passa
    #
    # Headers que CORS adiciona:
    # Access-Control-Allow-Origin: *  (permite qualquer origem)
    # Access-Control-Allow-Methods: GET, POST, PUT, DELETE
    # Access-Control-Allow-Headers: Content-Type, Authorization
    CORS(app)

    # ==================
    # 5. CONFIGURAR SWAGGER (Flask-RESTX)
    # ==================
    
    # Authorizations - Define esquema de autenticação JWT para Swagger UI
    # Permite testar endpoints protegidos diretamente no /docs
    authorizations = {
        'jwt': {
            'type': 'apiKey',           # Tipo: chave de API
            'in': 'header',             # Enviado no header HTTP
            'name': 'Authorization',    # Nome do header
            'description': "Digite 'Bearer ' antes do seu token. Ex: 'Bearer ey...'"
        }
    }

    # API principal - Configuração do Swagger
    api = Api(
        app,
        version='1.0',                  # Versão da API
        title='API de Tarefas',         # Título no Swagger
        description='Uma API completa para gerenciamento de tarefas com ciclo DevOps.',
        authorizations=authorizations,  # Passa config JWT
        doc='/docs'                     # URL da documentação: http://localhost:5000/docs
    )

    # ===================================================================================
    # Namespaces e Modelos de Dados para o Swagger
    # ===================================================================================
    ns_auth = api.namespace('auth', description='Operações de Autenticação')
    ns_tarefas = api.namespace(
        'tarefas', description='Operações relacionadas a tarefas',
        decorators=[jwt_required()]
    )

    modelo_registro = ns_auth.model('Registro', {
        'email': fields.String(required=True, description='Email para novo usuário'),
        'senha': fields.String(required=True, description='Senha para o novo usuário')
    })

    modelo_login = ns_auth.model('Login', {
        'email': fields.String(required=True, description='Email do usuário'),
        'senha': fields.String(required=True, description='Senha do usuário')
    })

    modelo_tarefa_output = ns_tarefas.model('TarefaOutput', {
        'id': fields.Integer(readOnly=True),
        'descricao': fields.String,
        'concluida': fields.Boolean,
        'prioridade': fields.String
    })

    modelo_tarefa_input = ns_tarefas.model('TarefaInput', {
        'descricao': fields.String(required=True, min_length=3),
        'prioridade': fields.String(default='baixa', enum=['baixa', 'media', 'alta'])
    })

    # ===================================================================================
    # Rotas da API
    # ===================================================================================
    @ns_auth.route('/register')
    class RegistroResource(Resource):
        @ns_auth.expect(modelo_registro)
        @ns_auth.response(201, 'Usuário criado com sucesso!')
        @ns_auth.response(409, 'Este email já está em uso')
        def post(self):
            """Registra um novo usuário."""
            dados = request.get_json()
            email = dados.get('email')
            senha = dados.get('senha')

            if Usuario.query.filter_by(email=email).first():
                return {'erro': 'Este email já está em uso'}, 409

            senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
            novo_usuario = Usuario(email=email, senha=senha_hash)
            db.session.add(novo_usuario)
            db.session.commit()
            return {'mensagem': 'Usuário criado com sucesso!'}, 201

    @ns_auth.route('/login')
    class LoginResource(Resource):
        @ns_auth.expect(modelo_login)
        def post(self):
            """Autentica um usuário e retorna um token JWT."""
            dados = request.get_json()
            email = dados.get('email')
            senha = dados.get('senha')
            usuario = Usuario.query.filter_by(email=email).first()

            if not usuario or not bcrypt.check_password_hash(usuario.senha, senha):
                return {'erro': 'Credenciais inválidas'}, 401

            access_token = create_access_token(identity=email)
            return {'access_token': access_token}

    # >>> corrigido: sem a barra final, rota será /tarefas (sem redirecionamento 308)
    @ns_tarefas.route('')
    @ns_tarefas.doc(security='jwt')
    class ListaDeTarefasResource(Resource):
        @ns_tarefas.marshal_list_with(modelo_tarefa_output)
        def get(self):
            """Lista todas as tarefas do usuário logado"""
            # Obtém o email do usuário a partir do token JWT
            email_usuario = get_jwt_identity()
            usuario = Usuario.query.filter_by(email=email_usuario).first()
            
            if not usuario:
                return {'erro': 'Usuário não encontrado'}, 404
            
            # Retorna apenas as tarefas do usuário logado
            return Tarefa.query.filter_by(user_id=usuario.id).all()

        @ns_tarefas.expect(modelo_tarefa_input)
        @ns_tarefas.marshal_with(modelo_tarefa_output, code=201)
        def post(self):
            """Cria uma nova tarefa para o usuário logado"""
            dados = api.payload
            try:
                tarefa_validada = TarefaCreateSchema(**dados)
            except ValidationError as e:
                return {"erros": e.errors()}, 400

            # Obtém o ID do usuário logado
            email_usuario = get_jwt_identity()
            usuario = Usuario.query.filter_by(email=email_usuario).first()
            
            if not usuario:
                return {'erro': 'Usuário não encontrado'}, 404

            # Cria a tarefa associada ao usuário
            nova_tarefa = Tarefa(**tarefa_validada.model_dump(), user_id=usuario.id)
            db.session.add(nova_tarefa)
            db.session.commit()
            return nova_tarefa, 201

    @ns_tarefas.route('/<int:id>')
    @ns_tarefas.doc(security='jwt', params={'id': 'O ID da Tarefa'})
    class TarefaResource(Resource):
        @ns_tarefas.marshal_with(modelo_tarefa_output)
        def get(self, id):
            """Busca uma tarefa pelo seu ID."""
            return Tarefa.query.get_or_404(id)

        @ns_tarefas.expect(modelo_tarefa_input)
        @ns_tarefas.marshal_with(modelo_tarefa_output)
        def put(self, id):
            """Atualiza uma tarefa existente."""
            tarefa = Tarefa.query.get_or_404(id)
            dados = api.payload
            try:
                dados_validados = TarefaUpdateSchema(**dados).model_dump(exclude_unset=True)
            except ValidationError as e:
                return {"erros": e.errors()}, 400

            for key, value in dados_validados.items():
                setattr(tarefa, key, value)

            db.session.commit()
            return tarefa

        @ns_tarefas.response(204, 'Tarefa deletada com sucesso')
        def delete(self, id):
            """Deleta uma tarefa."""
            tarefa = Tarefa.query.get_or_404(id)
            db.session.delete(tarefa)
            db.session.commit()
            return '', 204

    # 🗃️ INICIALIZAÇÃO DAS TABELAS NO BANCO
    # Cria automaticamente as tabelas quando app inicia
    # Essential para PostgreSQL em Container Apps!
    with app.app_context():
        try:
            print("🔄 Tentando conectar no banco de dados...")
            db.create_all()
            print("✅ Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao criar tabelas: {e}")
            print("⚠️  App vai iniciar mesmo assim - tabelas serão criadas na primeira requisição")
            # Não falha a aplicação, só loga o erro
    
    return app

# ===================================================================================
# 🌍 INSTANCIAR APP PARA USO DIRETO
# ===================================================================================
# Cria instância padrão da aplicação para uso fora do factory pattern
app = create_app()

@app.route('/health')
def health_check():
    """Endpoint de verificação de saúde da aplicação - não depende do banco"""
    return {'status': 'healthy', 'message': 'API está funcionando'}, 200

@app.route('/health/db')  
def health_check_db():
    """Endpoint de verificação de saúde com teste de banco"""
    try:
        # Testa conexão com banco
        with app.app_context():
            db.engine.execute('SELECT 1')
        return {'status': 'healthy', 'database': 'connected'}, 200
    except Exception as e:
        return {'status': 'unhealthy', 'database': 'disconnected', 'error': str(e)}, 503

@app.route('/')
def index():
    return {'message': 'API funcionando', 'docs': '/docs'}, 200

if __name__ == '__main__':
    app.run(debug=True)
