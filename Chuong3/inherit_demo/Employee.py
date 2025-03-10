class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def get_salary(self):
        return 10000000
    def __str__(self):
        infor=f"{self.id}\t{self.name}\t{self.get_salary()}"
        return infor


