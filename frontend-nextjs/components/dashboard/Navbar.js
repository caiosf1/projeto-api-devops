import { motion } from 'framer-motion';
import { FaTasks, FaSignOutAlt } from 'react-icons/fa';
import { Button } from "@/components/ui/button"

export function Navbar({ user, onLogout }) {
  return (
    <nav className="floating-navbar sticky top-0 z-50 transition-all duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex items-center gap-3"
          >
            <div className="bg-gradient-to-r from-purple-500 to-blue-500 p-2 rounded-lg shadow-lg shadow-purple-500/20">
              <FaTasks className="text-white text-xl" />
            </div>
            <h1 className="text-xl font-bold text-white tracking-wide">
              TaskMaster
            </h1>
          </motion.div>
          
          <motion.div 
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex items-center gap-4"
          >
            <span className="text-gray-300 text-sm hidden sm:block font-medium">{user?.email}</span>
            <Button 
              variant="destructive"
              size="sm"
              onClick={onLogout} 
              className="flex items-center gap-2 bg-red-500/10 text-red-400 hover:bg-red-500/20 border border-red-500/20 hover:shadow-[0_0_15px_rgba(239,68,68,0.2)] transition-all duration-300"
            >
              <FaSignOutAlt /> <span className="hidden sm:inline">Sair</span>
            </Button>
          </motion.div>
        </div>
      </div>
    </nav>
  );
}
