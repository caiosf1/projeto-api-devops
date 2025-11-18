// ============================================================================
// 📋 TASKLIST - LISTA DE TAREFAS COM FILTROS E ANIMAÇÕES
// ============================================================================
// Responsabilidades:
// - Buscar tarefas da API ao montar componente
// - Filtrar tarefas (todas/pendentes/concluídas)
// - Toggle de conclusão (checkbox)
// - Deletar tarefas com confirmação
// - Exibir skeleton enquanto carrega
// - Animar entrada/saída de itens (Framer Motion)
//
// ESTADO LOCAL:
// - tarefas: array de objetos { id, descricao, prioridade, concluida }
// - filtro: 'todas' | 'pendentes' | 'concluidas'
//
// PADRÃO DE ATUALIZAÇÃO:
// Ao deletar/atualizar, atualiza estado local (setTarefas) sem recarregar
// da API → atualização instantânea na UI (otimistic update)

import { useState, useEffect } from 'react';
import { Card, ListGroup, Badge, Button, Alert } from 'react-bootstrap';
import { motion, AnimatePresence } from 'framer-motion';
import { getTarefas, deleteTarefa, updateTarefa } from '../../services/api';
import { useApi } from '../../hooks';
import { notify } from '../../utils/toast';
import TaskListSkeleton from './TaskListSkeleton';

function TaskList() {
  const [tarefas, setTarefas] = useState([]);  // Lista de tarefas
  const [filtro, setFiltro] = useState('todas');  // Filtro ativo
  const { loading, error, execute } = useApi();  // Para primeira carga

  // Ao montar componente, busca tarefas da API
  useEffect(() => {
    carregarTarefas();
  }, []); // [] = executa apenas uma vez

  const carregarTarefas = async () => {
    try {
      const data = await execute(getTarefas);  // GET /tarefas
      setTarefas(data);
    } catch (err) {
      notify.error('Erro ao carregar tarefas');
    }
  };

  // Toggle de conclusão (checkbox)
  const toggleConcluida = async (id, concluida) => {
    try {
      // Chama API para atualizar no backend
      await updateTarefa(id, { concluida: !concluida });
      
      // Atualiza estado local imediatamente (otimistic update)
      setTarefas(tarefas.map(t => 
        t.id === id ? { ...t, concluida: !concluida } : t
      ));
      
      notify.success(!concluida ? 'Tarefa concluída! 🎉' : 'Tarefa reaberta');
    } catch (err) {
      notify.error('Erro ao atualizar tarefa');
    }
  };

  // Deleta tarefa com confirmação
  const handleDelete = async (id) => {
    if (!window.confirm('Tem certeza que deseja deletar esta tarefa?')) {
      return;  // Cancelou
    }

    try {
      await deleteTarefa(id);  // DELETE /tarefas/:id
      // Remove do estado local
      setTarefas(tarefas.filter(t => t.id !== id));
      notify.info('Tarefa deletada');
    } catch (err) {
      notify.error('Erro ao deletar tarefa');
    }
  };

  // Filtra tarefas com base no botão ativo
  const tarefasFiltradas = tarefas.filter(tarefa => {
    if (filtro === 'pendentes') return !tarefa.concluida;
    if (filtro === 'concluidas') return tarefa.concluida;
    return true;  // 'todas'
  });

  // Retorna cor do badge de prioridade
  const getPrioridadeVariant = (prioridade) => {
    if (prioridade === 'alta') return 'danger';    // Vermelho
    if (prioridade === 'media') return 'warning';  // Amarelo
    return 'success';  // Verde (baixa)
  };

  if (loading) {
    return (
      <Card>
        <Card.Header>
          <h4>📋 Minhas Tarefas</h4>
        </Card.Header>
        <Card.Body>
          <TaskListSkeleton count={5} />
        </Card.Body>
      </Card>
    );
  }

  if (error) {
    return <Alert variant="danger">{error}</Alert>;
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <Card>
        <Card.Header>
          <div className="d-flex justify-content-between align-items-center flex-wrap gap-2">
            <h4>📋 Minhas Tarefas</h4>
            
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
          {tarefasFiltradas.length === 0 && (
            <motion.p 
              className="text-muted text-center"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
            >
              Nenhuma tarefa encontrada
            </motion.p>
          )}

          <ListGroup>
            <AnimatePresence>
              {tarefasFiltradas.map((tarefa) => (
                <motion.div
                  key={tarefa.id}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 20 }}
                  transition={{ duration: 0.2 }}
                >
                  <ListGroup.Item 
                    className="d-flex justify-content-between align-items-center"
                  >
                    <div className="d-flex align-items-center">
                      <input
                        type="checkbox"
                        checked={tarefa.concluida}
                        onChange={() => toggleConcluida(tarefa.id, tarefa.concluida)}
                        className="me-3"
                        style={{ cursor: 'pointer', width: '20px', height: '20px' }}
                      />

                      <span 
                        style={{ 
                          textDecoration: tarefa.concluida ? 'line-through' : 'none',
                          color: tarefa.concluida ? '#6c757d' : '#000'
                        }}
                      >
                        {tarefa.descricao}
                      </span>

                      <Badge 
                        bg={getPrioridadeVariant(tarefa.prioridade)} 
                        className="ms-3"
                      >
                        {tarefa.prioridade}
                      </Badge>
                    </div>

                    <Button 
                      variant="danger" 
                      size="sm"
                      onClick={() => handleDelete(tarefa.id)}
                    >
                      🗑️
                    </Button>
                  </ListGroup.Item>
                </motion.div>
              ))}
            </AnimatePresence>
          </ListGroup>
        </Card.Body>
      </Card>
    </motion.div>
  );
}

export default TaskList;
