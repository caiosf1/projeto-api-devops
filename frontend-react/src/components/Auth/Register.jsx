import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Form, Button, Alert } from 'react-bootstrap';
import { register as registerApi } from '../../services/api';

function Register() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [confirmarSenha, setConfirmarSenha] = useState('');
  const [erro, setErro] = useState('');
  const [sucesso, setSucesso] = useState(false);
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErro('');
    setSucesso(false);

    if (senha !== confirmarSenha) {
      setErro('As senhas não coincidem');
      return;
    }

    if (senha.length < 6) {
      setErro('A senha deve ter pelo menos 6 caracteres');
      return;
    }

    setLoading(true);

    try {
      await registerApi(email, senha);
      setSucesso(true);
      
      setTimeout(() => {
        navigate('/login');
      }, 2000);
      
    } catch (error) {
      if (error.response && error.response.data) {
        setErro(error.response.data.erro || 'Erro ao criar conta');
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
          <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>✨</div>
          <h2>Criar Conta</h2>
          <p className="subtitle">Junte-se a nós e organize suas tarefas</p>
        </div>

        {erro && <Alert variant="danger">{erro}</Alert>}
        
        {sucesso && (
          <Alert variant="success">
            Conta criada! Redirecionando para login...
          </Alert>
        )}

        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="seu@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              disabled={loading || sucesso}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Senha</Form.Label>
            <Form.Control
              type="password"
              placeholder="Mínimo 6 caracteres"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              required
              disabled={loading || sucesso}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Confirmar Senha</Form.Label>
            <Form.Control
              type="password"
              placeholder="Digite a senha novamente"
              value={confirmarSenha}
              onChange={(e) => setConfirmarSenha(e.target.value)}
              required
              disabled={loading || sucesso}
            />
          </Form.Group>

          <Button 
            variant="primary" 
            type="submit" 
            className="w-100 mb-3"
            disabled={loading || sucesso}
          >
            {loading ? '⏳ Criando conta...' : '✨ Criar Conta'}
          </Button>
        </Form>

        <div className="text-center">
          <small>
            Já tem conta? <Link to="/login">Faça login aqui</Link>
          </small>
        </div>
      </div>
    </div>
  );
}

export default Register;
