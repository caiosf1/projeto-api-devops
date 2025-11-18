import { useState } from 'react';

/**
 * Custom Hook para gerenciar formulários
 * Elimina código repetitivo de useState para cada campo
 * 
 * @param {Object} initialValues - Valores iniciais do formulário
 * @returns {Object} - { values, handleChange, resetForm, setValues }
 */
export function useForm(initialValues = {}) {
  const [values, setValues] = useState(initialValues);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const resetForm = () => {
    setValues(initialValues);
  };

  return {
    values,
    handleChange,
    resetForm,
    setValues
  };
}
