import pymongo
import time
import json
import sys

def db_connect():
    try:
        client_mongo = pymongo.MongoClient("$STRING_CONNECTION")
    except pymongo.errors.ConfigurationError:
        print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
        sys.exit(1)
    db = client_mongo.tcc
    return(db)

def insercao():
    deployments_collection = db_connect()["automovel"]
    with open('db/INSERT-automovel-50k.json') as file:
        data = json.load(file)
    inicio = time.time()
    result = deployments_collection.insert_many(data)
    fim = time.time()
    tempo_decorrido = (fim - inicio)
    print("Tempo de inserção (seg): " + str(tempo_decorrido))

def exclusao():
    tcc_collection = db_connect()["automovel"]
    inicio = time.time()
    tcc_collection.delete_many({})
    fim = time.time()
    tempo_decorrido = (fim - inicio)
    print("Tempo de exclusão (seg): " + str(tempo_decorrido))

def consulta():
    tcc_collection = db_connect()["automovel"]
    inicio = time.time()
    a = tcc_collection.find_one({ 'numero_serie': "WBAPN7C57BA255822"})
    fim = time.time()
    tempo_decorrido = (fim - inicio)
    print("Tempo de busca (seg): " + str(tempo_decorrido))

#consulta()
#insercao()
#exclusao()