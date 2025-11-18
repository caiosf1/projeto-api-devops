// ============================================================================
// 📚 AUTHCONTEXT - SEU PRIMEIRO CONTEXT API!
// ============================================================================
// O que é Context? É uma forma de COMPARTILHAR dados entre componentes
// sem precisar passar props manualmente de pai para filho
//
// Analogia: É como uma "caixa de correio global" que todos os componentes
// podem acessar para pegar informações do usuário logado

import { createContext, useState, useContext, useEffect } from 'react';

// ============================================================================
// PASSO 1: CRIAR O CONTEXT (a "caixa de correio")
// ============================================================================
const AuthContext = createContext();

// ============================================================================
// PASSO 2: CRIAR O PROVIDER (quem gerencia a "caixa de correio")
// ============================================================================
// Este componente vai ENVOLVER toda a aplicação e fornecer os dados de auth
export function AuthProvider({ children }) {
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // 🎯 useState - GERENCIAR ESTADO
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // Sintaxe: const [valor, funcaoParaMudar] = useState(valorInicial)
  //
  // user: guarda os dados do usuário logado (null = ninguém logado)
  // setUser: função para MUDAR o valor de user
  const [user, setUser] = useState(null);
  
  // token: guarda o JWT token (string) ou null se não tiver
  const [token, setToken] = useState(null);
  
  // loading: true enquanto está verificando se tem usuário salvo no localStorage
  const [loading, setLoading] = useState(true);

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // 🎯 useEffect - EXECUTAR CÓDIGO QUANDO ALGO MUDA
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // Sintaxe: useEffect(() => { código }, [dependências])
  //
  // [] vazio = executa UMA VEZ quando o componente é criado (igual window.onload)
  // [variavel] = executa toda vez que 'variavel' muda
  useEffect(() => {
    // Quando o app inicia, verifica se tem token salvo no navegador
    const storedToken = localStorage.getItem('token');
    const storedUser = localStorage.getItem('user');

    if (storedToken && storedUser) {
      // Se achar, coloca nos states
      setToken(storedToken);
      setUser(JSON.parse(storedUser)); // JSON.parse transforma string em objeto
    }

    setLoading(false); // Terminou de carregar
  }, []); // [] = executa só 1 vez (quando monta o componente)

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // FUNÇÕES QUE OUTROS COMPONENTES VÃO USAR
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  
  // Função: Fazer login
  const login = (accessToken, userEmail) => {
    const userData = { email: userEmail };
    
    // Salva no state (memória React)
    setToken(accessToken);
    setUser(userData);
    
    // Salva no localStorage (memória do navegador - persiste ao fechar aba)
    localStorage.setItem('token', accessToken);
    localStorage.setItem('user', JSON.stringify(userData));
  };

  // Função: Fazer logout
  const logout = () => {
    // Limpa tudo
    setToken(null);
    setUser(null);
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  };

  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // O QUE ESSE CONTEXT VAI FORNECER PARA OUTROS COMPONENTES
  // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const value = {
    user,           // Dados do usuário logado (ou null)
    token,          // JWT token (ou null)
    loading,        // true se ainda está carregando
    login,          // Função para fazer login
    logout,         // Função para fazer logout
    isAuthenticated: !!token  // !! converte para boolean (se tem token = true)
  };

  // Retorna o Provider que vai envolver a aplicação
  // Todos os componentes dentro de {children} podem acessar 'value'
  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

// ============================================================================
// PASSO 3: CRIAR HOOK CUSTOMIZADO PARA USAR O CONTEXT
// ============================================================================
// Este hook facilita usar o context em outros componentes
// Ao invés de: const context = useContext(AuthContext)
// Você usa: const { user, login, logout } = useAuth()
export function useAuth() {
  const context = useContext(AuthContext);
  
  if (!context) {
    throw new Error('useAuth deve ser usado dentro de AuthProvider');
  }
  
  return context;
}

// ============================================================================
// COMO USAR ESSE CONTEXT EM OUTROS COMPONENTES?
// ============================================================================
// Exemplo:
//
// import { useAuth } from './context/AuthContext';
//
// function MeuComponente() {
//   const { user, login, logout, isAuthenticated } = useAuth();
//
//   if (isAuthenticated) {
//     return <p>Bem-vindo, {user.email}!</p>;
//   }
//
//   return <button onClick={() => login('token123', 'user@email.com')}>Login</button>;
// }
