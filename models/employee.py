import uuid

class Employee:
    def __init__(self, name:str, age:int,salary:float, id:str=None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.age = age
        self.salary = salary
        self.liquid_salary = self._calc_liquid_salary()

    def _calc_liquid_salary(self) -> float:
        ISENTION_LIMIT = 2000.0
        LOW_TAX = 0.10
        HIGH_TAX = 0.20

        if self.salary < ISENTION_LIMIT:
            return self.salary - (self.salary * LOW_TAX)
        else:
            return self.salary - (self.salary * HIGH_TAX)

    def get_bonus(self)->float:
        return 0.0

    @property
    def role(self):
        return type(self).__name__


    def toDict(self)->dict:
        return {
            'name':self.name,
            'age':self.age,
            'salary':self.salary,
            'liquid_salary':self.liquid_salary,
            'bonus':self.get_bonus()
        }