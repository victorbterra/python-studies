from models.employee import Employee
from models.manager import Manager
import sqlite3


class EmployeeRepository:
    def __init__(self):
        self.db_path = "./database/employees.db"


    def save(self, employee:Employee):
        if employee.id:
            self._update(employee)
        else:
            self._create(employee)

    # metodo para salvar dados dentro do banco de dados
    def _create(self, employee: Employee) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
              INSERT INTO employees (name,age,salary,role,liquid_salary) VALUES (?,?,?,?,?)
              """
        role = type(employee).__name__
        cursor.execute(sql, (employee.name, employee.age, employee.salary,role, employee.liquid_salary))
        conn.commit()
        conn.close()

    # método para atualizar dados
    def _update(self, employee: Employee):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
        UPDATE employees
        SET name=?, age = ?, salary = ?, role = ?, liquid_salary = ?
        WHERE id = ?
        """
        cargo = type(employee).__name__
        cursor.execute(sql,(employee.name,employee.age,employee.salary,cargo,employee.id))
        conn.commit()
        conn.close()

    # metodo para deletar usuário dentro do banco de dados
    def delete_by_id(self, id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = ?",(id,))
        conn.commit()
        conn.close()

    # metodo para encontrar um único usuário
    def find_by_id(self, id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = ?",(id,))
        employee = cursor.fetchone()
        conn.close()
        if employee:
            return self._mount_object(employee)
        return None

    # metodo para listar todos os usuários do banco de dados
    def find_all(self) -> list[Employee]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name,age,salary,role,id FROM employees")
        lines = cursor.fetchall()
        conn.close()
        return [self._mount_object(line) for line in lines]

    def _mount_object(self,employee):
        name, age,salary,role,db_id = employee

        from models.manager import Manager
        from models.employee import Employee

        if role == "Manager":
            emp = Manager(name=name, age=age, salary=salary, id=db_id)
        else:
            emp = Employee(name=name, age=age, salary=salary,id=db_id)
        return emp