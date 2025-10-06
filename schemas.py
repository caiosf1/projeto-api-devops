from pydantic import BaseModel, constr


class TarefaCreateSchema(BaseModel):
    # A descrição é um texto (str) e, usando constr,
    # Definimos que ela deve ter no mínimo 3 caracteres.
    descricao: constr(min_length=3)

    # A prioridade é um texto e é opcional.
    # Se não for enviada, o valor padrão será 'baixa'.
    prioridade: str = 'baixa'
