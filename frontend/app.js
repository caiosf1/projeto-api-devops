// ========== CONFIGURAÇÃO ==========
const API_URL = 'http://localhost:5000';

// Elementos DOM
const authScreen = document.getElementById('authScreen');
const dashboardScreen = document.getElementById('dashboardScreen');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const taskForm = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
const userName = document.getElementById('userName');

// Estado da aplicação
let currentFilter = 'todas';
let tasks = [];

// ========== AUTENTICAÇÃO ==========

// Verificar se usuário já está logado
window.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    if (token) {
        showDashboard();
        loadTasks();
    }
});

// Login
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('loginEmail').value;
    const senha = document.getElementById('loginSenha').value;

    try {
        const response = await fetch(`${API_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, senha })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('userName', email.split('@')[0]);
            showToast('Login realizado com sucesso!', 'success');
            showDashboard();
            loadTasks();
        } else {
            showToast(data.message || 'Erro ao fazer login', 'danger');
        }
    } catch (error) {
        showToast('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
});

// Registro
registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const nome = document.getElementById('registerNome').value;
    const email = document.getElementById('registerEmail').value;
    const senha = document.getElementById('registerSenha').value;

    try {
        const response = await fetch(`${API_URL}/auth/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, senha })
        });

        const data = await response.json();

        if (response.ok) {
            showToast('Conta criada! Faça login.', 'success');
            // Mudar para aba de login
            document.getElementById('login-tab').click();
            registerForm.reset();
        } else {
            showToast(data.message || 'Erro ao criar conta', 'danger');
        }
    } catch (error) {
        showToast('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
});

// Logout
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('userName');
    authScreen.classList.remove('hidden');
    dashboardScreen.classList.add('hidden');
    tasks = [];
    showToast('Você saiu da conta', 'info');
}

// Mostrar dashboard
function showDashboard() {
    authScreen.classList.add('hidden');
    dashboardScreen.classList.remove('hidden');
    userName.textContent = localStorage.getItem('userName') || 'Usuário';
}

// ========== TAREFAS ==========

// Carregar tarefas
async function loadTasks() {
    const token = localStorage.getItem('token');

    try {
        const response = await fetch(`${API_URL}/tarefas`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
            tasks = await response.json();
            renderTasks();
            updateStats();
        } else if (response.status === 401) {
            showToast('Sessão expirada. Faça login novamente.', 'warning');
            logout();
        } else {
            showToast('Erro ao carregar tarefas', 'danger');
        }
    } catch (error) {
        showToast('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
}

// Adicionar tarefa
taskForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const token = localStorage.getItem('token');
    const descricao = document.getElementById('taskTitulo').value; // Pega do campo "título" mas envia como "descricao"
    const prioridade = document.getElementById('taskPrioridade').value;

    try {
        const response = await fetch(`${API_URL}/tarefas`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ descricao, prioridade }) // Backend espera "descricao", não "titulo"
        });

        if (response.ok) {
            showToast('Tarefa criada com sucesso!', 'success');
            taskForm.reset();
            loadTasks();
        } else {
            showToast('Erro ao criar tarefa', 'danger');
        }
    } catch (error) {
        showToast('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
});

// Marcar como concluída/pendente
async function toggleTask(id, concluida) {
    const token = localStorage.getItem('token');

    try {
        const response = await fetch(`${API_URL}/tarefas/${id}`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ concluida: !concluida })
        });

        if (response.ok) {
            showToast(
                !concluida ? 'Tarefa concluída! 🎉' : 'Tarefa reaberta',
                'success'
            );
            loadTasks();
        } else {
            showToast('Erro ao atualizar tarefa', 'danger');
        }
    } catch (error) {
        showToast('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
}

// Deletar tarefa
async function deleteTask(id) {
    if (!confirm('Tem certeza que deseja deletar esta tarefa?')) return;

    const token = localStorage.getItem('token');

    try {
        const response = await fetch(`${API_URL}/tarefas/${id}`, {
            method: 'DELETE',
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
            showToast('Tarefa deletada', 'info');
            loadTasks();
        } else {
            showToast('Erro ao deletar tarefa', 'danger');
        }
    } catch (error) {
        showToast('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
}

// ========== RENDERIZAÇÃO ==========

// Renderizar lista de tarefas
function renderTasks() {
    const filteredTasks = tasks.filter(task => {
        if (currentFilter === 'todas') return true;
        if (currentFilter === 'pendentes') return !task.concluida;
        if (currentFilter === 'concluidas') return task.concluida;
    });

    if (filteredTasks.length === 0) {
        taskList.innerHTML = `
            <div class="text-center text-muted py-5">
                <i class="bi bi-inbox" style="font-size: 3rem;"></i>
                <p class="mt-3">Nenhuma tarefa encontrada</p>
            </div>
        `;
        return;
    }

    taskList.innerHTML = filteredTasks.map(task => `
        <div class="task-item ${task.concluida ? 'concluida' : ''}">
            <div class="d-flex justify-content-between align-items-start">
                <div class="flex-grow-1">
                    <div class="d-flex align-items-center mb-2">
                        <input 
                            type="checkbox" 
                            class="form-check-input me-3" 
                            ${task.concluida ? 'checked' : ''}
                            onchange="toggleTask(${task.id}, ${task.concluida})"
                            style="cursor: pointer; width: 20px; height: 20px;"
                        >
                        <h5 class="task-title mb-0">${task.descricao}</h5>
                        <span class="priority-badge priority-${task.prioridade} ms-2">
                            ${task.prioridade.toUpperCase()}
                        </span>
                    </div>
                </div>
                <button 
                    class="btn btn-sm btn-outline-danger" 
                    onclick="deleteTask(${task.id})"
                    title="Deletar"
                >
                    <i class="bi bi-trash"></i>
                </button>
            </div>
        </div>
    `).join('');
}

// Atualizar estatísticas
function updateStats() {
    const total = tasks.length;
    const concluidas = tasks.filter(t => t.concluida).length;
    const pendentes = total - concluidas;

    document.getElementById('statTotal').textContent = total;
    document.getElementById('statPendentes').textContent = pendentes;
    document.getElementById('statConcluidas').textContent = concluidas;
}

// Filtrar tarefas
function filterTasks(filter) {
    currentFilter = filter;
    
    // Atualizar botões
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
    
    renderTasks();
}

// ========== UTILITÁRIOS ==========

// Mostrar toast
function showToast(message, type = 'info') {
    const toastElement = document.getElementById('liveToast');
    const toastBody = document.getElementById('toastMessage');
    
    // Cores baseadas no tipo
    const colors = {
        success: '#28a745',
        danger: '#dc3545',
        warning: '#ffc107',
        info: '#667eea'
    };

    toastElement.querySelector('.toast-header').style.backgroundColor = colors[type] || colors.info;
    toastElement.querySelector('.toast-header').style.color = type === 'warning' ? '#000' : '#fff';
    toastBody.textContent = message;

    const toast = new bootstrap.Toast(toastElement);
    toast.show();
}
