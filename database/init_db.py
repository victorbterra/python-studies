import sqlite3
from config import DB_PATH

def criar_tabela():
    print(f"🛠️ Criando/Resetando banco em: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS employees")

    sql = """
    CREATE TABLE employees (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        role TEXT NOT NULL,
        salary REAL NOT NULL,
        liquid_salary REAL NOT NULL
    )
    """

    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("Tabela 'Employees' criado com sucesso!")

if __name__ == '__main__':
    criar_tabela()