import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "employees.db")

def criar_tabela():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        salary REAL INTEGER NOT NULL,
        role TEXT NOT NULL,
        liquid_salary REAL INTEGER NOT NULL
    )
    """

    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("Tabela 'Employees' criado com sucesso!")

if __name__ == '__main__':
    criar_tabela()