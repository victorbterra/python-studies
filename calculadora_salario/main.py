from models.employee import Employee
from repositories.employee_repository import EmployeeRepository

repository = EmployeeRepository()


if __name__ == "__main__":

    while True:

        entry_name = input("Digite o nome do funcionário (ou 'sair' para fechar):")
        if entry_name.lower() == "sair": break
        entry_age = int(input("Digite a idade do funcionário"))
        entry_salary = input("Digite o salário do funcionário (ou 'sair' para fechar):")

        try:
            gross_salary = float(entry_salary)
            new_employee = Employee(name=entry_name,age=entry_age, gross_salary=gross_salary)
            repository.save(new_employee)
            print(f"{new_employee.name}, o seu salário líquido será de: R${new_employee.liquid_salary:.2f} ")

        except ValueError:
            print("Por favor, digite um número válido ex.: 2300.50")
    print("========= LISTA DE FUNCIONÁRIOS =========")
    all_employees = repository.find_all()
    for employee in all_employees:
        print(f"Nome: {employee.name}\nIdade:{employee.age}\nSalário: R$ {employee.liquid_salary:.2f}\n=====================")
