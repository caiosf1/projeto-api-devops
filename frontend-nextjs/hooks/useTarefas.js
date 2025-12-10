import { useState, useEffect, useCallback } from 'react';
import api from '../lib/api';

export function useTarefas(user) {
  const [tarefas, setTarefas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchTarefas = useCallback(async () => {
    if (!user) return;
    try {
      setLoading(true);
      const response = await api.get('/tarefas');
      setTarefas(response.data);
      setError(null);
    } catch (err) {
      console.error('Erro ao buscar tarefas:', err);
      setError('Falha ao carregar tarefas.');
    } finally {
      setLoading(false);
    }
  }, [user]);

  useEffect(() => {
    fetchTarefas();
  }, [fetchTarefas]);

  const addTarefa = async (descricao, prioridade = 'media') => {
    try {
      // Optimistic update (opcional, mas moderno)
      // const tempId = Date.now();
      // setTarefas([...tarefas, { id: tempId, descricao, prioridade, temp: true }]);
      
      const response = await api.post('/tarefas', { descricao, prioridade });
      setTarefas(prev => [...prev, response.data]);
      return { success: true };
    } catch (err) {
      console.error('Erro ao criar tarefa:', err);
      return { success: false, error: 'Erro ao criar tarefa' };
    }
  };

  const deleteTarefa = async (id) => {
    try {
      // Optimistic update
      const previousTarefas = [...tarefas];
      setTarefas(tarefas.filter(t => t.id !== id));

      await api.delete(`/tarefas/${id}`);
      return { success: true };
    } catch (err) {
      console.error('Erro ao deletar:', err);
      // Revert on error
      // setTarefas(previousTarefas); 
      // Para simplificar, apenas recarregamos
      fetchTarefas();
      return { success: false, error: 'Erro ao deletar tarefa' };
    }
  };

  const toggleTarefa = async (id, concluida) => {
    try {
      // Optimistic update
      setTarefas(prev => prev.map(t => 
        t.id === id ? { ...t, concluida: !concluida } : t
      ));

      await api.put(`/tarefas/${id}`, { concluida: !concluida });
      return { success: true };
    } catch (err) {
      console.error('Erro ao concluir tarefa:', err);
      // Revert optimistic update
      fetchTarefas();
      return { success: false };
    }
  };

  return { 
    tarefas, 
    loading, 
    error, 
    addTarefa, 
    deleteTarefa,
    toggleTarefa
  };
}
