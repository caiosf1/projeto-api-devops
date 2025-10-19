# 🚀 Recriação Rápida do Projeto

## Quando usar:
- Deletou os recursos para economizar
- Precisa recriar para demo/entrevista
- Quer mostrar o projeto funcionando

## Tempo total: ~10 minutos

---

## 1️⃣ Recriar PostgreSQL (~5 minutos)

```bash
# Criar banco
az postgres flexible-server create \
  --resource-group rg-projeto-api \
  --name postgres-api-caio \
  --location eastus \
  --admin-user pgadmin \
  --admin-password "MinhaSenh123" \
  --sku-name Standard_B1ms \
  --tier Burstable \
  --storage-size 32 \
  --version 14 \
  --yes

# Criar database
az postgres flexible-server db create \
  --resource-group rg-projeto-api \
  --server-name postgres-api-caio \
  --database-name apitodo

# Configurar firewall
az postgres flexible-server firewall-rule create \
  --resource-group rg-projeto-api \
  --name postgres-api-caio \
  --rule-name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0
```

---

## 2️⃣ Recriar Container Apps (~3 minutos)

```bash
# O Container Apps environment já existe, só precisa recriar o app

# Deploy já existente
az containerapp update \
  --name projeto-api-caio \
  --resource-group rg-projeto-api \
  --image caiosfdev/projeto-api-devops:latest \
  --set-env-vars \
    FLASK_ENV=production \
    SECRET_KEY="${SECRET_KEY}" \
    JWT_SECRET_KEY="${JWT_SECRET_KEY}" \
    POSTGRES_SERVER=postgres-api-caio.postgres.database.azure.com \
    POSTGRES_USER=pgadmin \
    POSTGRES_PASSWORD="MinhaSenh123" \
    POSTGRES_DB=apitodo \
    POSTGRES_PORT=5432 \
    POSTGRES_SSL_MODE=require

# OU se deletou tudo, criar do zero:
az containerapp create \
  --name projeto-api-caio \
  --resource-group rg-projeto-api \
  --environment env-projeto-api \
  --image caiosfdev/projeto-api-devops:latest \
  --target-port 5000 \
  --ingress external \
  --min-replicas 1 \
  --max-replicas 10 \
  --cpu 0.5 \
  --memory 1Gi \
  --env-vars \
    FLASK_ENV=production \
    SECRET_KEY="${SECRET_KEY}" \
    JWT_SECRET_KEY="${JWT_SECRET_KEY}" \
    POSTGRES_SERVER=postgres-api-caio.postgres.database.azure.com \
    POSTGRES_USER=pgadmin \
    POSTGRES_PASSWORD="MinhaSenh123" \
    POSTGRES_DB=apitodo \
    POSTGRES_PORT=5432 \
    POSTGRES_SSL_MODE=require
```

---

## 3️⃣ Verificar (~2 minutos)

```bash
# Testar API
curl https://api.caiodev.me/health
curl https://api.caiodev.me/health/db

# Testar frontend
curl https://app.caiodev.me
```

---

## 💾 Backup dos Dados (antes de deletar)

```bash
# Exportar dados do banco
pg_dump -h postgres-api-caio.postgres.database.azure.com \
  -U pgadmin \
  -d apitodo \
  -F c \
  -f backup_$(date +%Y%m%d).dump

# Restaurar depois:
pg_restore -h postgres-api-caio.postgres.database.azure.com \
  -U pgadmin \
  -d apitodo \
  backup_YYYYMMDD.dump
```

---

## 🗑️ Deletar Recursos (para economizar)

```bash
# Deletar Container App (mantém environment)
az containerapp delete \
  --name projeto-api-caio \
  --resource-group rg-projeto-api \
  --yes

# Deletar PostgreSQL
az postgres flexible-server delete \
  --resource-group rg-projeto-api \
  --name postgres-api-caio \
  --yes

# Economia: ~$20/mês → $0/mês
```

---

## 📊 Custos por Cenário

| Cenário | Custo/Mês | Quando Usar |
|---------|-----------|-------------|
| Tudo rodando | $20/mês | Uso contínuo |
| Tudo pausado | $1/mês | Usar às vezes |
| Tudo deletado | $0/mês | Raramente usar |
| Apenas frontend | $0/mês | Demo visual apenas |

---

## 🎯 Estratégia Student Pack

Com $100/ano = $8.33/mês:

1. **Mantenha deletado** ($0/mês)
2. **Recrie quando precisar** (~10 min)
3. **Use por 2-3 dias** (~$2-3)
4. **Delete novamente**

Resultado: Usa ~4-6x por ano, gasta $8-18 total (cabe no Student Pack!)
