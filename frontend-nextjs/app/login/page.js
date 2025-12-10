"use client";
import { useState, useEffect } from 'react';
import { useAuth } from '../../context/AuthContext';
import Link from 'next/link';
import { motion } from 'framer-motion';
import { FaEnvelope, FaLock, FaSignInAlt } from 'react-icons/fa';
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { toast } from "sonner"

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [greeting, setGreeting] = useState('Bem-vindo!');
  const { login } = useAuth();

  useEffect(() => {
    const hasVisited = localStorage.getItem('hasVisited');
    if (hasVisited) {
      setGreeting('Bem-vindo de volta!');
    } else {
      localStorage.setItem('hasVisited', 'true');
      setGreeting('Bem-vindo!');
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);
    
    try {
      const success = await login(email, senha);
      if (!success) {
        setError('Falha no login. Verifique suas credenciais.');
        toast.error("Falha no login. Verifique suas credenciais.");
      } else {
        toast.success("Login realizado com sucesso!");
      }
    } catch (err) {
      setError('Erro de conexão. Tente novamente.');
      toast.error("Erro de conexão. Tente novamente.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center relative overflow-hidden">
      {/* Background Blobs */}
      <div className="blob bg-purple-600 w-96 h-96 rounded-full top-0 left-0 mix-blend-multiply filter blur-xl opacity-70 animate-blob"></div>
      <div className="blob bg-blue-600 w-96 h-96 rounded-full bottom-0 right-0 mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-2000"></div>

      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="w-full max-w-md relative z-10"
      >
        <Card className="glass border-white/10 bg-white/5 backdrop-blur-xl shadow-2xl shadow-purple-500/10">
          <CardHeader className="text-center">
            <CardTitle className="text-3xl font-bold text-white">{greeting}</CardTitle>
            <CardDescription className="text-gray-300">Acesse sua conta para gerenciar tarefas</CardDescription>
          </CardHeader>
          <CardContent>
            {error && (
              <motion.div 
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                className="p-4 mb-4 text-sm text-red-200 bg-red-500/20 border border-red-500/50 rounded-lg"
              >
                {error}
              </motion.div>
            )}

            <form className="space-y-6" onSubmit={handleSubmit}>
              <div className="space-y-2">
                <Label htmlFor="email" className="text-gray-200">Email</Label>
                <div className="relative group">
                  <FaEnvelope className="absolute top-1/2 left-3 transform -translate-y-1/2 text-gray-400 group-focus-within:text-purple-400 transition-colors z-10" />
                  <Input
                    id="email"
                    type="email"
                    placeholder="Seu email"
                    required
                    className="pl-10 glass-input h-12 text-white placeholder:text-gray-400 focus-visible:ring-purple-500 transition-all duration-300"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    disabled={isLoading}
                  />
                </div>
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="password" className="text-gray-200">Senha</Label>
                <div className="relative group">
                  <FaLock className="absolute top-1/2 left-3 transform -translate-y-1/2 text-gray-400 group-focus-within:text-purple-400 transition-colors z-10" />
                  <Input
                    id="password"
                    type="password"
                    placeholder="Sua senha"
                    required
                    className="pl-10 glass-input h-12 text-white placeholder:text-gray-400 focus-visible:ring-purple-500 transition-all duration-300"
                    value={senha}
                    onChange={(e) => setSenha(e.target.value)}
                    disabled={isLoading}
                  />
                </div>
              </div>

              <Button
                type="submit"
                disabled={isLoading}
                className="w-full h-12 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 text-white font-bold shadow-lg shadow-purple-500/25 hover:shadow-purple-500/40 hover:scale-[1.02] active:scale-[0.98] transition-all duration-300"
              >
                {isLoading ? (
                  <div className="animate-spin rounded-full h-5 w-5 border-t-2 border-b-2 border-white"></div>
                ) : (
                  <>
                    <FaSignInAlt className="mr-2" /> Entrar
                  </>
                )}
              </Button>
            </form>
          </CardContent>
          <CardFooter className="justify-center">
            <p className="text-gray-400 text-sm">
              Não tem uma conta?{' '}
              <Link href="/register" className="text-purple-400 hover:text-purple-300 font-semibold transition-colors">
                Registre-se
              </Link>
            </p>
          </CardFooter>
        </Card>
      </motion.div>
    </div>
  );
}

