import psycopg2

conn = psycopg2.connect(
    dbname="castrobrinquedos",
    user="postgres",
    password="1234",
    host="localhost",
    port=5432
)
print("Conectado com sucesso!")
print(conn)


import os
print(repr(os.getenv("db_username")))
print(repr(os.getenv("db_password")))
print(repr(os.getenv("db_host")))
print(repr(os.getenv("db_schema")))
