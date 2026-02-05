import os
from time import sleep
from DTO.employeeDTO import EmployeeDTO
from models.employee import Employee
from models.manager import Manager
from repositories.employee_repository import EmployeeRepository
from pydantic import ValidationError


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
        # Pegar os dados brutos do usuário
        entry_name = input("Nome do funcionário:")
        entry_age = input("idade do funcionário: ")
        entry_salary = input("salário bruto do funcionário:")

        #Validação dos dados com o pydantic
        validate_data = EmployeeDTO(
                name= entry_name,
                age= entry_age,
                salary= entry_salary
            )
        #Escolha do cargo
        print("Qual o cargo?")
        print("1 - Funcionário Comum")
        print("2 - Gerente")
        option_role = int(input("Opção: "))

        if option_role == 1:
            new_employee = Employee(validate_data.name, validate_data.age, validate_data.salary)
        else:
            new_employee = Manager(validate_data.name, validate_data.age, validate_data.salary)

        #Aplicação da regra de negócios e cria usuário no banco de dados
        repository.save(new_employee)
        #mensagem de sucesso ao usuário !
        print(f"O {new_employee.role()} {new_employee.name} foi registrado com sucesso!")
        sleep(1)
    except ValidationError as error:
        print("Erro de validação: ")
        for error in error.errors():
            print(f"-> Campo '{error['loc'][0]}': {error['msg']}")
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
            print(f"Nome: {employee.name}\nIdade: {employee.age}\nCargo: {employee.role()}\nBonus: R${employee.get_bonus()}\nSalário Bruto: R${employee.salary}\nSalário Líquido: R${employee.liquid_salary:.2f}\n=====================")

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