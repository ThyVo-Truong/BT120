from inherit_demo.Employee import Employee

class FulltimeEmployee(Employee):
    def get_salary(self):
        return super().get_salary()*1.1
