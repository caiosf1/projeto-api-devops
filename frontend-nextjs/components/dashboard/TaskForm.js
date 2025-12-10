import { useState } from 'react';
import { motion } from 'framer-motion';
import { FaPlus } from 'react-icons/fa';
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { toast } from "sonner"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

export function TaskForm({ onAdd }) {
  const [novaTarefa, setNovaTarefa] = useState('');
  const [prioridade, setPrioridade] = useState('media');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!novaTarefa.trim()) return;
    
    const result = await onAdd(novaTarefa, prioridade);
    if (result.success) {
      toast.success("Tarefa adicionada com sucesso!")
      setNovaTarefa('');
      setPrioridade('media');
    } else {
      toast.error("Erro ao adicionar tarefa.")
    }
  };

  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="glass-card rounded-2xl p-6 mb-8 relative overflow-hidden group"
    >
      {/* Ambient Glow Effect */}
      <div className="absolute -top-20 -right-20 w-40 h-40 bg-purple-500/20 rounded-full blur-3xl group-hover:bg-purple-500/30 transition-all duration-500"></div>
      
      <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4 relative z-10">
        <div className="flex-1 flex gap-2">
            <Input
              type="text"
              value={novaTarefa}
              onChange={(e) => setNovaTarefa(e.target.value)}
              placeholder="O que você precisa fazer hoje?"
              className="flex-1 glass-input h-14 text-lg rounded-xl border-white/10 focus-visible:ring-purple-500 focus-visible:border-purple-500/50 transition-all duration-300"
            />
            
            <Select value={prioridade} onValueChange={setPrioridade}>
              <SelectTrigger className="w-[120px] h-14 glass-input rounded-xl border-white/10 focus:ring-purple-500 focus:border-purple-500/50 transition-all duration-300">
                <SelectValue placeholder="Prioridade" />
              </SelectTrigger>
              <SelectContent className="glass border-white/10 bg-slate-900/90 backdrop-blur-xl">
                <SelectItem value="baixa" className="text-green-400 focus:bg-green-500/20 focus:text-green-300 cursor-pointer">Baixa</SelectItem>
                <SelectItem value="media" className="text-yellow-400 focus:bg-yellow-500/20 focus:text-yellow-300 cursor-pointer">Média</SelectItem>
                <SelectItem value="alta" className="text-red-400 focus:bg-red-500/20 focus:text-red-300 cursor-pointer">Alta</SelectItem>
              </SelectContent>
            </Select>
        </div>
        
        <Button
          type="submit"
          disabled={!novaTarefa.trim()}
          className="h-14 px-8 rounded-xl bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 text-white font-bold shadow-lg shadow-purple-500/25 hover:shadow-purple-500/40 hover:scale-[1.02] active:scale-[0.98] transition-all duration-300"
        >
          <FaPlus className="mr-2" /> <span className="hidden sm:inline">Adicionar</span>
        </Button>
      </form>
    </motion.div>
  );
}
