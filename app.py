#1. Importações: Trazendo as ferramentas da nossa caixa "venv"
from flask import Flask, jsonify, request

#2. Criação da aplicação: A instancia principal do nosso programa
app = Flask(__name__)

#3. "Banco de dados Fake": Uma lista de dicionários para guardar nossas tarefas

tarefas = [
    {"id": 1, "descricao": "Estudar Docker","concluida":False},
    {"id": 2, "descricao": "Fazer o projeto da API", "concluida": True}
]

# 4. Rota para LER todas as tarefas (GET)
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    # A Função jsonify pega nossa lista python e a converte para o formato JSON
    return jsonify(tarefas)

#5. Rota para CRIAR uma nova tarefa (POST)
@app.route('/tarefas', methods=['POST'])
def criar_tarefas():
    # Pega o corpo da requisição, que esperamos ser um JSON, e o transforma em um dicionário Python
    dados = request.get_json()
    nova_tarefa = {
        "id": tarefas[-1]['id'] + 1,
        "descricao": dados['descricao'],
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

#5. Rota para ATUALIZAR uma noma tarefa (UPDATE)
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefas(id):
    global tarefas
    
    tarefas_modificadas = None
    #1. Visita cada dicionário na nossa lista de tarefas
    for tarefa in tarefas:
        #2. Pergunta se o 'id' do dicionário atual é oque procuramos
        if tarefa['id'] == id:
            #3. Se for, dá a ordem para mudar o valor de 'concluida'
            tarefa['concluida'] = True
            tarefas_modificadas = tarefa
            break #Já encontramos, podemos parar o loop
    #4. Retorna a tarefa que foi modificada para o usuário ver o resultado
    if tarefas_modificadas:
        return jsonify(tarefas_modificadas)
    return jsonify({"erro": "Tarefa não encontrada"}), 404 #Se o loop terminar e não encontrarmos a tarefa

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefas(id):
    # Não se esqueça da permissão para modificar a lista global!
    global tarefas
     # Passo 1: Use um 'for' loop e um 'if' para encontrar a tarefa.
    # Guarde a tarefa encontrada em uma variável.
    tarefas_encontrada = None
    
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas_encontrada = tarefa
            break
    
    # Passo 2: Se a tarefa foi encontrada, use o método .remove() para apagá-la.
    # Passo 3: Retorne o jsonify com a mensagem de sucesso.
    # Bônus: E se a tarefa não for encontrada? Retorne uma mensagem de erro com status 404.
    if tarefas_encontrada:
        tarefas.remove(tarefas_encontrada)
        return jsonify({'mensagem': 'Tarefa deletada com sucesso'}), 200
    return jsonify({"Erro": "Tarefa não encontrada"}), 404
        
            
            
            




#5. O "Interruptor": este bloco fazer o servidor de fato rodar quando executamos o arquivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)