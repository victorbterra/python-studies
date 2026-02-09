from fastapi import APIRouter
from DTO.employeeDTO import EmployeeDTO


router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/")
def create_employee(employee:EmployeeDTO):
    return{
        "msg":f"{employee.name} Castrado!"
    }

@router.get("/")
def list_employee():
    return[
        {
            "name":"Teste",
            "role":"Dev"
        }
    ] 


