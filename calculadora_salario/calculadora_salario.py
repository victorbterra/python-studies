from employees import employees


isentionLimit = 2000.0
lowTax = 0.10
highTax = 0.20



def calc_salary(value: float) -> float:
    if value < isentionLimit :
        return value-(value * lowTax)
    else:
        return value-(value * highTax)

def add_employee():
    new_employee = {
        "name": entry_name,
        "salary": liquid_salary,
    }
    return new_employee


if __name__ == "__main__":

    while True:
        entry_name = input("Digite o nome do funcionário (ou 'sair' para fechar):")
        if entry_name.lower() == "sair": break

        entry_salary = input("Digite o salário do funcionário (ou 'sair' para fechar):")

        try:
            gross_salary = float(entry_salary)
            liquid_salary = calc_salary(gross_salary)
            employees.append(add_employee())

            print(f"{entry_name}, o seu salário líquido será de: R${liquid_salary:.2f} ")

        except ValueError:
            print("Por favor, digite um número válido ex.: 2300.50")

    for employee in employees:
        print(f"Nome: {employee['name']}\nSalário: R$ {employee['salary']:.2f}")
