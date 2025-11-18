// ============================================================================
// 🌐 USEAPI - CUSTOM HOOK PARA CHAMADAS DE API
// ============================================================================
// Hook reutilizável que gerencia os 3 estados de uma requisição:
// 1. loading: true/false
// 2. error: string ou null
// 3. data: resposta da API ou null
//
// ANTES (sem useApi):
// const [loading, setLoading] = useState(false);
// const [error, setError] = useState(null);
// const [data, setData] = useState(null);
// try {
//   setLoading(true);
//   const response = await api.get('/tarefas');
//   setData(response.data);
// } catch(err) {
//   setError(err.message);
// } finally {
//   setLoading(false);
// }
//
// DEPOIS (com useApi):
// const { data, loading, error, execute } = useApi();
// await execute(() => api.get('/tarefas'));
//
// QUANDO USAR:
// - Qualquer componente que faz chamadas HTTP
// - Para mostrar spinners (loading)
// - Para exibir mensagens de erro

import { useState, useCallback } from 'react';

/**
 * Custom Hook para gerenciar chamadas de API
 * 
 * @returns {Object} - { data, loading, error, execute, reset }
 */
export function useApi() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Executa a chamada de API com tratamento automático de estados
  // useCallback evita recriar função a cada render (otimização)
  const execute = useCallback(async (apiCall) => {
    setLoading(true);   // Mostra spinner
    setError(null);     // Limpa erro anterior
    
    try {
      const response = await apiCall();  // Executa função recebida
      setData(response);                 // Salva resposta
      return response;                   // Retorna para quem chamou
    } catch (err) {
      // Extrai mensagem de erro da resposta da API
      const errorMessage = err.response?.data?.erro || 
                          err.response?.data?.message || 
                          'Erro ao conectar com o servidor';
      setError(errorMessage);
      throw err;  // Repassa erro para componente tratar se quiser
    } finally {
      setLoading(false);  // Esconde spinner sempre (sucesso ou erro)
    }
  }, []);

  const reset = useCallback(() => {
    setData(null);
    setError(null);
    setLoading(false);
  }, []);

  return {
    data,
    loading,
    error,
    execute,
    reset
  };
}
