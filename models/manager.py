from models.employee import Employee

class Manager(Employee):
    def get_bonus(self)->float:
        return self.salary * 0.10