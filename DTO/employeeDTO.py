from pydantic import BaseModel, Field

SALARIO_MINIMO_PISO = 1621
TETO_SALARIAL = 13054.97


class EmployeeDTO(BaseModel):
    name: str = Field(
        min_length=3,
        description='O nome deve ter pelo menos 3 caracteres',
    )
    age: int = Field(
        ge=18,
        le=100,
        description='O funcionário precisa ser maior de idade.',
    )
    salary: float = Field(
        ge=SALARIO_MINIMO_PISO,
        le=TETO_SALARIAL,
        description=f"Salário entre R${SALARIO_MINIMO_PISO} e R${TETO_SALARIAL}"
    )