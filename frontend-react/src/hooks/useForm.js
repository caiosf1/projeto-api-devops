// ============================================================================
// 🎨 USEFORM - CUSTOM HOOK PARA FORMULÁRIOS
// ============================================================================
// Hook reutilizável que elimina código repetitivo em formulários.
// 
// ANTES (sem useForm):
// const [email, setEmail] = useState('');
// const [senha, setSenha] = useState('');
// const handleEmailChange = (e) => setEmail(e.target.value);
// const handleSenhaChange = (e) => setSenha(e.target.value);
//
// DEPOIS (com useForm):
// const { values, handleChange } = useForm({ email: '', senha: '' });
// <input name="email" value={values.email} onChange={handleChange} />
//
// QUANDO USAR:
// - Qualquer formulário com múltiplos campos
// - Quando precisar resetar formulário após submit
// - Para evitar criar vários useState e handlers

import { useState } from 'react';

/**
 * Custom Hook para gerenciar formulários
 * 
 * @param {Object} initialValues - Valores iniciais do formulário ex: { email: '', senha: '' }
 * @returns {Object} - { values, handleChange, resetForm, setValues }
 */
export function useForm(initialValues = {}) {
  const [values, setValues] = useState(initialValues);

  // Handler genérico para qualquer input
  // Usa atributo 'name' do input para atualizar campo correto
  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues(prev => ({
      ...prev,
      [name]: value  // Ex: { ...prev, email: 'novo@email.com' }
    }));
  };

  // Reseta formulário para valores iniciais
  // Útil após submit bem-sucedido
  const resetForm = () => {
    setValues(initialValues);
  };

  return {
    values,       // Objeto com todos os valores do form { email: '...', senha: '...' }
    handleChange, // Função onChange genérica
    resetForm,    // Reseta para valores iniciais
    setValues     // Para atualização manual (ex: carregar dados de API)
  };
}
