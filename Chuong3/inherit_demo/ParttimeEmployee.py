from inherit_demo.Employee import Employee


class ParttimeEmployee(Employee):
    def __init(self,id,name,workday):
        super().__init__(id,name)
        self.workday=workday
    def get_salary(self):
        return 200000*self.workday