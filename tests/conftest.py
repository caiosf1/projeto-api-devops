import pytest
from app import create_app, db
from config import TestingConfig

@pytest.fixture(scope='module')
def app():
    """Cria e configura uma instância da aplicação Flask para os testes."""
    # Usa a factory para criar a app com a configuração de teste
    flask_app = create_app(TestingConfig)

    # Cria as tabelas do banco de dados antes de cada sessão de teste
    with flask_app.app_context():
        db.create_all()
        yield flask_app # Disponibiliza a app para os testes
        # Limpa o banco de dados depois de cada sessão de teste
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    """Cria um cliente de teste para fazer requisições à API."""
    return app.test_client()

@pytest.fixture(scope='function')
def init_database(app):
    """Limpa e recria o banco de dados para cada teste."""
    with app.app_context():
        db.drop_all()
        db.create_all()