def test_listar_tarefas_sem_token_deve_retornar_401(client):
    """Testa se a rota de tarefas retorna 401 sem um token de autenticação."""
    response = client.get('/tarefas')
    assert response.status_code == 401

def test_listar_tarefas_com_token_deve_retornar_200(client):
    """Testa o fluxo completo: registrar, logar e acessar uma rota protegida."""
    # Arrange
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

    # Act
    response_tarefas = client.get('/tarefas', headers=headers)

    # Assert
    assert response_tarefas.status_code == 200