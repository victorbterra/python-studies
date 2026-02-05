from pydantic import BaseModel, PositiveFloat, PositiveInt, Field

class employee_schema(BaseModel):
    name: str = Field(
        min_length=3,
        description='O nome deve ter pelo menos 3 caracteres',
    )
    age: int = PositiveInt
    salary: float = PositiveFloat