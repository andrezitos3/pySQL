import pandas as pd
from pw import get_pw
from database import create_server_connection, create_database
from querys import query_create_database

connection = create_server_connection('localhost', 'root', get_pw())
create_database(connection, query_create_database)

