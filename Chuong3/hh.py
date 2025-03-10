class Student:
    def __init__(self,id, name, age):
        self.id=id
        self.name=name
        self.age=age
    def __str__(self):
        infor=f"{self.id}\t{self.name}\t{self.age}"
        return infor
#Mo hinh hoas cacs doi tuong trong do an
