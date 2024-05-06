import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'clientes.sqlite')

cur = con.cursor()
cur.row_factory = sqlite3.Row

def criar_tabela (conexao,cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

def inserir_registro(conexao,cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao,cursor, nome , email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def excluir_registro(conexao,cursor,  id):
    data = (id ,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_muitos_registros(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,) )
    return cursor.fetchone() 

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome ;")

cliente = recuperar_cliente(cur, 2)
print(dict(cliente))

clientes = listar_clientes(cur)
for cliente in clientes:
    print(dict(cliente))

# dados = [
#     ("Guilherme", "guilherme@gmail.com"),
#     ("Antonio", "antonio@gmail.com"),
#     ("Giovana", "giovana@gmail.com"),
# ]

# inserir_muitos_registros(con, cur, dados)
