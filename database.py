import mysql.connector
from mysql.connector import Error

# essa funcao cria a conexao com o servidor MySQL
def create_server_connection(hostName, userName, userPassword):

    # encerrar conexao com o servidor para nao dar conflito
    connection = None

    try:
        connection = mysql.connector.connect(
            host=hostName,
            user=userName,
            password=userPassword
        )
        print('conexão com MySQL efetuada com sucesso')
    except Error as err:
        print(f'Error: {err}')
    
    return connection

# essa funcao cria a conexao com uma base de dados especifica do servidor
def create_db_connection(hostName, userName, userPassword,dbName):

    # encerrar conexao com o servidor para nao dar conflito
    connection = None

    try:
        connection = mysql.connector.connect(
            host=hostName,
            user=userName,
            password=userPassword,
            db=dbName
        )
        print('conexão com MySQL efetuada com sucesso')
    except Error as err:
        print(f'Error: {err}')
    
    return connection

# essa funcao cria a base de dados e recebe o argumento de objeto de conexao, e uma consulta
# a consulta (query) é o código em SQL 
def create_database(connection, query):
    
    # criando o objeto cursor para herdar propriedades e métodos úteis
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print('base de dados criada com sucesso')
    except Error as err:
        print(f'Error: {err}')

# essa funcao executa a consulta 
def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        # os comandos especificos SQL serao implementados
        connection.commit()
        ('consulta realizada com sucesso')
    except Error as err:
        (f'Error: {err}')

