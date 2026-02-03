
isentionLimit = 2000.0
lowTax = 0.10
highTax = 0.20


def calc_salary(value: float) -> float:
    if value < isentionLimit :
        return value-(value * lowTax)
    else:
        return value-(value * highTax)




if __name__ == "__main__":

    entry_salary = input("DIGITE SEU SALÁRIO:")
    try:
        gross_salary = float(entry_salary)
        liquid_salary = calc_salary(gross_salary)
        print(f"o seu salário líquido será de: R${liquid_salary:.2f} ")
    except ValueError:
        print("Por favor, digite um número válido ex.: 2300.50")