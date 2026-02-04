import os
import sys
from time import sleep

from models.employee import Employee
from repositories.employee_repository import EmployeeRepository

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_enter():
    input("\nPressione enter para continuar...")
    clean_screen()

def header(text: str):
    clean_screen()
    print("=" * 40)
    print(f"{text:^40}") # Texto Centralizado
    print("=" * 40)

def register_employee(repository: EmployeeRepository):
    header("NOVO CADASTRO")
    try:
        entry_name = input("Nome do funcionário:")
        if not entry_name:
            print("O nome não pode ser vazio")
            return
        entry_age = int(input("idade do funcionário: "))
        entry_salary = float(input("salário bruto do funcionário:"))
        new_employee = Employee(name=entry_name, age=entry_age, salary=entry_salary)
        repository.save(new_employee)
        print(f"O funcionário {new_employee.name} foi registrado com sucesso!")
        sleep(3)
    except ValueError:
        print("Erro: Digite números válidos para idade e salário.")
    except Exception as error:
        print(f"Erro inesperado:{error}")

def list_employees(repository: EmployeeRepository):
    header("LISTA DE FUNCIONÁRIOS")
    employee = repository.find_all()
    if not employee:
        print("Nenhum funcionário cadastrado.")
        return
    else:
        for employee in employee:
            print(f"Nome: {employee.name}\nIdade:{employee.age}\nSalário Bruto: R${employee.salary}\nSalário Líquido: R${employee.liquid_salary:.2f}\n=====================")

def main ():
    repository = EmployeeRepository()
    while True:
        header("SISTEMA DE CADASTRO DE FUNCIONÁRIOS")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")
        print("-" * 40)
        option = input("Escolha uma opção:")

        match option:
            case "1":
                register_employee(repository)
                wait_enter()
            case "2":
                list_employees(repository)
                wait_enter()
            case "3":
                print("\nSaindo do sistema... Até logo !")
                break
            case _:
                print("\n Opção inválida!")
                sleep(2)


if __name__ == "__main__":
    main()