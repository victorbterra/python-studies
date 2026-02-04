from calculadora_salario.models.employee import Employee
import sqlite3

class EmployeeRepository:
    def __init__(self):
        self.db_path = "./database/employees.db"

    # metodo para iniciar leitura dos dados do json
    """def _load_file(self):
        try:
            with open(self.db_path, "r") as file:
                content = json.load(file)
                if not isinstance(content, list):
                    return []
                return content
        except (FileNotFoundError, json.JSONDecodeError):
            return [] """

    # metodo para salvar dados dentro do json
    def save(self, employee: Employee) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = """
              INSERT INTO employees (name,age,salary,liquid_salary) VALUES (?,?,?,?)
              """
        cursor.execute(sql, (employee.name, employee.age, employee.salary, employee.liquid_salary))
        conn.commit()
        conn.close()

    # metodo para listar todos os usuários do json
    def find_all(self) -> list[Employee]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name, age, salary,liquid_salary FROM employees")
        lines = cursor.fetchall()
        conn.close()

        employees_objects = []
        for line in lines:
            emp = Employee(name=line[0],age=line[1], salary=line[2])
            employees_objects.append(emp)

        return employees_objects