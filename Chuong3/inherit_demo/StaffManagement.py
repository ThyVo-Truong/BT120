from inherit_demo.FulltimeEmployee import FulltimeEmployee
from inherit_demo.ParttimeEmployee import ParttimeEmployee


class StaffManagement:
    def __init__(self):
        self.employees=[]
    def add_employee(self,emp):
        self.employees.append(emp)
    def print_employees(self):
        for emp in self.employees:
            print(emp)
    def get_fulltime_employees(self):
        staff=StaffManagement()
        for emp in self.employees:
            if isinstance(emp,FulltimeEmployee):
                staff.add_employee(emp)
        return staff
    def get_parttime_employees(self):
        staff=StaffManagement()
        for emp in self.employees:
            if isinstance(emp,ParttimeEmployee):
                staff.add_employee(emp)
        return staff
    def get_buget_for_salary(self):
        payment=0
        #viet vong lap cong don get_salary()
        for emp in self.employees:
            payment += emp.get_salary()
        return payment
