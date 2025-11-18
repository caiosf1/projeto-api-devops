import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Form, Button, Alert } from 'react-bootstrap';
import { login as loginApi } from '../../services/api';
import { useAuth } from '../../context/AuthContext';

function Login() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErro('');
    setLoading(true);

    try {
      const data = await loginApi(email, senha);
      login(data.access_token, email);
      navigate('/dashboard');
    } catch (error) {
      if (error.response && error.response.data) {
        setErro(error.response.data.erro || 'Erro ao fazer login');
      } else {
        setErro('Erro ao conectar com o servidor');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="text-center mb-4">
          <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🚀</div>
          <h2>Bem-vindo de Volta!</h2>
          <p className="subtitle">Entre para gerenciar suas tarefas</p>
        </div>

        {erro && <Alert variant="danger">{erro}</Alert>}

        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="seu@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              disabled={loading}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Senha</Form.Label>
            <Form.Control
              type="password"
              placeholder="••••••••"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
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
            {loading ? '⏳ Entrando...' : '🚀 Entrar'}
          </Button>
        </Form>

        <div className="text-center">
          <small>
            Não tem conta? <Link to="/register">Registre-se aqui</Link>
          </small>
        </div>
      </div>
    </div>
  );
}

export default Login;
