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
            print(f"ID:{employee.id:<4}\nNOME:{employee.name:<5}\nCARGO:{employee.role:<5}\nSAL.BRUTO:R${employee.salary}\nSAL.LIQUIDO:R${employee.liquid_salary:<7.2f}\nBÔNUS:R${employee.get_bonus()}\n")
            print("-"* 30)

def delete_employee(repository: EmployeeRepository):
    list_employees(repository)
    try:
        delete_id = int(input("Digite o id do funcionário para excluir: "))
        employee = repository.find_by_id(delete_id)
        if not employee:
            print("Funcionário não encontrado.")
            return
        confirm = input(f"Tem certeza que deseja excluir{employee.name}? (S/N):").upper()
        match confirm:
            case "S":
                repository.delete_by_id(delete_id)
            case "N":
                print("Operação cancelada!")
    except ValueError:
        print("ID inválido!")

def update_employee(repository: EmployeeRepository):
    list_employees(repository)
    try:
        update_id = int(input("\nDigite o ID do funcionário para editar:"))
        update_employee = repository.find_by_id(update_id)
        if not update_id:
            print("Funcionário não encontrado.")
            return
        print(f"\n --- EDITANDO:{update_employee.name}")
        print("Pressione [ENTER] para manter o valor atual")

        new_name = input(f"Digite o nome atualizado:[{update_employee.name}]:")
        new_age = input(f"Digite a Idade atualizada:[{update_employee.age}]")
        new_salary = input(f"Digite o salário atualizado:[{update_employee.salary}]")

        if new_name: update_employee.name = new_name
        if new_age: update_employee.age = new_age
        if new_salary:
            update_employee.salary = float(new_salary)
            update_employee.liquid_salary = update_employee._calc_liquid_salary()
        repository.save(update_employee)
    except ValueError:
        print("Erro de digitação.")

def main ():
    repository = EmployeeRepository()
    while True:
        header("SISTEMA DE CADASTRO DE FUNCIONÁRIOS")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Deletar Funcionario")
        print("4. Editar Funcionario")
        print("5. Sair")

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
                delete_employee(repository)
                wait_enter()
            case "4":
                update_employee(repository)
                wait_enter()
            case "5":
                print("\nSaindo do sistema... Até logo !")
                break
            case _:
                print("\n Opção inválida!")
                sleep(2)


if __name__ == "__main__":
    main()