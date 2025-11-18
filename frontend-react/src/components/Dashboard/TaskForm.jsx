// ============================================================================
// ➕ COMPONENTE TASKFORM - CRIAR NOVA TAREFA
// ============================================================================
import { useState } from 'react';
import { Form, Button, Card, Alert } from 'react-bootstrap';
import { createTarefa } from '../../services/api';

// onTarefaCriada é uma função passada pelo pai (Dashboard)
// Quando criar tarefa, chama essa função para atualizar a lista
function TaskForm({ onTarefaCriada }) {
  const [descricao, setDescricao] = useState('');
  const [prioridade, setPrioridade] = useState('baixa');
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErro('');

    // Validação: descrição deve ter pelo menos 3 caracteres
    if (descricao.trim().length < 3) {
      setErro('A descrição deve ter pelo menos 3 caracteres');
      return;
    }

    setLoading(true);

    try {
      // Cria a tarefa na API
      const novaTarefa = await createTarefa(descricao, prioridade);
      
      // Limpa o formulário
      setDescricao('');
      setPrioridade('baixa');
      
      // Avisa o componente pai que criou uma tarefa
      if (onTarefaCriada) {
        onTarefaCriada(novaTarefa);
      }
    } catch (error) {
      if (error.response && error.response.data) {
        setErro(error.response.data.erros || 'Erro ao criar tarefa');
      } else {
        setErro('Erro ao conectar com o servidor');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="mb-4">
      <Card.Body>
        <Card.Title>➕ Nova Tarefa</Card.Title>

        {erro && <Alert variant="danger">{erro}</Alert>}

        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3">
            <Form.Label>Descrição</Form.Label>
            <Form.Control
              type="text"
              placeholder="Digite sua tarefa..."
              value={descricao}
              onChange={(e) => setDescricao(e.target.value)}
              required
              disabled={loading}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Prioridade</Form.Label>
            <Form.Select 
              value={prioridade}
              onChange={(e) => setPrioridade(e.target.value)}
              disabled={loading}
            >
              <option value="baixa">🟢 Baixa</option>
              <option value="media">🟡 Média</option>
              <option value="alta">🔴 Alta</option>
            </Form.Select>
          </Form.Group>

          <Button 
            variant="primary" 
            type="submit"
            disabled={loading}
          >
            {loading ? 'Criando...' : 'Adicionar Tarefa'}
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
}

export default TaskForm;
