import time
import json
import sys
import psycopg2
from psycopg2.extras import Json 

def insercao():
    conn = psycopg2.connect(host='$host', dbname='$database', user='$user', password='$password')
    cur = conn.cursor()
    data = open('INSERT-automovel-50k.sql','r')
    sqlFile = data.read()
    data.close()
    sqlCommands = sqlFile.split(';')
    inicio = time.time()
    for command in sqlCommands:
        try:
            cur.execute(command)
            conn.commit()
        except:
            print("Error")
            # print("Command skipped: ")
    conn.commit()
    fim = time.time()
    tempo_decorrido = (fim - inicio)
    print("Tempo de inserção (seg): " + str(tempo_decorrido))
    cur.close()
    conn.close()
    
def exclusao():
    conn = psycopg2.connect(host='$host', dbname='$database', user='$user', password='$password')
    cur = conn.cursor()
    inicio = time.time()
    cur.execute("TRUNCATE TABLE tcc.veiculo")
    conn.commit()
    fim = time.time()
    tempo_decorrido = (fim - inicio)
    print("Tempo de inserção (seg): " + str(tempo_decorrido))
    cur.close()
    print("Deletado com sucesso")

def consulta():
    conn = psycopg2.connect(host='$host', dbname='$database', user='$user', password='$password')
    cur = conn.cursor()
    inicio = time.time()
    cur.execute("SELECT * FROM tcc.veiculo WHERE marca = 'Toyota'")
    print(cur)
    conn.commit()
    fim = time.time()
    tempo_decorrido = (fim - inicio)
    print("Tempo de busca (seg): " + str(tempo_decorrido))
    cur.close()

consulta()
#insercao()
#exclusao()
