from models.employee import Employee
from repositories.employee_repository import EmployeeRepository

print("1. Instanciando Repositório...")
repo = EmployeeRepository()

print("2. Criando Funcionário Falso...")
# Note o uso de um UUID fixo ou gerado na hora
emp = Employee(name="Teste Debug", age=30, salary=5000.0)

print(f"3. Tentando Salvar (ID: {emp.id})...")
try:
    repo.create(emp)
    print("✅ Sucesso no Python! Verifique o arquivo do banco agora.")
except Exception as e:
    print(f"❌ ERRO AO SALVAR: {e}")

print("4. Tentando ler de volta...")
buscado = repo.find_by_id(emp.id)
if buscado:
    print(f"✅ O dado VOLTOU do banco: {buscado.name}")
else:
    print("❌ O dado NÃO VOLTOU (Perdido no limbo).")