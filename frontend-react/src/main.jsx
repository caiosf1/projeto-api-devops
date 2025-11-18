// ============================================================================
// 🎬 MAIN.JSX - ENTRYPOINT DA APLICAÇÃO
// ============================================================================
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

// Renderiza a aplicação no elemento <div id="root"> do index.html
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
