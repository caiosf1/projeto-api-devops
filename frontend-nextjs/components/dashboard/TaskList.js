import { motion, AnimatePresence } from 'framer-motion';
import { FaTrash } from 'react-icons/fa';
import { Checkbox } from "@/components/ui/checkbox"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"

export function TaskList({ tarefas, loading, onDelete, onToggle }) {
  if (loading) {
    return (
      <div className="space-y-4">
        {[1, 2, 3].map((i) => (
          <div key={i} className="glass-card h-20 rounded-xl animate-pulse bg-white/5"></div>
        ))}
      </div>
    );
  }

  if (tarefas.length === 0) {
    return (
      <div className="text-center py-20 text-gray-400">
        <p className="text-xl">Nenhuma tarefa por enquanto 🎉</p>
        <p className="text-sm mt-2">Adicione uma nova tarefa acima para começar.</p>
      </div>
    );
  }

  const getPriorityBadge = (prioridade) => {
    switch(prioridade) {
      case 'alta': return <Badge variant="destructive" className="bg-red-500/20 text-red-300 hover:bg-red-500/30 border-red-500/50">Alta</Badge>;
      case 'media': return <Badge variant="secondary" className="bg-yellow-500/20 text-yellow-300 hover:bg-yellow-500/30 border-yellow-500/50">Média</Badge>;
      default: return <Badge variant="outline" className="bg-green-500/20 text-green-300 hover:bg-green-500/30 border-green-500/50">Baixa</Badge>;
    }
  }

  return (
    <div className="grid gap-4">
      <AnimatePresence mode="popLayout">
        {tarefas.map((tarefa) => (
          <motion.div
            key={tarefa.id}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 20 }}
            layout
            whileHover={{ scale: 1.01 }}
            className="relative group"
          >
            {/* Glow Effect on Hover */}
            <div className="absolute inset-0 bg-gradient-to-r from-purple-500/0 via-purple-500/10 to-blue-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-xl blur-xl -z-10"></div>

            <Card className={`p-4 flex justify-between items-center transition-all border-l-4 bg-white/5 border-white/10 hover:bg-white/10 backdrop-blur-md ${
              tarefa.concluida ? 'border-l-green-500 opacity-60' : 'border-l-purple-500 hover:border-l-purple-400'
            }`}>
              <div className="flex items-center gap-4">
                <Checkbox 
                  checked={tarefa.concluida}
                  onCheckedChange={() => onToggle(tarefa.id, tarefa.concluida)}
                  className="border-white/50 data-[state=checked]:bg-green-500 data-[state=checked]:border-green-500 w-6 h-6 transition-all duration-300"
                />
                <span className={`text-gray-200 text-lg transition-all duration-300 ${tarefa.concluida ? 'line-through text-gray-500' : 'group-hover:text-white'}`}>
                  {tarefa.descricao}
                </span>
                {getPriorityBadge(tarefa.prioridade)}
              </div>
              <Button
                variant="ghost"
                size="icon"
                onClick={() => onDelete(tarefa.id)}
                className="text-gray-500 hover:text-red-400 hover:bg-red-500/10 opacity-0 group-hover:opacity-100 transition-all duration-300 hover:scale-110"
              >
                <FaTrash />
              </Button>
            </Card>
          </motion.div>
        ))}
      </AnimatePresence>
    </div>
  );
}
