from pydantic import BaseModel, PositiveFloat, PositiveInt, Field

class EmployeeSchema(BaseModel):
    name: str = Field(
        min_length=3,
        description='O nome deve ter pelo menos 3 caracteres',
    )
    age: int = Field(
        ge=18,
        le=100,
        description='O funcionário precisa ser maior de idade.',
    )
    salary: float = PositiveFloat