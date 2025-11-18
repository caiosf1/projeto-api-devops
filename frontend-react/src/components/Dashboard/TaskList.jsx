// ============================================================================
// 📋 COMPONENTE TASKLIST - LISTA DE TAREFAS
// ============================================================================
// Aqui você vai ver useEffect buscando dados da API quando o componente carrega!

import { useState, useEffect } from 'react';
import { Card, ListGroup, Badge, Button, Spinner, Alert } from 'react-bootstrap';
import { getTarefas, deleteTarefa, updateTarefa } from '../../services/api';

function TaskList() {
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // 🎯 useState - ESTADOS DO COMPONENTE
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const [tarefas, setTarefas] = useState([]);         // Array de tarefas
  const [loading, setLoading] = useState(true);       // true = mostra spinner
  const [erro, setErro] = useState('');               // Mensagem de erro
  const [filtro, setFiltro] = useState('todas');      // 'todas', 'pendentes', 'concluidas'

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // 🎯 useEffect - BUSCAR TAREFAS QUANDO O COMPONENTE CARREGA
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // [] vazio = executa UMA VEZ (quando o componente monta)
  useEffect(() => {
    carregarTarefas();
  }, []);  // ← Array vazio = executa só quando monta o componente

  // Função para buscar tarefas da API
  const carregarTarefas = async () => {
    try {
      setLoading(true);
      const data = await getTarefas();  // Chama API
      setTarefas(data);                 // Salva no state
    } catch (error) {
      setErro('Erro ao carregar tarefas');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // FUNÇÃO: MARCAR COMO CONCLUÍDA/PENDENTE
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const toggleConcluida = async (id, concluida) => {
    try {
      await updateTarefa(id, { concluida: !concluida });
      
      // Atualiza o state localmente (sem precisar buscar tudo de novo)
      setTarefas(tarefas.map(t => 
        t.id === id ? { ...t, concluida: !concluida } : t
      ));
    } catch (error) {
      alert('Erro ao atualizar tarefa');
    }
  };

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // FUNÇÃO: DELETAR TAREFA
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const handleDelete = async (id) => {
    if (!window.confirm('Tem certeza que deseja deletar esta tarefa?')) {
      return;
    }

    try {
      await deleteTarefa(id);
      
      // Remove do state
      setTarefas(tarefas.filter(t => t.id !== id));
    } catch (error) {
      alert('Erro ao deletar tarefa');
    }
  };

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // FILTRAR TAREFAS
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const tarefasFiltradas = tarefas.filter(tarefa => {
    if (filtro === 'pendentes') return !tarefa.concluida;
    if (filtro === 'concluidas') return tarefa.concluida;
    return true;  // 'todas'
  });

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // FUNÇÃO: COR DO BADGE DE PRIORIDADE
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const getPrioridadeVariant = (prioridade) => {
    if (prioridade === 'alta') return 'danger';
    if (prioridade === 'media') return 'warning';
    return 'success';
  };

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // RENDERIZAÇÃO
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
  // Se estiver carregando, mostra spinner
  if (loading) {
    return (
      <div className="text-center my-5">
        <Spinner animation="border" />
        <p className="mt-2">Carregando tarefas...</p>
      </div>
    );
  }

  // Se tiver erro, mostra alerta
  if (erro) {
    return <Alert variant="danger">{erro}</Alert>;
  }

  return (
    <Card>
      <Card.Header>
        <div className="d-flex justify-content-between align-items-center">
          <h4>📋 Minhas Tarefas</h4>
          
          {/* BOTÕES DE FILTRO */}
          <div>
            <Button 
              size="sm" 
              variant={filtro === 'todas' ? 'primary' : 'outline-primary'}
              onClick={() => setFiltro('todas')}
              className="me-2"
            >
              Todas ({tarefas.length})
            </Button>
            <Button 
              size="sm" 
              variant={filtro === 'pendentes' ? 'warning' : 'outline-warning'}
              onClick={() => setFiltro('pendentes')}
              className="me-2"
            >
              Pendentes ({tarefas.filter(t => !t.concluida).length})
            </Button>
            <Button 
              size="sm" 
              variant={filtro === 'concluidas' ? 'success' : 'outline-success'}
              onClick={() => setFiltro('concluidas')}
            >
              Concluídas ({tarefas.filter(t => t.concluida).length})
            </Button>
          </div>
        </div>
      </Card.Header>

      <Card.Body>
        {/* Se não tiver tarefas */}
        {tarefasFiltradas.length === 0 && (
          <p className="text-muted text-center">Nenhuma tarefa encontrada</p>
        )}

        {/* LISTA DE TAREFAS */}
        <ListGroup>
          {tarefasFiltradas.map((tarefa) => (
            <ListGroup.Item 
              key={tarefa.id}
              className="d-flex justify-content-between align-items-center"
            >
              <div className="d-flex align-items-center">
                {/* CHECKBOX */}
                <input
                  type="checkbox"
                  checked={tarefa.concluida}
                  onChange={() => toggleConcluida(tarefa.id, tarefa.concluida)}
                  className="me-3"
                />

                {/* DESCRIÇÃO */}
                <span 
                  style={{ 
                    textDecoration: tarefa.concluida ? 'line-through' : 'none',
                    color: tarefa.concluida ? '#6c757d' : '#000'
                  }}
                >
                  {tarefa.descricao}
                </span>

                {/* BADGE DE PRIORIDADE */}
                <Badge 
                  bg={getPrioridadeVariant(tarefa.prioridade)} 
                  className="ms-3"
                >
                  {tarefa.prioridade}
                </Badge>
              </div>

              {/* BOTÃO DELETE */}
              <Button 
                variant="danger" 
                size="sm"
                onClick={() => handleDelete(tarefa.id)}
              >
                🗑️
              </Button>
            </ListGroup.Item>
          ))}
        </ListGroup>
      </Card.Body>
    </Card>
  );
}

export default TaskList;

// ============================================================================
// 📚 O QUE VOCÊ APRENDEU AQUI:
// ============================================================================
// 1. useEffect(() => {}, []) - Executa quando componente monta
// 2. Chamar API assíncrona e atualizar state
// 3. Conditional rendering: {loading && <Spinner />}
// 4. .map() para renderizar lista
// 5. .filter() para filtrar arrays
// 6. Atualizar state de forma imutável: setTarefas(tarefas.map(...))
// 7. Event handlers: onChange, onClick
