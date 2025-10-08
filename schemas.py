from pydantic import BaseModel, constr


class TarefaCreateSchema(BaseModel):
    """
    Schema para a criação de uma nova tarefa.

    Utiliza Pydantic para validar os dados de entrada.

    Attributes:
        descricao (str): A descrição da tarefa. Deve ter no mínimo 3 caracteres.
        prioridade (str): A prioridade da tarefa. O valor padrão é 'baixa'.
    """
    # A descrição é um texto (str) e, usando constr,
    # Definimos que ela deve ter no mínimo 3 caracteres.
    descricao: constr(min_length=3)

    # A prioridade é um texto e é opcional.
    # Se não for enviada, o valor padrão será 'baixa'.
    prioridade: str = 'baixa'
