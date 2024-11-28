import sqlite3

conexao = sqlite3.connect("banco_de_dados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Matrícula TEXT NOT NULL,
    Notas REAL
)
""")

cursor.execute("SELECT * FROM Alunos")
for linha in cursor.fetchall():
    print(linha)
    
    
conexao.close()
