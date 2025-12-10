"use client";
import { useAuth } from '../../context/AuthContext';
import { useTarefas } from '../../hooks/useTarefas';
import { TaskForm } from '../../components/dashboard/TaskForm';
import { TaskList } from '../../components/dashboard/TaskList';

export default function Dashboard() {
  const { user } = useAuth();
  const { tarefas, loading, addTarefa, deleteTarefa, toggleTarefa } = useTarefas(user);

  return (
    <div className="space-y-6">
      <div className="bg-white/10 backdrop-blur-md rounded-2xl p-6 shadow-xl border border-white/10">
        <h2 className="text-2xl font-bold text-white mb-6 flex items-center gap-2">
          <span className="text-3xl">✨</span> Nova Tarefa
        </h2>
        <TaskForm onAdd={addTarefa} />
      </div>

      <div className="bg-white/10 backdrop-blur-md rounded-2xl p-6 shadow-xl border border-white/10">
        <h2 className="text-2xl font-bold text-white mb-6 flex items-center gap-2">
          <span className="text-3xl">📝</span> Suas Tarefas
        </h2>
        <TaskList 
          tarefas={tarefas} 
          loading={loading} 
          onDelete={deleteTarefa}
          onToggle={toggleTarefa}
        />
      </div>
    </div>
  );
}

