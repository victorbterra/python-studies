from mock.employees import employees
from services.user_service import create_user
from models.employee import Employee
import json


data_base = "./mock/db.json"

try:
    with open(data_base, "r") as file:
        employees = json.load(file)
except FileNotFoundError:
    employees = []

if __name__ == "__main__":

    while True:

        entry_name = input("Digite o nome do funcionário (ou 'sair' para fechar):")
        if entry_name.lower() == "sair": break
        entry_age = int(input("Digite a idade do funcionário"))
        entry_salary = input("Digite o salário do funcionário (ou 'sair' para fechar):")

        try:
            gross_salary = float(entry_salary)
            new_employee = Employee(name=entry_name,age=entry_age, gross_salary=gross_salary)
            employees.append(new_employee.toDict())

            with open(data_base, "w") as file:
                json.dump(employees, file, indent=4, ensure_ascii=False)

            print(f"{new_employee.name}, o seu salário líquido será de: R${new_employee.liquid_salary:.2f} ")

        except ValueError:
            print("Por favor, digite um número válido ex.: 2300.50")
    print("========= LISTA DE FUNCIONÁRIOS =========")
    for employee in employees:
        print(f"Nome: {employee['name']}\nIdade:{employee['age']}\nSalário: R$ {employee['liquid_salary']:.2f}\n=====================")
