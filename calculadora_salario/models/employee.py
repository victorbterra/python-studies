class Employee:
    def __init__(self, name:str, age:int, gross_salary:float):
        self.name = name
        self.age = age
        self.gross_salary = gross_salary
        self.liquid_salary = self._calc_liquid_salary()

    def _calc_liquid_salary(self) -> float:
        ISENTION_LIMIT = 2000.0
        LOW_TAX = 0.10
        HIGH_TAX = 0.20

        if self.gross_salary < ISENTION_LIMIT:
            return self.gross_salary - (self.gross_salary * LOW_TAX)
        else:
            return self.gross_salary - (self.gross_salary * HIGH_TAX)


    def toDict(self)->dict:
        return {
            'name':self.name,
            'age':self.age,
            'liquid_salary':self.liquid_salary,
        }