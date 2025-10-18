FROM python:3.9-slim

WORKDIR /app

# 1. Copia a lista de dependências e instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# 2. Copia a pasta de migrações
COPY migrations/ ./migrations/

# 3. Copia o resto do código da aplicação
COPY . .

EXPOSE 5000
CMD ["python3", "run.py"]