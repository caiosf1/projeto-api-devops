// ============================================================================
// 🔐 AUTHCONTEXT - CONTEXTO GLOBAL DE AUTENTICAÇÃO
// ============================================================================
// Context API permite compartilhar estado de autenticação em toda a aplicação
// sem precisar passar props manualmente em cada nível (prop drilling).
//
// ESTRUTURA:
// 1. createContext() - Cria o contexto
// 2. AuthProvider - Componente que fornece o valor (wrapper em App.jsx)
// 3. useAuth() - Hook customizado para consumir o contexto
//
// ESTADO GERENCIADO:
// - user: { email: '...' } ou null
// - token: JWT string ou null (salvo em localStorage via useLocalStorage)
// - loading: true enquanto verifica localStorage
// - isAuthenticated: booleano derivado (!!token)
//
// AÇÕES:
// - login(token, email): Salva token e user
// - logout(): Limpa token e user

import { createContext, useState, useContext, useEffect } from 'react';
import { useLocalStorage } from '../hooks';

// Cria o contexto vazio
const AuthContext = createContext();

// Provider: componente que envolve a aplicação em App.jsx
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);  // { email: '...' }
  const [token, setToken] = useLocalStorage('token', null);  // JWT salvo em localStorage
  const [loading, setLoading] = useState(true);  // true até verificar localStorage

  // Ao montar componente, verifica se há token/user salvos
  // Se sim, restaura sessão automaticamente
  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (token && storedUser) {
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);  // Libera renderização do app
  }, [token]);

  // Função chamada após login bem-sucedido
  // Salva token (via useLocalStorage) e user (via localStorage manual)
  const login = (accessToken, userEmail) => {
    const userData = { email: userEmail };
    setToken(accessToken);  // useLocalStorage salva automaticamente
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
  };

  // Limpa autenticação (chamado ao clicar em Sair)
  const logout = () => {
    setToken(null);  // useLocalStorage remove automaticamente
    setUser(null);
    localStorage.removeItem('user');
  };

  // Objeto com todos os valores/funções disponíveis para componentes
  const value = {
    user,              // { email: '...' } ou null
    token,             // JWT string ou null
    loading,           // true enquanto verifica localStorage
    login,             // Função para fazer login
    logout,            // Função para fazer logout
    isAuthenticated: !!token  // true se tem token, false se não
  };

  return (
    <AuthContext.Provider value={value}>
      {/* Só renderiza children após verificar localStorage (loading=false) */}
      {!loading && children}
    </AuthContext.Provider>
  );
}

// Hook customizado para consumir o contexto
// USAR: const { user, login, logout, isAuthenticated } = useAuth();
export function useAuth() {
  const context = useContext(AuthContext);
  // Se tentar usar fora do AuthProvider, lança erro explicativo
  if (!context) {
    throw new Error('useAuth deve ser usado dentro de AuthProvider');
  }
  return context;
}