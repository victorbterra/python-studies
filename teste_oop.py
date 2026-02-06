from models.employee import Employee
from models.manager import Manager

func = Employee(name="João", age=20, salary=1700)

boss = Manager(name="Ana", age=38, salary=5700)

equipe = [func,boss]

print("=== FOLHA DE BÔNUS ===")

for funcionario in equipe:

    bonus = funcionario.get_bonus()
    tipo = type(funcionario).__name__
    print(f"Cargo:{tipo} | Nome:{funcionario.name} | Bonus:{bonus:.2f}")