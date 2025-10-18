# ===================================================================================
# Testes da API de Tarefas
# ===================================================================================
import pytest


# ===================================================================================
# Testes de Autenticação
# ===================================================================================

def test_registro_usuario_com_sucesso(client):
    """Testa se é possível registrar um novo usuário."""
    response = client.post('/auth/register', json={
        "email": "novo@email.com",
        "senha": "senha123"
    })
    assert response.status_code == 201
    assert response.get_json()['mensagem'] == 'Usuário criado com sucesso!'


def test_registro_usuario_duplicado_deve_retornar_409(client):
    """Testa se o sistema impede registro de email duplicado."""
    # Primeiro registro
    client.post('/auth/register', json={
        "email": "duplicado@email.com",
        "senha": "senha123"
    })
    # Segundo registro com mesmo email
    response = client.post('/auth/register', json={
        "email": "duplicado@email.com",
        "senha": "outrasenha"
    })
    assert response.status_code == 409
    assert 'já está em uso' in response.get_json()['erro']


def test_login_com_credenciais_validas(client):
    """Testa login com credenciais corretas."""
    # Registra usuário
    client.post('/auth/register', json={
        "email": "login@email.com",
        "senha": "senha123"
    })
    # Tenta fazer login
    response = client.post('/auth/login', json={
        "email": "login@email.com",
        "senha": "senha123"
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()


def test_login_com_credenciais_invalidas_deve_retornar_401(client):
    """Testa se login com senha errada é rejeitado."""
    # Registra usuário
    client.post('/auth/register', json={
        "email": "teste@email.com",
        "senha": "senhaCorreta"
    })
    # Tenta login com senha errada
    response = client.post('/auth/login', json={
        "email": "teste@email.com",
        "senha": "senhaErrada"
    })
    assert response.status_code == 401
    assert 'Credenciais inválidas' in response.get_json()['erro']


# ===================================================================================
# Testes de Autorização
# ===================================================================================

def test_listar_tarefas_sem_token_deve_retornar_401(client):
    """Testa se a rota de tarefas retorna 401 (Não Autorizado) sem um token de autenticação."""
    response = client.get('/tarefas')
    assert response.status_code == 401


def test_criar_tarefa_sem_token_deve_retornar_401(client):
    """Testa se não é possível criar tarefa sem autenticação."""
    response = client.post('/tarefas', json={
        "descricao": "Tarefa sem auth",
        "prioridade": "baixa"
    })
    assert response.status_code == 401


# ===================================================================================
# Testes de CRUD de Tarefas
# ===================================================================================

def test_listar_tarefas_com_token_deve_retornar_200(client):
    """Testa o fluxo completo: registrar, logar e acessar uma rota protegida."""
    # Registra e faz login
    client.post('/auth/register', json={
        "email": "testefeliz@email.com",
        "senha": "senha123"
    })
    response_login = client.post('/auth/login', json={
        "email": "testefeliz@email.com",
        "senha": "senha123"
    })
    assert response_login.status_code == 200
    token = response_login.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # Acessa rota protegida
    response_tarefas = client.get('/tarefas', headers=headers)
    assert response_tarefas.status_code == 200


def test_criar_tarefa_com_dados_validos(client):
    """Testa criação de tarefa com dados corretos."""
    # Registra e faz login
    client.post('/auth/register', json={
        "email": "criar@email.com",
        "senha": "senha123"
    })
    response_login = client.post('/auth/login', json={
        "email": "criar@email.com",
        "senha": "senha123"
    })
    token = response_login.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # Cria tarefa
    response = client.post('/tarefas', headers=headers, json={
        "descricao": "Estudar Flask",
        "prioridade": "alta"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['descricao'] == "Estudar Flask"
    assert data['prioridade'] == "alta"
    assert data['concluida'] == False


def test_criar_tarefa_com_descricao_curta_deve_retornar_400(client):
    """Testa se validação impede descrição muito curta."""
    # Registra e faz login
    client.post('/auth/register', json={
        "email": "val@email.com",
        "senha": "senha123"
    })
    response_login = client.post('/auth/login', json={
        "email": "val@email.com",
        "senha": "senha123"
    })
    token = response_login.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # Tenta criar tarefa com descrição de 2 caracteres (mínimo é 3)
    response = client.post('/tarefas', headers=headers, json={
        "descricao": "ab",
        "prioridade": "baixa"
    })
    assert response.status_code == 400


def test_usuario_so_ve_suas_proprias_tarefas(client):
    """Testa se cada usuário vê apenas suas próprias tarefas."""
    # Usuário 1
    client.post('/auth/register', json={"email": "user1@email.com", "senha": "senha123"})
    login1 = client.post('/auth/login', json={"email": "user1@email.com", "senha": "senha123"})
    token1 = login1.get_json()['access_token']
    headers1 = {'Authorization': f'Bearer {token1}'}

    # Usuário 2
    client.post('/auth/register', json={"email": "user2@email.com", "senha": "senha123"})
    login2 = client.post('/auth/login', json={"email": "user2@email.com", "senha": "senha123"})
    token2 = login2.get_json()['access_token']
    headers2 = {'Authorization': f'Bearer {token2}'}

    # Usuário 1 cria 2 tarefas
    client.post('/tarefas', headers=headers1, json={"descricao": "Tarefa do User 1 - A", "prioridade": "baixa"})
    client.post('/tarefas', headers=headers1, json={"descricao": "Tarefa do User 1 - B", "prioridade": "media"})

    # Usuário 2 cria 1 tarefa
    client.post('/tarefas', headers=headers2, json={"descricao": "Tarefa do User 2", "prioridade": "alta"})

    # Verifica se cada usuário vê apenas suas tarefas
    tarefas_user1 = client.get('/tarefas', headers=headers1).get_json()
    tarefas_user2 = client.get('/tarefas', headers=headers2).get_json()

    assert len(tarefas_user1) == 2
    assert len(tarefas_user2) == 1
    assert all('User 1' in t['descricao'] for t in tarefas_user1)
    assert 'User 2' in tarefas_user2[0]['descricao']


def test_atualizar_tarefa(client):
    """Testa atualização de uma tarefa existente."""
    # Setup: criar usuário e tarefa
    client.post('/auth/register', json={"email": "update@email.com", "senha": "senha123"})
    login = client.post('/auth/login', json={"email": "update@email.com", "senha": "senha123"})
    token = login.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # Cria tarefa
    create_response = client.post('/tarefas', headers=headers, json={
        "descricao": "Tarefa original",
        "prioridade": "baixa"
    })
    tarefa_id = create_response.get_json()['id']

    # Atualiza a tarefa
    update_response = client.put(f'/tarefas/{tarefa_id}', headers=headers, json={
        "descricao": "Tarefa atualizada",
        "prioridade": "alta",
        "concluida": True
    })

    assert update_response.status_code == 200
    data = update_response.get_json()
    assert data['descricao'] == "Tarefa atualizada"
    assert data['prioridade'] == "alta"
    assert data['concluida'] == True


def test_deletar_tarefa(client):
    """Testa deleção de uma tarefa."""
    # Setup: criar usuário e tarefa
    client.post('/auth/register', json={"email": "delete@email.com", "senha": "senha123"})
    login = client.post('/auth/login', json={"email": "delete@email.com", "senha": "senha123"})
    token = login.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # Cria tarefa
    create_response = client.post('/tarefas', headers=headers, json={
        "descricao": "Tarefa para deletar",
        "prioridade": "baixa"
    })
    tarefa_id = create_response.get_json()['id']

    # Deleta a tarefa
    delete_response = client.delete(f'/tarefas/{tarefa_id}', headers=headers)
    assert delete_response.status_code == 204

    # Verifica que a tarefa não existe mais
    get_response = client.get(f'/tarefas/{tarefa_id}', headers=headers)
    assert get_response.status_code == 404