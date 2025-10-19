FROM python:3.9-slim

WORKDIR /app

# 1. Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 2. Copia a lista de dependências e instala
COPY requirements.txt .
RUN pip install -r requirements.txt psycopg2-binary

# 3. Copia o script de espera pelo PostgreSQL
COPY wait-for-postgres.py .

# 4. Copia a pasta de migrações
COPY migrations/ ./migrations/

# 5. Copia o resto do código da aplicação
COPY . .

# 6. Definir variáveis de ambiente padrão
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# 7. Script de entrada que aguarda PostgreSQL e depois inicia a app
# Se wait-for-postgres falhar, ainda assim inicia a app (modo degradado)
CMD ["sh", "-c", "python3 wait-for-postgres.py || echo '⚠️ Iniciando em modo degradado' && python3 run.py"]