import pyodbc
from random import choice

dados_de_conexao = (
    "Driver={SQLite3 ODBC Driver};"
    "Server=localhost;"
    "Database=Textos.db"
)

conexao = pyodbc.connect(dados_de_conexao)
cursor = conexao.cursor()

print(choice(list(cursor.execute("""SELECT Texto FROM DarkSouls WHERE Tema = 'Titulos' """)))[0])

cursor.close()
conexao.close()