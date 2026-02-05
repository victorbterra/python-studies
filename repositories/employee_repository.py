from models.employee import Employee
from models.manager import Manager
import sqlite3


class EmployeeRepository:
    def __init__(self):
        self.db_path = "./database/employees.db"

    # metodo para salvar dados dentro do banco de dados
    def save(self, employee: Employee) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
              INSERT INTO employees (name,age,salary,role,liquid_salary) VALUES (?,?,?,?,?)
              """
        role = type(employee).__name__
        cursor.execute(sql, (employee.name, employee.age, employee.salary,role, employee.liquid_salary))
        conn.commit()
        conn.close()

    # metodo para listar todos os usuários do banco de dados
    def find_all(self) -> list[Employee]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name,age,salary,role,liquid_salary FROM employees")
        lines = cursor.fetchall()
        conn.close()

        employees_objects = []
        for line in lines:
            name, age,salary,role,liquid_salary = line
            if role == "Manager":
                emp = Manager(name=name, age=age, salary=salary)
            else:
                emp = Employee(name=name, age=age, salary=salary)

            employees_objects.append(emp)

        return employees_objects