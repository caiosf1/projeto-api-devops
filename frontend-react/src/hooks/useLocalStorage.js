import { useState, useEffect } from 'react';

/**
 * Custom Hook para persistir estado no localStorage
 * Sincroniza automaticamente com localStorage
 * 
 * @param {string} key - Chave do localStorage
 * @param {any} initialValue - Valor inicial
 * @returns {Array} - [value, setValue]
 */
export function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Erro ao ler ${key} do localStorage:`, error);
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      if (value === null || value === undefined) {
        window.localStorage.removeItem(key);
      } else {
        window.localStorage.setItem(key, JSON.stringify(value));
      }
    } catch (error) {
      console.error(`Erro ao salvar ${key} no localStorage:`, error);
    }
  }, [key, value]);

  return [value, setValue];
}
