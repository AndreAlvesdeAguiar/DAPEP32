import requests
import psycopg2
import json
import time

def consulta_api():
    try:
        # Faz a requisição à API
        response = requests.get("http://192.168.15.25/data")
        data = response.json()
        return data
    except Exception as e:
        print("Erro na consulta à API:", e)
        return None

def gravar_no_postgres(data):
    try:
        # Parâmetros de conexão ao banco de dados PostgreSQL
        dbname = 'my_database'
        user = 'postgres'
        password = 'minhasenha'
        host = 'db'  # Nome do serviço do banco de dados no docker-compose.yml
        
        # Estabelece uma conexão com o banco de dados
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        
        # Cria um cursor para executar comandos SQL
        cursor = conn.cursor()
        
        # Converte os dados para JSON
        json_data = json.dumps(data)
        
        # Insere os dados na tabela sensor_data
        cursor.execute("INSERT INTO sensor_data (data) VALUES (%s)", (json_data,))
        
        # Confirma a transação
        conn.commit()
        
        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()
        
        print("Dados gravados com sucesso no PostgreSQL.")
    except Exception as e:
        print("Erro ao gravar no PostgreSQL:", e)

if __name__ == "__main__":
    while True:
        data = consulta_api()
        if data:
            gravar_no_postgres(data)
        time.sleep(1)
