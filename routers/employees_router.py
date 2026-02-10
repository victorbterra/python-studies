from fastapi import APIRouter,Depends, HTTPException, status
from typing import List
from DTO.employeeDTO import EmployeeDTO, EmployeeResponseDTO
from models.employee import Employee
from models.manager import Manager
from repositories.employee_repository import EmployeeRepository


router = APIRouter(prefix="/employees", tags=["Employees"])

def get_repo():
    return EmployeeRepository()

@router.get("/",response_model=List[EmployeeResponseDTO])
def list_employees(repo: EmployeeRepository = Depends(get_repo)):
    return repo.find_all()

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=EmployeeResponseDTO)
def create_employee(data:EmployeeDTO,repo:EmployeeRepository = Depends(get_repo)):
    if data.role == "Manager":
        new_employee = Manager(name=data.name,age=data.age,salary=data.salary)
    else:
        new_employee = Employee(name=data.name,age=data.age,salary=data.salary)

    repo.create(new_employee)
    return new_employee

@router.put("/{employee_id}",response_model=EmployeeResponseDTO)
def update_employee(employee_id:str,data:EmployeeDTO,repo:EmployeeRepository= Depends(get_repo)):

    current_employee = repo.find_by_id(employee_id)

    if not current_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Funcionário com ID {employee_id} não encontrado.")
    
    #Atualizando os dados
    current_employee.name = data.name
    current_employee.age = data.age
    current_employee.salary = data.salary

    #Recalculo dos impostos
    current_employee.liquid_salary = current_employee._calc_liquid_salary()

    #salva no banco de dados
    repo.update(current_employee)

    return current_employee

@router.delete("/{employee_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id:str,repo:EmployeeRepository = Depends(get_repo)):
    #pegando o id do funcionário no banco de dados
    emp = repo.find_by_id(employee_id)

    #caso o id não exista no banco de dados
    if not emp:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Funcionário não encontrado."
    )

    #deletar o usuário
    repo.delete_by_id(employee_id)
    return