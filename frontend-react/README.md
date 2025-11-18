# 🎓 Frontend React - Guia de Aprendizado

## 📚 O que você criou?

Uma aplicação React completa com:
- ✅ **useState** - Gerenciar estado dos componentes
- ✅ **useEffect** - Executar ações quando componente carrega
- ✅ **Context API** - Compartilhar dados de autenticação entre componentes
- ✅ **React Router** - Navegação entre páginas
- ✅ **React Bootstrap** - Componentes estilizados
- ✅ **Axios** - Chamadas de API com interceptors

## 🚀 Como Rodar

### 1. Instalar Node.js (se ainda não tem)

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm

# Verificar instalação
node --version
npm --version
```

### 2. Instalar Dependências

```bash
cd frontend-react
npm install
```

### 3. Rodar em Desenvolvimento

```bash
npm run dev
```

Abrirá automaticamente em: http://localhost:3000

### 4. Build para Produção

```bash
npm run build
```

Gera pasta `/dist` pronta para deploy

---

## 📖 Conceitos React - Explicados

### 1️⃣ **useState** - Gerenciar Estado

```jsx
const [nome, setNome] = useState('');  // Estado inicial: string vazia

// Ler o valor
console.log(nome);  // ''

// Atualizar o valor
setNome('João');    // Agora nome = 'João'
```

**Analogia**: É como uma variável, mas quando você muda ela, o React re-renderiza o componente.

**Exemplo Real** (Login.jsx):
```jsx
const [email, setEmail] = useState('');
const [senha, setSenha] = useState('');

// No input:
<input 
  value={email} 
  onChange={(e) => setEmail(e.target.value)} 
/>
```

Quando você digita, `setEmail()` atualiza o state e o input mostra o novo valor.

---

### 2️⃣ **useEffect** - Executar Código Quando Algo Muda

```jsx
useEffect(() => {
  // Código aqui
}, [dependências]);
```

**Regras**:
- `[]` vazio = executa UMA VEZ (quando monta o componente)
- `[variavel]` = executa quando `variavel` muda
- Sem array = executa em TODA re-renderização (cuidado!)

**Exemplo Real** (TaskList.jsx):
```jsx
useEffect(() => {
  carregarTarefas();  // Busca tarefas da API
}, []);  // [] = só executa 1 vez
```

---

### 3️⃣ **Context API** - Compartilhar Dados Globalmente

**Problema sem Context**:
```
App
 ├─ Header (precisa do usuário)
 ├─ Dashboard (precisa do usuário)
 │   └─ TaskList (precisa do usuário)
 └─ Footer (precisa do usuário)
```

Sem Context, você teria que passar `user` como prop de pai para filho para filho...

**Solução com Context**:
```jsx
// Cria Context
const AuthContext = createContext();

// Provider envolve a app
<AuthProvider>
  <App />
</AuthProvider>

// Qualquer componente acessa
const { user } = useAuth();
```

**Exemplo Real** (AuthContext.jsx):
```jsx
// Define Context
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  
  const login = (token, email) => {
    setUser({ email });
  };
  
  return (
    <AuthContext.Provider value={{ user, login }}>
      {children}
    </AuthContext.Provider>
  );
}

// Usa em qualquer componente
function Dashboard() {
  const { user, login, logout } = useAuth();
  // ...
}
```

---

## 🗂️ Estrutura de Arquivos

```
src/
├── main.jsx                    # Entrypoint (ReactDOM.render)
├── App.jsx                     # Rotas da aplicação
├── context/
│   └── AuthContext.jsx         # 🔑 Context API (user, login, logout)
├── services/
│   └── api.js                  # 📡 Axios + interceptors JWT
├── components/
│   ├── Auth/
│   │   ├── Login.jsx           # 🔐 useState + API call
│   │   └── Register.jsx        # 📝 Validação de formulário
│   ├── Dashboard/
│   │   ├── Dashboard.jsx       # 🏠 Página principal
│   │   ├── TaskForm.jsx        # ➕ Criar tarefa
│   │   └── TaskList.jsx        # 📋 useEffect + filtros
│   └── Layout/
│       └── ProtectedRoute.jsx  # 🔒 Rota protegida
```

---

## 🎯 Fluxo de Dados

### Fluxo de Login:
```
1. Usuário digita email/senha
   ↓
2. Login.jsx: handleSubmit() chama loginApi()
   ↓
3. services/api.js: POST /auth/login
   ↓
4. Backend retorna { access_token }
   ↓
5. Login.jsx: chama login() do Context
   ↓
6. AuthContext: salva token no state + localStorage
   ↓
7. Login.jsx: navigate('/dashboard')
   ↓
8. ProtectedRoute: verifica isAuthenticated
   ↓
9. Dashboard renderiza!
```

### Fluxo de Carregar Tarefas:
```
1. TaskList monta (useEffect)
   ↓
2. useEffect chama carregarTarefas()
   ↓
3. carregarTarefas() chama getTarefas()
   ↓
4. services/api.js: GET /tarefas (token automático via interceptor)
   ↓
5. Backend retorna array de tarefas
   ↓
6. setTarefas(data) atualiza state
   ↓
7. TaskList re-renderiza com as tarefas
```

---

## 🔍 Como Debugar

### Ver o que está no state:
```jsx
const [email, setEmail] = useState('');

console.log('Estado atual:', email);  // Debug
```

### Ver chamadas de API:
```jsx
const carregarTarefas = async () => {
  console.log('Iniciando carregamento...');
  const data = await getTarefas();
  console.log('Tarefas recebidas:', data);
  setTarefas(data);
};
```

### React DevTools (extensão do navegador):
- Chrome: https://chrome.google.com/webstore → "React Developer Tools"
- Veja todos os states, props, Context em tempo real!

---

## 📚 Próximos Passos para Aprender Mais

### 1. **Entenda cada arquivo criado**
Leia os comentários linha por linha. Tente mudar algo e veja o que acontece!

### 2. **Adicione funcionalidade nova**
Ideias:
- Editar tarefa (modal com formulário)
- Ordenar por prioridade
- Buscar tarefa por texto
- Dark mode com Context

### 3. **Estude esses conceitos**
- [ ] Desestruturação: `const { user, login } = useAuth()`
- [ ] Array methods: `.map()`, `.filter()`, `.find()`
- [ ] Spread operator: `{ ...tarefa, concluida: true }`
- [ ] Async/await vs Promises
- [ ] Optional chaining: `user?.email`

### 4. **Recursos de Estudo**
- 📺 **YouTube**: "React para Iniciantes" (vários canais bons)
- 📖 **Documentação**: https://react.dev/learn
- 🎓 **Prática**: Tente recriar componentes sem olhar o código

---

## 💡 Dicas do Seu Amigo Pleno

Ele tem razão! Com **useState, useEffect e Context**, você já sabe 80% do React usado no dia a dia.

**O que falta?**
- Custom Hooks (criar seus próprios hooks)
- useCallback/useMemo (otimização - avançado)
- useReducer (alternativa ao useState para estados complexos)

Mas não se preocupe com isso agora. **Domine esses 3 primeiro!**

---

## 🎯 Checklist de Aprendizado

- [ ] Entendo o que é useState e como usar
- [ ] Entendo quando useEffect executa ([] vazio vs [variavel])
- [ ] Entendo como Context evita "prop drilling"
- [ ] Consigo criar um formulário com validação
- [ ] Consigo fazer chamada de API e mostrar dados
- [ ] Consigo atualizar lista sem recarregar página
- [ ] Entendo o fluxo: user digita → setState → re-render

---

## 🚀 Deploy

Quando estiver pronto:

```bash
npm run build
```

A pasta `/dist` tem arquivos prontos para:
- Azure Static Web Apps
- Netlify
- Vercel
- GitHub Pages

---

**🎉 Parabéns! Você criou uma aplicação React completa!**

Qualquer dúvida, leia os comentários no código. Eles explicam TUDO! 📚
