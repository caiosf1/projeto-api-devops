import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações base."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'uma-chave-secreta-bem-segura')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'outra-chave-secreta-para-jwt')
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)

# Constrói a URI do banco de dados a partir das variáveis de ambiente
db_user = os.getenv('POSTGRES_USER', 'caio')
db_password = os.getenv('POSTGRES_PASSWORD', 'minhasenha')
db_name = os.getenv('POSTGRES_DB', 'apitodo')
db_host = 'db'  # Nome do serviço do postgres no docker-compose

# String de conexão completa
database_uri = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

class DevelopmentConfig(Config):
    """Configurações de desenvolvimento."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    DEBUG = True

class TestingConfig(Config):
    """Configurações de teste."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # Usa um banco de dados em memória para testes