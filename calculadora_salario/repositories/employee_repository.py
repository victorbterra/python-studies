import json
from calculadora_salario.models.employee import Employee

class EmployeeRepository:
    def __init__(self, db_path:str ="./mock/db.json"):
        self.db_path = db_path

    # metodo para iniciar leitura dos dados do json
    def _load_file(self):
        try:
            with open(self.db_path, "r") as file:
                content = json.load(file)
                if not isinstance(content, list):
                    return []
                return content
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # metodo para salvar dados dentro do json
    def save(self, employee: Employee) -> list:
        current_data = self._load_file()
        current_data.append(employee.toDict())
        with open(self.db_path, "w") as file:
            json.dump(current_data, file, indent=4, ensure_ascii=False)

    # metodo para listar todos os usuários do json
    def find_all(self) -> list[Employee]:
        data_dicts = self._load_file()

        employees_objects = []
        for item in data_dicts:
            emp = Employee(item['name'], item['age'], item['liquid_salary'])
            employees_objects.append(emp)

        return employees_objects