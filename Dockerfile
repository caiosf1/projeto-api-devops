FROM python:3.9-slim

WORKDIR /app

# 1. Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 2. Copia a lista de dependências e instala
COPY requirements.txt .
RUN pip install -r requirements.txt psycopg2-binary

# 3. Copia a pasta de migrações
COPY migrations/ ./migrations/

# 4. Copia o resto do código da aplicação
COPY . .

# 5. Definir variáveis de ambiente padrão
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# 6. Inicia a aplicação
CMD ["python3", "run.py"]