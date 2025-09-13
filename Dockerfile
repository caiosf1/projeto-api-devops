#1. Começa com o kit base do Python
FROM python:3.9-slim
#2. Defina a workbench para /app
WORKDIR /app
# Primeiro, copie os requerimentos para a workbench
COPY requirements.txt .
# agora com a lista, instala tudo
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3","app.py"]