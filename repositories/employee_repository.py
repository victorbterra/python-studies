from models.employee import Employee
import sqlite3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import DB_PATH


class EmployeeRepository:
    def __init__(self):
        self.db_path = DB_PATH

    # metodo para salvar dados dentro do banco de dados
    def create(self, employee: Employee) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
            INSERT INTO employees (id,name,age,role,salary,liquid_salary) VALUES (?,?,?,?,?,?)
        """
        role = type(employee).__name__
        cursor.execute(sql, (employee.id,employee.name,employee.age,role,employee.salary,employee.liquid_salary))
        conn.commit()
        conn.close()

    # método para atualizar dados
    def update(self, employee: Employee):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
        UPDATE employees
        SET name=?, age = ?,role = ?, salary = ?
        WHERE id = ?
        """
        role = type(employee).__name__
        cursor.execute(sql,(
            employee.name,
            employee.age,
            role,
            employee.salary,
            employee.id
        ))
        conn.commit()
        conn.close()

    # metodo para deletar usuário dentro do banco de dados
    def delete_by_id(self, id: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = ?",(id,))
        conn.commit()
        conn.close()

    # metodo para encontrar um único usuário
    def find_by_id(self, id: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
            SELECT id, name,age,role,salary,liquid_salary 
            FROM employees WHERE id = ?
        """
        cursor.execute(sql, (id,))
        employee = cursor.fetchone()
        conn.close()
        if employee:
            return self._mount_object(employee)
        return None

    # metodo para listar todos os usuários do banco de dados
    def find_all(self) -> list[Employee]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
        """
        SELECT id,name,age,role,salary,liquid_salary 
        FROM employees
        """)
        lines = cursor.fetchall()
        conn.close()
        return [self._mount_object(line) for line in lines]

    def _mount_object(self,employee):
        id,name,age,role,salary,liquid_salary = employee

        try:
            salary = float(salary)
        except ValueError:
            salary = 0.0

        from models.manager import Manager
        from models.employee import Employee

        if role == "Manager":
            emp = Manager(id=id,name=name, age=age, salary=salary)
        else:
            emp = Employee(id=id,name=name, age=age, salary=salary)

        emp.liquid_salary = liquid_salary

        return emp