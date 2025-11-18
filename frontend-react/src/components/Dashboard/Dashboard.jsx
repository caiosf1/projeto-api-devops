// ============================================================================
// 🏠 DASHBOARD - PÁGINA PRINCIPAL
// ============================================================================
// Componente pai que junta TaskForm + TaskList
import { useState } from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import TaskForm from './TaskForm';
import TaskList from './TaskList';

function Dashboard() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [refresh, setRefresh] = useState(0);  // Truque para forçar TaskList recarregar

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  // Quando criar tarefa, incrementa refresh para TaskList recarregar
  const handleTarefaCriada = () => {
    setRefresh(prev => prev + 1);
  };

  return (
    <div style={{ background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', minHeight: '100vh', paddingTop: '20px' }}>
      <Container>
        {/* HEADER */}
        <div className="d-flex justify-content-between align-items-center mb-4 text-white">
          <div>
            <h1>🎯 Sistema de Tarefas</h1>
            <p>Bem-vindo, <strong>{user?.email}</strong></p>
          </div>
          <Button variant="light" onClick={handleLogout}>
            🚪 Sair
          </Button>
        </div>

        <Row>
          {/* COLUNA ESQUERDA - FORMULÁRIO */}
          <Col md={4}>
            <TaskForm onTarefaCriada={handleTarefaCriada} />
          </Col>

          {/* COLUNA DIREITA - LISTA */}
          <Col md={8}>
            <TaskList key={refresh} />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Dashboard;
