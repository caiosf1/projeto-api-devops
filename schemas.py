# ===================================================================================
# 🛡️ SCHEMAS DE VALIDAÇÃO - PYDANTIC V2
# ===================================================================================
# Este arquivo define REGRAS DE NEGÓCIO para validação de dados da API.
#
# O QUE É PYDANTIC?
# -----------------
# Biblioteca Python para validação de dados usando type hints.
# Transforma classes Python em validadores automáticos.
#
# POR QUE USAR VALIDAÇÃO?
# -----------------------
# ❌ SEM VALIDAÇÃO:
#    Cliente envia: {"descricao": ""}  → cria tarefa vazia (bug!)
#    Cliente envia: {"prioridade": "urgente"}  → valor inválido
#    Cliente envia dados maliciosos → SQL injection, XSS
#
# ✅ COM VALIDAÇÃO:
#    Pydantic rejeita ANTES de tocar no banco
#    Retorna erro 400 com mensagem clara
#    Protege contra ataques de injeção
#
# PADRÃO:
# -------
# 1. Cliente envia JSON
# 2. Flask recebe em request.get_json()
# 3. Pydantic valida: TarefaCreateSchema(**dados)
# 4. Se inválido: levanta ValidationError → retorna 400
# 5. Se válido: continua para banco de dados

# ===================================================================================
# 📦 IMPORTAÇÕES
# ===================================================================================

# BaseModel: Classe base do Pydantic que transforma classes em validadores
# Toda classe que herda BaseModel ganha validação automática
from pydantic import BaseModel, constr

# Optional: Indica que campo pode ser None (usado em updates parciais)
# Ex: Optional[str] aceita string ou None
from typing import Optional

# Enum: Cria conjunto de constantes (enumeração)
# Usado para campos com valores limitados (ex: prioridade)
from enum import Enum


# ===================================================================================
# 📋 ENUM DE PRIORIDADE - VALORES PERMITIDOS
# ===================================================================================
class PrioridadeEnum(str, Enum):
    """
    Enumeração de prioridades permitidas para tarefas.
    
    POR QUE ENUM?
    -------------
    ❌ Sem Enum: {"prioridade": "urgentissimooo"}  → aceita qualquer string
    ✅ Com Enum: Pydantic aceita APENAS 'baixa', 'media' ou 'alta'
    
    POR QUE HERDAR str E Enum?
    --------------------------
    - Herda de Enum → comportamento de enumeração
    - Herda de str → valores se comportam como strings em JSON
    - Serialização automática: PrioridadeEnum.alta → "alta" (não precisa converter)
    
    USO:
    ----
    >>> prioridade = PrioridadeEnum.alta
    >>> print(prioridade)
    'alta'
    >>> print(prioridade == 'alta')
    True
    >>> PrioridadeEnum('media')  # Cria a partir de string
    <PrioridadeEnum.media: 'media'>
    
    VALIDAÇÃO AUTOMÁTICA:
    ---------------------
    >>> TarefaCreateSchema(descricao="Teste", prioridade="super_alta")
    ValidationError: prioridade
      Input should be 'baixa', 'media' or 'alta'
    """
    
    baixa = 'baixa'   # Tarefa pode esperar (ex: organizar favoritos)
    media = 'media'   # Importante mas não urgente (ex: estudar React)
    alta = 'alta'     # Urgente e importante (ex: bug em produção)


# ===================================================================================
# ➕ SCHEMA DE CRIAÇÃO - POST /tarefas
# ===================================================================================
class TarefaCreateSchema(BaseModel):
    """
    Schema para criar nova tarefa (POST /tarefas).
    
    VALIDAÇÕES APLICADAS:
    ---------------------
    - descricao: Mínimo 3 caracteres
    - prioridade: Enum (baixa, media, alta) com padrão 'baixa'
    
    EXEMPLO DE USO NA API:
    ----------------------
    # No endpoint:
    dados = request.get_json()  # {"descricao": "Estudar Python", "prioridade": "alta"}
    
    try:
        tarefa_validada = TarefaCreateSchema(**dados)  # Valida
        # Se chegou aqui, dados são válidos!
        nova_tarefa = Tarefa(**tarefa_validada.model_dump())
        db.session.add(nova_tarefa)
        db.session.commit()
    except ValidationError as e:
        return {"erros": e.errors()}, 400  # Retorna erros de validação
    
    EXEMPLOS DE VALIDAÇÃO:
    ----------------------
    ✅ VÁLIDO:
    {"descricao": "Estudar Flask", "prioridade": "alta"}
    {"descricao": "Ler documentação"}  → usa prioridade padrão 'baixa'
    
    ❌ INVÁLIDO:
    {"descricao": "ab"}  → Erro: mínimo 3 caracteres
    {"descricao": ""}  → Erro: campo obrigatório
    {"prioridade": "urgente"}  → Erro: deve ser baixa/media/alta
    {}  → Erro: descricao é obrigatório
    
    DIFERENÇA PYDANTIC V1 → V2:
    ---------------------------
    V1: constr(min_length=3)
    V2: constr(min_length=3)  (mesmo, mas .dict() → .model_dump())
    """
    
    # constr = constrained string (string com restrições)
    # min_length=3 → Pydantic rejeita strings com menos de 3 caracteres
    # Ex: "ab" → erro, "abc" → OK
    descricao: constr(min_length=3)
    
    # PrioridadeEnum garante que apenas baixa/media/alta são aceitos
    # = PrioridadeEnum.baixa define valor padrão se cliente não enviar
    # Cliente pode omitir prioridade: {"descricao": "Tarefa"} → prioridade='baixa'
    prioridade: PrioridadeEnum = PrioridadeEnum.baixa


# ===================================================================================
# ✏️ SCHEMA DE ATUALIZAÇÃO - PUT/PATCH /tarefas/<id>
# ===================================================================================
class TarefaUpdateSchema(BaseModel):
    """
    Schema para atualizar tarefa existente (PUT/PATCH /tarefas/<id>).
    
    POR QUE TODOS OS CAMPOS SÃO OPTIONAL?
    --------------------------------------
    Update parcial: cliente envia APENAS campos que quer mudar
    
    Exemplo: quero só marcar como concluída
    PUT /tarefas/5 {"concluida": true}  → atualiza só concluida
    
    Se fossem obrigatórios, teria que enviar tudo:
    PUT /tarefas/5 {"descricao": "...", "concluida": true, "prioridade": "..."}
    
    USO NA API:
    -----------
    dados = request.get_json()  # {"concluida": true}
    tarefa = Tarefa.query.get_or_404(id)
    
    try:
        # Valida dados
        dados_validados = TarefaUpdateSchema(**dados)
        
        # model_dump(exclude_unset=True) retorna APENAS campos enviados
        # exclude_unset=True → ignora campos com valor None (não enviados)
        atualizar = dados_validados.model_dump(exclude_unset=True)
        # atualizar = {"concluida": True}  (só o que mudou!)
        
        # Atualiza campos dinamicamente
        for key, value in atualizar.items():
            setattr(tarefa, key, value)  # tarefa.concluida = True
        
        db.session.commit()
    except ValidationError as e:
        return {"erros": e.errors()}, 400
    
    EXEMPLOS:
    ---------
    ✅ VÁLIDO (update parcial):
    {"concluida": true}  → marca como concluída
    {"prioridade": "alta"}  → só muda prioridade
    {"descricao": "Nova descrição", "concluida": false}  → muda 2 campos
    
    ✅ VÁLIDO (update completo):
    {"descricao": "Tarefa", "concluida": false, "prioridade": "media"}
    
    ❌ INVÁLIDO:
    {"descricao": "ab"}  → mínimo 3 caracteres
    {"prioridade": "super"}  → deve ser baixa/media/alta
    {"campo_inexistente": "valor"}  → Pydantic ignora campos extras
    
    DIFERENÇA CREATE vs UPDATE:
    ---------------------------
    CREATE (TarefaCreateSchema):
      - descricao: obrigatório
      - prioridade: opcional com padrão
      
    UPDATE (TarefaUpdateSchema):
      - descricao: opcional (mantém atual se não enviar)
      - concluida: opcional
      - prioridade: opcional
    """
    
    # Optional[tipo] = pode ser tipo ou None
    # = None define padrão como None (campo não enviado)
    
    # Descrição opcional, mas se enviar, mínimo 3 caracteres
    descricao: Optional[constr(min_length=3)] = None
    
    # Booleano opcional (True/False ou None)
    # Permite marcar/desmarcar conclusão
    concluida: Optional[bool] = None
    
    # Prioridade opcional, mas se enviar, valida Enum
    prioridade: Optional[PrioridadeEnum] = None


# ===================================================================================
# 📚 NOTAS ADICIONAIS
# ===================================================================================
"""
PYDANTIC V2 - PRINCIPAIS MUDANÇAS:
-----------------------------------
1. .dict() → .model_dump()
2. .json() → .model_dump_json()
3. Performance ~50x mais rápida (core em Rust)
4. Validação mais rigorosa (menos bugs)

ALTERNATIVAS AO PYDANTIC:
-------------------------
1. Marshmallow: mais antigo, mais verboso
2. Cerberus: focado em dicionários
3. Voluptuous: sintaxe diferente
4. attrs + cattrs: mais genérico

POR QUE PYDANTIC É MELHOR:
--------------------------
✅ Type hints nativos (IDE autocomplete)
✅ Performance (core em Rust)
✅ Usado por FastAPI (ecosistema)
✅ Validação + Serialização em um só
✅ Documentação automática

SEGURANÇA:
----------
Validação NÃO substitui sanitização!
- Validação: verifica se dados estão corretos
- Sanitização: remove/escapa caracteres perigosos

Pydantic valida TIPO e FORMATO.
SQLAlchemy parametriza queries (previne SQL injection).
Nunca use f-strings com input do usuário em queries!

PADRÃO DE PROJETO:
------------------
Schema = Contrato entre Cliente ↔ API
- Cliente sabe quais campos enviar
- API sabe o que esperar
- Documentação Swagger gerada automaticamente
- Testes podem usar schemas para gerar dados válidos

EVOLUÇÃO DOS SCHEMAS:
---------------------
1. Adicionar campo novo? Adicione como Optional
2. Campo antigo virou obrigatório? Migração gradual:
   - Fase 1: Optional com warning se None
   - Fase 2: Obrigatório (clientes já adaptados)
3. Renomear campo? Aceite ambos nomes temporariamente
"""
