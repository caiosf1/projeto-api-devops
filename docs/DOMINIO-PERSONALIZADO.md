# 🌐 GUIA COMPLETO - DOMÍNIO PERSONALIZADO AZURE CONTAINER APPS

## 📋 PRÉ-REQUISITOS

1. **Domínio registrado** (exemplo: meuapp.com.br)
2. **Acesso ao DNS** do domínio (onde ele foi comprado)
3. **Azure CLI** configurado
4. **Container App** funcionando

---

## 🚀 PASSO A PASSO COMPLETO

### **ETAPA 1: Obter certificado gerenciado do Azure**

```bash
# 1. Adicionar domínio personalizado ao Container App
az containerapp hostname add \
  --name projeto-api-caio \
  --resource-group rg-projeto-api \
  --hostname api.seudominio.com.br

# 2. Obter informações para configurar DNS
az containerapp hostname list \
  --name projeto-api-caio \
  --resource-group rg-projeto-api
```

### **ETAPA 2: Configurar DNS do seu domínio**

No painel do seu provedor de DNS (GoDaddy, Registro.br, etc):

```dns
# Adicione estes registros DNS:

# CNAME para subdomínio
api.seudominio.com.br → projeto-api-caio.gentleisland-7ad00bd6.eastus.azurecontainerapps.io

# TXT para validação (Azure vai fornecer este valor)
asuid.api.seudominio.com.br → [VALOR_FORNECIDO_PELO_AZURE]
```

### **ETAPA 3: Gerar certificado SSL automático**

```bash
# Azure gera certificado SSL gratuito automaticamente
az containerapp hostname bind \
  --name projeto-api-caio \
  --resource-group rg-projeto-api \
  --hostname api.seudominio.com.br \
  --environment env-projeto-api
```

---

## 💡 OPÇÕES DE DOMÍNIO BARATO/GRATUITO

### **1. 🆓 Freenom (.tk, .ml, .ga)**
- **Custo:** Gratuito por 1 ano
- **Site:** freenom.com
- **Pros:** Grátis, funciona perfeitamente
- **Contras:** Extensões menos profissionais

### **2. 💰 Namecheap (.tech, .site, .online)**
- **Custo:** $2-5/ano
- **Site:** namecheap.com  
- **Pros:** Barato, extensões modernas
- **Exemplo:** meuapp.tech, api-projeto.site

### **3. 🇧🇷 Registro.br (.com.br, .net.br)**
- **Custo:** R$ 40/ano
- **Site:** registro.br
- **Pros:** Domínio brasileiro profissional
- **Exemplo:** meuapp.com.br

---

## 🤖 AUTOMATIZAÇÃO NO CI/CD

Vou adicionar ao workflow para configurar domínio automaticamente:

```yaml
# Adicionar no job de deploy
- name: 'Configure Custom Domain'
  run: |
    if [ "${{ secrets.CUSTOM_DOMAIN }}" != "" ]; then
      echo "🌐 Configurando domínio personalizado: ${{ secrets.CUSTOM_DOMAIN }}"
      
      # Adiciona hostname se não existir
      az containerapp hostname add \
        --name ${{ env.AZURE_CONTAINER_APP }} \
        --resource-group ${{ env.AZURE_RESOURCE_GROUP }} \
        --hostname ${{ secrets.CUSTOM_DOMAIN }} || echo "Hostname já existe"
        
      # Bind certificado SSL
      az containerapp hostname bind \
        --name ${{ env.AZURE_CONTAINER_APP }} \
        --resource-group ${{ env.AZURE_RESOURCE_GROUP }} \
        --hostname ${{ secrets.CUSTOM_DOMAIN }} \
        --environment ${{ env.AZURE_CONTAINER_ENV }} || echo "SSL já configurado"
        
      echo "✅ Domínio configurado: https://${{ secrets.CUSTOM_DOMAIN }}"
    else
      echo "⚠️  CUSTOM_DOMAIN secret não configurado"
    fi
```

---

## 🎯 RECOMENDAÇÃO PARA PORTFÓLIO

Para **vagas de estágio/júnior**, recomendo:

### **OPÇÃO 1: .tech ou .site ($3/ano)**
```
api-projeto.tech
meuapp.site  
portfolio-api.online
```

### **OPÇÃO 2: Subdomínio gratuito**
```
Use serviços como:
- Netlify (subdominio.netlify.app)  
- Vercel (subdominio.vercel.app)
- GitHub Pages (usuario.github.io)
```

### **OPÇÃO 3: Domínio brasileiro profissional**
```
meuapp.com.br (R$ 40/ano)
```

---

## ⚡ CONFIGURAÇÃO RÁPIDA - 5 MINUTOS

Se você tem um domínio, posso configurar agora:

1. **Me diga seu domínio** (ex: meuapp.com.br)
2. **Eu configuro o Azure** 
3. **Você configura o DNS** (2 registros)
4. **Certificado SSL** automático em ~15 minutos

Quer que eu configure agora? 🚀