# Importa as ferramentas necessárias da biblioteca Pydantic e do módulo 'typing' e 'enum' do Python.
# BaseModel: Classe base do Pydantic que transforma classes Python normais em modelos de validação de dados.
# constr: Tipo de string que permite adicionar restrições, como comprimento mínimo/máximo.
# Optional: Indica que um campo pode ser do tipo especificado ou None (ou seja, é opcional).
# Enum: Permite criar um conjunto de constantes nomeadas (enumerações).
from pydantic import BaseModel, constr
from typing import Optional
from enum import Enum

# Cria uma enumeração para as prioridades permitidas.
# Herdar de 'str' e 'Enum' faz com que os membros do Enum se comportem como strings,
# o que é útil para validação e serialização em APIs JSON.
class PrioridadeEnum(str, Enum):
    baixa = 'baixa'
    media = 'media'
    alta = 'alta'

# Define o schema para a criação de uma nova tarefa.
# Herdar de BaseModel faz com que o Pydantic valide automaticamente os dados recebidos.
class TarefaCreateSchema(BaseModel):
    # Campo 'descricao':
    # - constr(min_length=3): Garante que a descrição tenha pelo menos 3 caracteres.
    # - O Pydantic levantará um erro de validação se essa condição não for atendida.
    descricao: constr(min_length=3)

    # Campo 'prioridade':
    # - Usa o PrioridadeEnum para garantir que apenas os valores 'baixa', 'media' ou 'alta' sejam aceitos.
    # - Define 'PrioridadeEnum.baixa' como o valor padrão se nenhum for fornecido.
    prioridade: PrioridadeEnum = PrioridadeEnum.baixa

# Define o schema para a atualização de uma tarefa existente.
# Todos os campos são opcionais, permitindo que o cliente da API envie apenas os campos que deseja alterar.
class TarefaUpdateSchema(BaseModel):
    # Optional[constr(min_length=3)]: O campo 'descricao' é opcional, mas se for fornecido,
    # deve ter pelo menos 3 caracteres.
    descricao: Optional[constr(min_length=3)] = None

    # Optional[bool]: O campo 'concluida' é opcional e deve ser um booleano se fornecido.
    concluida: Optional[bool] = None

    # Optional[PrioridadeEnum]: O campo 'prioridade' é opcional, mas se for fornecido,
    # deve ser um dos valores definidos em PrioridadeEnum.
    prioridade: Optional[PrioridadeEnum] = None
