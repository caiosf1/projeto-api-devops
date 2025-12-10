"use client";

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '../../context/AuthContext';
import { Navbar } from '../../components/dashboard/Navbar';

export default function DashboardLayout({ children }) {
  const { user, loading, logout } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !user) {
      router.push('/login');
    }
  }, [user, loading, router]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!user) {
    return null; // Evita flash de conteúdo antes do redirect
  }

  return (
    <div className="min-h-screen bg-gray-900 relative overflow-hidden text-white">
      {/* Background Blobs */}
      <div className="blob bg-purple-600 w-[800px] h-[800px] rounded-full -top-40 -left-40 mix-blend-multiply filter blur-3xl opacity-20 fixed pointer-events-none animate-blob"></div>
      <div className="blob bg-blue-600 w-[600px] h-[600px] rounded-full bottom-0 right-0 mix-blend-multiply filter blur-3xl opacity-20 fixed pointer-events-none animate-blob animation-delay-2000"></div>

      <div className="relative z-10">
        <Navbar user={user} onLogout={logout} />
        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          {children}
        </main>
      </div>
    </div>
  );
}