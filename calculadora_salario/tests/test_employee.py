import pytest
from calculadora_salario.models.employee import Employee

def test_low_salary_tax():
    new_employee = Employee(name="Junior", age=20, gross_salary=1000.0)

    result = new_employee.liquid_salary

    assert result == 900


def test_high_salary_tax():
    new_employee = Employee(name="Senor", age=30, gross_salary=3200.0)
    result = new_employee.liquid_salary

    assert result == 2560.0

