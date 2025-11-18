// ============================================================================
// ✨ REGISTER - PÁGINA DE CADASTRO
// ============================================================================
// Fluxo:
// 1. Usuário digita email, senha e confirmação
// 2. Validações: senhas coincidem? mínimo 6 caracteres?
// 3. Submit chama API de registro
// 4. Se sucesso: exibe mensagem e redireciona para /login após 2s
// 5. Se erro: exibe mensagem de erro
//
// RECURSOS:
// - useForm: gerencia 3 campos (email, senha, confirmarSenha)
// - useApi: gerencia loading/error/sucesso
// - Validação frontend antes de chamar API
// - Framer Motion: animações de entrada

import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Form, Button, Alert, Spinner } from 'react-bootstrap';
import { motion } from 'framer-motion';
import { register as registerApi } from '../../services/api';
import { useForm, useApi } from '../../hooks';
import { notify } from '../../utils/toast';

function Register() {
  // Gerencia 3 campos: email, senha, confirmarSenha
  const { values, handleChange, resetForm } = useForm({
    email: '',
    senha: '',
    confirmarSenha: ''
  });
  const { loading, error, execute } = useApi();
  const [sucesso, setSucesso] = useState(false);  // Para exibir mensagem de sucesso
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // VALIDAÇÃO 1: Senhas devem ser iguais
    if (values.senha !== values.confirmarSenha) {
      notify.error('As senhas não coincidem');
      return;  // Para execução aqui
    }

    // VALIDAÇÃO 2: Senha mínima de 6 caracteres
    if (values.senha.length < 6) {
      notify.error('A senha deve ter pelo menos 6 caracteres');
      return;
    }

    try {
      // Chama API de registro (backend cria usuário no banco)
      await execute(() => registerApi(values.email, values.senha));
      setSucesso(true);  // Exibe Alert de sucesso
      notify.success('Conta criada com sucesso!');
      resetForm();  // Limpa formulário
      
      // Após 2 segundos, redireciona para login
      setTimeout(() => {
        navigate('/login');
      }, 2000);
    } catch (err) {
      // useApi já setou error, aqui só exibimos toast
      notify.error(error || 'Erro ao criar conta');
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
            ✨
          </motion.div>
          <h2>Criar Conta</h2>
          <p className="subtitle">Junte-se a nós e organize suas tarefas</p>
        </div>

        {error && <Alert variant="danger">{error}</Alert>}
        
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
              name="email"
              placeholder="seu@email.com"
              value={values.email}
              onChange={handleChange}
              required
              disabled={loading || sucesso}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Senha</Form.Label>
            <Form.Control
              type="password"
              name="senha"
              placeholder="Mínimo 6 caracteres"
              value={values.senha}
              onChange={handleChange}
              required
              disabled={loading || sucesso}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Confirmar Senha</Form.Label>
            <Form.Control
              type="password"
              name="confirmarSenha"
              placeholder="Digite a senha novamente"
              value={values.confirmarSenha}
              onChange={handleChange}
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
            {loading ? (
              <>
                <Spinner animation="border" size="sm" className="me-2" />
                Criando conta...
              </>
            ) : (
              '✨ Criar Conta'
            )}
          </Button>
        </Form>

        <div className="text-center">
          <small>
            Já tem conta? <Link to="/login">Faça login aqui</Link>
          </small>
        </div>
      </div>
    </motion.div>
  );
}

export default Register;
