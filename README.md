# API de Gerenciamento de Tarefas

Uma API completa para gerenciamento de tarefas, construída com Flask, Flask-RESTx e SQLAlchemy.

## Visão Geral

Esta API oferece um sistema robusto para criar, listar, atualizar e deletar tarefas. Inclui também um sistema de autenticação de usuários baseado em JWT para proteger os endpoints.

## Tecnologias Utilizadas

- **Flask**: Um microframework web para Python.
- **Flask-RESTx**: Uma extensão do Flask para a criação de APIs RESTful, com geração automática de documentação Swagger.
- **Flask-SQLAlchemy**: Integração do SQLAlchemy com o Flask para facilitar o trabalho com o banco de dados.
- **Flask-Migrate**: Ferramenta para gerenciar migrações de banco de dados com Alembic.
- **Flask-Bcrypt**: Utilizado para o hashing de senhas.
- **Flask-JWT-Extended**: Para a implementação de autenticação com JSON Web Tokens (JWT).
- **Pydantic**: Para a validação de dados.
- **Docker**: Para a conteinerização da aplicação.
- **PostgreSQL**: Banco de dados relacional.

## Configuração do Projeto

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.

### Passos para a Instalação

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Crie um arquivo `.env`:**

   Baseado no arquivo `.env.example` (se houver), crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

   ```env
   DATABASE_URL=postgresql://user:password@db:5432/db_name
   JWT_SECRET_KEY=sua_chave_secreta_aqui
   ```

3. **Suba os contêineres com Docker Compose:**

   ```bash
   docker-compose up --build -d
   ```

4. **Execute as migrações do banco de dados:**

   ```bash
   docker-compose exec web flask db upgrade
   ```

## Endpoints da API

A documentação completa da API está disponível via Swagger UI na rota `/`.

### Autenticação

- `POST /auth/register`: Registra um novo usuário.
  - **Corpo da Requisição**: `{ "email": "user@example.com", "senha": "password" }`
- `POST /auth/login`: Autentica um usuário e retorna um token JWT.
  - **Corpo da Requisição**: `{ "email": "user@example.com", "senha": "password" }`

### Tarefas (Requer Autenticação)

- `GET /tarefas/`: Lista todas as tarefas.
- `POST /tarefas/`: Cria uma nova tarefa.
  - **Corpo da Requisição**: `{ "descricao": "Minha nova tarefa", "prioridade": "alta" }`
- `GET /tarefas/<int:id>`: Busca uma tarefa pelo seu ID.
- `PUT /tarefas/<int:id>`: Atualiza o status de uma tarefa para "concluída".
- `DELETE /tarefas/<int:id>`: Deleta uma tarefa.

## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona nova feature'`).
4. Envie para a branch original (`git push origin feature/nova-feature`).
5. Abra um Pull Request.
