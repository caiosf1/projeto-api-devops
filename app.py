# ===================================================================================
# 1. Importações
# ===================================================================================
import time
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
from flask_migrate import Migrate
from schemas import TarefaCreateSchema
from pydantic import ValidationError
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_restx import Api, Resource, fields
import os

load_dotenv()

# ===================================================================================
# 2. Setup da Aplicação e Extensões
# ===================================================================================
authorizations = {
    'jwt': {
        'type': 'apiKey', 'in': 'header', 'name': 'Authorization',
        'description': "Digite 'Bearer ' antes do seu token. Ex: 'Bearer ey...'"
    }
}

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Tarefas',
          description='Uma API completa para gerenciamento de tarefas com ciclo DevOps.',
          authorizations=authorizations)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

db_uri = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ===================================================================================
# 3. Modelos do Banco de Dados (SQLAlchemy)
# ===================================================================================


class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    concluida = db.Column(db.Boolean, default=False)
    prioridade = db.Column(db.String(50), nullable=False, default='baixa')


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)


# ===================================================================================
# 4. Namespaces e Modelos de Dados para o Swagger (Flask-RESTx)
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
    'id': fields.Integer(readOnly=True), 'descricao': fields.String,
    'concluida': fields.Boolean, 'prioridade': fields.String
})

modelo_tarefa_input = ns_tarefas.model('TarefaInput', {
    'descricao': fields.String(required=True, min_length=3),
    'prioridade': fields.String(default='baixa', enum=['baixa', 'media', 'alta'])
})

# ===================================================================================
# 5. Rotas da API (no formato Resource)
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
        return {'mensagem': 'Usuario criado com sucesso!'}, 201


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


@ns_tarefas.route('/')
@ns_tarefas.doc(security='jwt')
class ListaDeTarefasResource(Resource):
    @ns_tarefas.marshal_list_with(modelo_tarefa_output)
    def get(self):
        """Lista todas as tarefas"""
        return Tarefa.query.all()

    @ns_tarefas.expect(modelo_tarefa_input)
    @ns_tarefas.marshal_with(modelo_tarefa_output, code=201)
    def post(self):
        """Cria uma nova tarefa"""
        dados = api.payload
        try:
            tarefa_validada = TarefaCreateSchema(**dados)
        except ValidationError as e:
            return {"erros": e.errors()}, 400

        nova_tarefa = Tarefa(descricao=tarefa_validada.descricao,
                             prioridade=tarefa_validada.prioridade)
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

    @ns_tarefas.marshal_with(modelo_tarefa_output)
    def put(self, id):
        """Atualiza o status de uma tarefa para 'concluída'."""
        tarefa = Tarefa.query.get_or_404(id)
        tarefa.concluida = True
        db.session.commit()
        return tarefa

    @ns_tarefas.response(204, 'Tarefa deletada com sucesso')
    def delete(self, id):
        """Deleta uma tarefa."""
        tarefa = Tarefa.query.get_or_404(id)
        db.session.delete(tarefa)
        db.session.commit()
        return '', 204


# ===================================================================================
# 6. Inicialização do Servidor
# ===================================================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
