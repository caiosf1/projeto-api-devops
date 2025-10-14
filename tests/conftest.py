import os
import pytest

# Define a URL do banco de teste ANTES de importar o app
os.environ['DATABASE_URL'] = "postgresql://caio:minhasenha@localhost:5432/apitodo_test"

from app import app as flask_app, db

def app():
    """Cria a aplicação Flask para a sessão de testes."""
    flask_app.config.update({"TESTING": True})
    with flask_app.app_context():
        db.drop_all()
        db.create_all()
    yield flask_app
    with flask_app.app_context():
        db.drop_all()

def client(app):
    """Fornece um cliente de teste para cada função."""
    with app.test_client() as client:
        yield client