// ============================================================================
// 🔓 LOGIN - PÁGINA DE AUTENTICAÇÃO
// ============================================================================
// Fluxo:
// 1. Usuário digita email/senha
// 2. Submit chama API de login
// 3. Se sucesso: salva token no AuthContext e redireciona para /dashboard
// 4. Se erro: exibe mensagem de erro
//
// RECURSOS:
// - useForm: gerencia campos email/senha
// - useApi: gerencia loading/error da requisição
// - useAuth: acessa função login() do contexto
// - Framer Motion: animações de entrada
// - Mensagem condicional: "Bem-vindo" vs "Bem-vindo de Volta"

import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Form, Button, Alert, Spinner } from 'react-bootstrap';
import { motion } from 'framer-motion';
import { login as loginApi } from '../../services/api';
import { useAuth } from '../../context/AuthContext';
import { useForm, useApi } from '../../hooks';
import { notify } from '../../utils/toast';

function Login() {
  // Custom hooks
  const { values, handleChange } = useForm({ email: '', senha: '' });  // Gerencia form
  const { loading, error, execute } = useApi();  // Gerencia chamada API
  const navigate = useNavigate();  // Para redirecionar após login
  const { login } = useAuth();  // Função login do contexto
  
  // Verifica se usuário já logou antes (para mensagem condicional)
  const hasLoggedBefore = localStorage.getItem('lastUserEmail');

  const handleSubmit = async (e) => {
    e.preventDefault();  // Evita reload da página
    
    try {
      // Chama API de login (retorna { access_token: '...' })
      const data = await execute(() => loginApi(values.email, values.senha));
      
      // Salva token e email no contexto global (via AuthContext)
      login(data.access_token, values.email);
      
      // Salva email para mostrar "Bem-vindo de volta" na próxima vez
      localStorage.setItem('lastUserEmail', values.email);
      
      // Feedback visual e redirecionamento
      notify.success('Login realizado com sucesso!');
      navigate('/dashboard');
    } catch (err) {
      // useApi já setou error, aqui só exibimos toast
      notify.error(error || 'Erro ao fazer login');
    }
  };

  return (
    <motion.div
      className="auth-container"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="auth-card">
        <div className="text-center mb-4">
          <motion.div
            style={{ fontSize: '4rem', marginBottom: '1rem' }}
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ type: 'spring', stiffness: 200, delay: 0.2 }}
          >
            🚀
          </motion.div>
          <h2>{hasLoggedBefore ? 'Bem-vindo de Volta!' : 'Bem-vindo!'}</h2>
          <p className="subtitle">
            {hasLoggedBefore ? 'Entre para gerenciar suas tarefas' : 'Faça login para começar'}
          </p>
        </div>

        {error && <Alert variant="danger">{error}</Alert>}

        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              name="email"
              placeholder="seu@email.com"
              value={values.email}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Senha</Form.Label>
            <Form.Control
              type="password"
              name="senha"
              placeholder="••••••••"
              value={values.senha}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </Form.Group>

          <Button 
            variant="primary" 
            type="submit" 
            className="w-100 mb-3"
            disabled={loading}
          >
            {loading ? (
              <>
                <Spinner animation="border" size="sm" className="me-2" />
                Entrando...
              </>
            ) : (
              '🚀 Entrar'
            )}
          </Button>
        </Form>

        <div className="text-center">
          <small>
            Não tem conta? <Link to="/register">Registre-se aqui</Link>
          </small>
        </div>
      </div>
    </motion.div>
  );
}

export default Login;
