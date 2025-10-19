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
    
    max_retries = 30  # 30 tentativas = ~2 minutos
    retry_interval = 5  # 5 segundos entre tentativas
    
    for attempt in range(1, max_retries + 1):
        try:
            # Tenta conectar
            conn = psycopg2.connect(**db_config, connect_timeout=10)
            conn.close()
            print(f"✅ PostgreSQL disponível após {attempt} tentativas!")
            return True
            
        except OperationalError as e:
            print(f"⏳ Tentativa {attempt}/{max_retries}: {str(e)[:100]}...")
            
            if attempt < max_retries:
                time.sleep(retry_interval)
            else:
                print(f"❌ PostgreSQL não disponível após {max_retries} tentativas!")
                return False
    
    return False

if __name__ == '__main__':
    import sys
    success = wait_for_postgres()
    sys.exit(0 if success else 1)