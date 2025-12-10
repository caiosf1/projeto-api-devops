import { Inter } from 'next/font/google'
import './globals.css'
import { AuthProvider } from '../context/AuthContext'
import { Toaster } from "@/components/ui/sonner"
import Script from 'next/script'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Gerenciador de Tarefas',
  description: 'App Fullstack com Next.js e Flask',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <Script id="redirect-to-www" strategy="beforeInteractive">
          {`
            if (typeof window !== 'undefined' && window.location.hostname === 'caiodev.me') {
              window.location.replace('https://www.caiodev.me' + window.location.pathname + window.location.search);
            }
          `}
        </Script>
        <AuthProvider>
          {children}
          <Toaster />
        </AuthProvider>
      </body>
    </html>
  )
}
