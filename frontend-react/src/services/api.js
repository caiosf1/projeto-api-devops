// ============================================================================
// 📡 API SERVICE - COMUNICAÇÃO COM O BACKEND FLASK
// ============================================================================
// Axios é uma biblioteca para fazer requisições HTTP (GET, POST, PUT, DELETE)
// Ele é melhor que fetch() porque:
// - Converte JSON automaticamente
// - Tem interceptors (middleware para adicionar token em TODAS as requisições)
// - Tratamento de erros mais simples

import axios from 'axios';

// ============================================================================
// CONFIGURAÇÃO BASE
// ============================================================================
// Cria uma instância do axios com configurações padrão
const api = axios.create({
  baseURL: 'https://api.caiodev.me',  // URL base do seu backend Flask
  headers: {
    'Content-Type': 'application/json'
  },
  timeout: 15000,  // Timeout de 15 segundos
  withCredentials: false  // Não envia cookies (usa JWT no header)
});

// ============================================================================
// INTERCEPTOR DE REQUISIÇÃO - ADICIONA TOKEN AUTOMATICAMENTE
// ============================================================================
// Isso é MUITO importante! Toda requisição vai passar por aqui ANTES de ser enviada
// Se tiver token salvo, ele adiciona automaticamente no header Authorization
//
// Sem interceptor você teria que fazer isso em CADA requisição:
// axios.get('/tarefas', { headers: { Authorization: `Bearer ${token}` }})
//
// Com interceptor, só precisa fazer:
// api.get('/tarefas')  ← O token é adicionado automaticamente!

api.interceptors.request.use(
  (config) => {
    // Pega o token do localStorage
    let token = localStorage.getItem('token');
    
    // Se tiver token, remove aspas extras (JSON.parse caso necessário)
    if (token) {
      try {
        // Se o token estiver em JSON (entre aspas), faz parse
        token = JSON.parse(token);
      } catch {
        // Se não for JSON, usa direto (já é string pura)
      }
      config.headers.Authorization = `Bearer ${token}`;
    }
    
    return config;
  },
  (error) => {
    // Se der erro antes de enviar (raro), rejeita
    return Promise.reject(error);
  }
);

// ============================================================================
// INTERCEPTOR DE RESPOSTA - TRATA ERROS GLOBALMENTE
// ============================================================================
// Se a API retornar erro 401 (não autorizado), limpa o token e redireciona para login
api.interceptors.response.use(
  (response) => {
    // Se deu certo, só retorna a resposta
    return response;
  },
  (error) => {
    // Log de debug para ver o erro exato
    console.error('API Error:', {
      message: error.message,
      response: error.response?.data,
      status: error.response?.status,
      url: error.config?.url
    });
    
    // Se for erro 401 (token expirado ou inválido)
    if (error.response && error.response.status === 401) {
      // Limpa o token
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      
      // Redireciona para login (se não estiver na tela de login)
      if (window.location.pathname !== '/login') {
        window.location.href = '/login';
      }
    }
    
    return Promise.reject(error);
  }
);

// ============================================================================
// FUNÇÕES DA API - AUTENTICAÇÃO
// ============================================================================

// Registrar novo usuário
export const register = async (email, senha) => {
  const response = await api.post('/auth/register', { email, senha });
  return response.data;
};

// Fazer login
export const login = async (email, senha) => {
  const response = await api.post('/auth/login', { email, senha });
  return response.data; // Retorna { access_token: "..." }
};

// ============================================================================
// FUNÇÕES DA API - TAREFAS
// ============================================================================

// Listar todas as tarefas do usuário logado
export const getTarefas = async () => {
  const response = await api.get('/tarefas');
  return response.data;
};

// Criar nova tarefa
export const createTarefa = async (descricao, prioridade = 'baixa') => {
  const response = await api.post('/tarefas', { descricao, prioridade });
  return response.data;
};

// Atualizar tarefa existente
export const updateTarefa = async (id, dados) => {
  // dados pode ser: { descricao: "...", concluida: true, prioridade: "alta" }
  const response = await api.put(`/tarefas/${id}`, dados);
  return response.data;
};

// Deletar tarefa
export const deleteTarefa = async (id) => {
  const response = await api.delete(`/tarefas/${id}`);
  return response.data;
};

// Marcar tarefa como concluída/pendente (toggle)
export const toggleTarefa = async (id, concluida) => {
  const response = await api.put(`/tarefas/${id}`, { concluida });
  return response.data;
};

// ============================================================================
// EXPORTA A INSTÂNCIA DO AXIOS PARA CASOS ESPECIAIS
// ============================================================================
// Se precisar fazer uma requisição customizada, pode usar:
// import api from './services/api';
// api.get('/algum-endpoint-customizado')
export default api;

// ============================================================================
// COMO USAR ESSAS FUNÇÕES NOS COMPONENTES?
// ============================================================================
// Exemplo de Login:
//
// import { login } from './services/api';
//
// const handleLogin = async () => {
//   try {
//     const data = await login('user@email.com', 'senha123');
//     console.log(data.access_token);  // Token JWT
//   } catch (error) {
//     console.error('Erro no login:', error);
//   }
// };
//
// Exemplo de Listar Tarefas:
//
// import { getTarefas } from './services/api';
// import { useState, useEffect } from 'react';
//
// function TaskList() {
//   const [tarefas, setTarefas] = useState([]);
//
//   useEffect(() => {
//     getTarefas().then(data => setTarefas(data));
//   }, []);
//
//   return <div>{tarefas.map(t => <p key={t.id}>{t.descricao}</p>)}</div>;
// }
