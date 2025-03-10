from Access.Employee import Employee

e1=Employee("EMP113","Teo dai bang",28)
print("Thong tin e1:")
print(e1) #tu dong lay chuoi trong ham
#doi ma e1:
e1.id="EMP114"
print("Thong tin e1 sau khi sua:")
print(e1)
e1._name="Ti ruoi"
print("Thong tin cua e1 sau khi doi ten:")
print(e1)
e1.__age=30
print("Thong tin cua e1 sau khi doi tuoi:")
print(e1)

