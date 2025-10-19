#!/usr/bin/env python3
"""
Script para aguardar PostgreSQL ficar disponível antes de iniciar a aplicação.
Usado em Container Apps para garantir que DB está pronto.
"""

import os
import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_postgres():
    """Aguarda PostgreSQL ficar disponível."""
    
    # Configurações do banco (mesmas que config.py)
    db_config = {
        'host': os.getenv('POSTGRES_SERVER', 'localhost'),
        'user': os.getenv('POSTGRES_USER', 'postgres'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'database': os.getenv('POSTGRES_DB', 'apitodo'),
        'port': os.getenv('POSTGRES_PORT', '5432')
    }
    
    if not db_config['password']:
        print("❌ POSTGRES_PASSWORD não definida!")
        return False
    
    print(f"🔄 Aguardando PostgreSQL em {db_config['host']}:{db_config['port']}...")
    
    max_retries = 60  # 60 tentativas = ~10 minutos (para Container Apps)
    retry_interval = 10  # 10 segundos entre tentativas
    
    for attempt in range(1, max_retries + 1):
        try:
            # Tenta conectar com timeout maior para Container Apps
            conn = psycopg2.connect(**db_config, connect_timeout=30)
            
            # Testa se a conexão realmente funciona
            cursor = conn.cursor()
            cursor.execute('SELECT 1')
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if result:
                print(f"✅ PostgreSQL disponível e funcionando após {attempt} tentativas!")
                return True
            
        except OperationalError as e:
            error_msg = str(e)
            print(f"⏳ Tentativa {attempt}/{max_retries}: {error_msg[:150]}...")
            
            # Se for erro de timeout, aguarda mais
            if "timeout" in error_msg.lower():
                print("   🕐 Timeout detectado - aguardando mais tempo...")
                time.sleep(retry_interval * 2)  # Aguarda dobrado em caso de timeout
            elif "connection refused" in error_msg.lower():
                print("   🔌 Conexão recusada - serviço pode estar iniciando...")
                time.sleep(retry_interval)
            else:
                time.sleep(retry_interval)
                
        except Exception as e:
            print(f"⚠️  Erro inesperado na tentativa {attempt}: {str(e)[:100]}...")
            time.sleep(retry_interval)
    
    print(f"❌ PostgreSQL não disponível após {max_retries} tentativas ({max_retries * retry_interval / 60:.1f} minutos)!")
    print("💡 Sugestão: Considere usar Azure Database for PostgreSQL para maior confiabilidade.")
    return False
    
    return False

if __name__ == '__main__':
    import sys
    success = wait_for_postgres()
    sys.exit(0 if success else 1)