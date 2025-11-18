// ============================================================================
// 🎯 APP.JSX - COMPONENTE RAIZ DA APLICAÇÃO
// ============================================================================
// Este é o componente principal que gerencia:
// - Rotas da aplicação (Login, Register, Dashboard)
// - Contexto de autenticação (AuthProvider)
// - Notificações toast (ToastContainer)
// - Navegação entre páginas (React Router)

import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import { AuthProvider } from './context/AuthContext';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import Dashboard from './components/Dashboard/Dashboard';
import ProtectedRoute from './components/Layout/ProtectedRoute';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    // AuthProvider: Fornece contexto de autenticação para toda aplicação
    <AuthProvider>
      {/* BrowserRouter: Habilita navegação entre páginas */}
      <BrowserRouter>
        <Routes>
          {/* Rota raiz redireciona para dashboard */}
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          
          {/* Rotas públicas (não requerem login) */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          
          {/* Rota protegida (só acessa se estiver logado) */}
          <Route 
            path="/dashboard" 
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            } 
          />
        </Routes>
        
        {/* Container de notificações toast (aparece no canto superior direito) */}
        <ToastContainer />
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
