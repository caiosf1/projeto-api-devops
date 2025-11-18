import { useState, useCallback } from 'react';

/**
 * Custom Hook para gerenciar chamadas de API
 * Gerencia loading, error e success states automaticamente
 * 
 * @returns {Object} - { data, loading, error, execute }
 */
export function useApi() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const execute = useCallback(async (apiCall) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await apiCall();
      setData(response);
      return response;
    } catch (err) {
      const errorMessage = err.response?.data?.erro || 
                          err.response?.data?.message || 
                          'Erro ao conectar com o servidor';
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
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
