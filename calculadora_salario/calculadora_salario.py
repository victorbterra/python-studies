from mock.employees import employees
from services.user_service import create_user
from services.salary_service import calc_salary
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

        entry_salary = input("Digite o salário do funcionário (ou 'sair' para fechar):")

        try:
            gross_salary = float(entry_salary)
            liquid_salary = calc_salary(gross_salary)
            employees.append(create_user(entry_name, round(liquid_salary ,2)))

            with open(data_base, "w") as file:
                json.dump(employees, file, indent=4, ensure_ascii=False)

            print(f"{entry_name}, o seu salário líquido será de: R${liquid_salary:.2f} ")

        except ValueError:
            print("Por favor, digite um número válido ex.: 2300.50")
    print("========= LISTA DE FUNCIONÁRIOS =========")
    for employee in employees:
        print(f"Nome: {employee['name']}\nSalário: R$ {employee['salary']:.2f}\n=====================")
