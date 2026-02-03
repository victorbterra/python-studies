from employees import employees


ISENTION_LIMIT = 2000.0
LOW_TAX = 0.10
HIGH_TAX = 0.20

def create_user (name:str, salary:float)-> dict:
    return {"name": name, "salary": salary}


def calc_salary(value: float) -> float:
    if value < ISENTION_LIMIT :
        return value-(value * LOW_TAX)
    else:
        return value-(value * HIGH_TAX)


if __name__ == "__main__":

    while True:
        entry_name = input("Digite o nome do funcionário (ou 'sair' para fechar):")
        if entry_name.lower() == "sair": break

        entry_salary = input("Digite o salário do funcionário (ou 'sair' para fechar):")

        try:
            gross_salary = float(entry_salary)
            liquid_salary = calc_salary(gross_salary)
            employees.append(create_user(entry_name, liquid_salary))

            print(f"{entry_name}, o seu salário líquido será de: R${liquid_salary:.2f} ")

        except ValueError:
            print("Por favor, digite um número válido ex.: 2300.50")

    for employee in employees:
        print("========= LISTA DE FUNCIONÁRIOS =========")
        print(f"Nome: {employee['name']}\nSalário: R$ {employee['salary']:.2f}\n=====================")
