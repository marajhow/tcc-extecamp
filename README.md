
# Aplicação de teste entre Postgres x MongoDB

Uso exclusivo para replicação dos testes no TCC do curso de Engenharia e Administração de Sistemas de Banco de Dados da Extecamp - Unicamp

## Instalação

#### Python
Para execução dessa aplicação, é necessário ter instalado na máquina que irá rodar o teste o Python3.

Caso ainda não tenha instalado em seu equipamento, siga abaixo:

#### Windows

https://python.org.br/instalacao-windows/

#### Ubuntu

https://python.org.br/instalacao-linux/

#### MAC

https://python.org.br/instalacao-mac/

### Bibliotecas

Toda biblioteca necessária já se encontra dentro do arquivo requirements.txt, com isso, basta rodar o comando abaixo para instalar:
```
pip3 install -r requirements.txt
```

## Configuração

Como a bse de teste faz referência a uma conexão interna nos teste, a mesma deverá ser personalização para que seja direcionada ao seu banco de dados. No arquivo mongodb.py, a função de conexão deve ser alterada onde se tem $STRING_CONNECTION pela string de conexão com o seu banco MongoDB:

```
def db_connect():
    try:
        client_mongo = pymongo.MongoClient("$STRING_CONNECTION")
    except pymongo.errors.ConfigurationError:
        print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
        sys.exit(1)
    db = client_mongo.tcc
    return(db)
```

O mesmo acontece para o arquivo postgres.py, porém esse será divido em 
$host,$database, $user, $password:

```
def db_connect():
    try:
        client_postgres = psycopg2.connect(host=$host, dbname=$database, user=$user, password=$password)
    except psycopg2.errors.Error as e:
        print(e)
        sys.exit(1)
    return(client_postgres)
```

Realizado esses ajustes na conexão a aplicação está apta a ser executada.

## Execução

Para executar as operações, basta descomentar a função desejada que já estão listadas ao fim de cada script, e para executar utilizar o comanda:

```
python3 mongodb.py
```

ou 

```
python3 postgres.py
```