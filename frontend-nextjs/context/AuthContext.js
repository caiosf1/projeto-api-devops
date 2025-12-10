"use client";

import { createContext, useState, useContext, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import api from '../lib/api';

const AuthContext = createContext({});

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const validateToken = async () => {
      const token = localStorage.getItem('token');
      if (token) {
        try {
          // Valida o token no backend
          const response = await api.get('/auth/me');
          setUser({ 
            token, 
            email: response.data.email,
            id: response.data.id 
          });
        } catch (error) {
          console.error('Token inválido ou expirado:', error);
          localStorage.removeItem('token');
          setUser(null);
        }
      }
      setLoading(false);
    };

    validateToken();
  }, []);

  const login = async (email, senha) => {
    try {
      const response = await api.post('/auth/login', { email, senha });
      const { access_token } = response.data;
      
      localStorage.setItem('token', access_token);
      setUser({ token: access_token, email });
      router.push('/dashboard');
      return true;
    } catch (error) {
      console.error('Erro no login:', error);
      return false;
    }
  };

  const register = async (email, senha) => {
    try {
      await api.post('/auth/register', { email, senha });
      // Auto login após registro ou redirecionar para login
      return await login(email, senha);
    } catch (error) {
      console.error('Erro no registro:', error);
      return false;
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
    router.push('/login');
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
