class ListStudent:
    def __init__(self):
        self.list=[]
    #Ham them 1 sv cuoi ds
    def appen_student(self,st):
        self.list.append(st)
    #Ham xuat toan bo ds sv
    def print_students(self):
        for st in self.list:
            print(st)