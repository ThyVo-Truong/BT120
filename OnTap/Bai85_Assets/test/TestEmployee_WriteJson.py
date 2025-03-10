from OnTap.Bai85_Assets.libs.JsonFileFactory import JsonFileFactory
from OnTap.Bai85_Assets.models.Employee import Employee

employees=[]
employees.append(Employee('E1', 'Teo', 'teo', "123"))
employees.append(Employee('E2', 'Ty', 'ty', "5g6"))
employees.append(Employee('E3', 'Bin', 'bin', "b62"))
employees.append(Employee('E4', 'Bo', 'bo', "965"))
employees.append(Employee('E5', 'Bun', 'bun', "gdy"))
employees.append(Employee('E6', 'Tun', 'tun', "8gf"))
print ('Danh sách Employee:')
for e in employees:
    print(e)
jff=JsonFileFactory()
filename='../dataset/Employee.json'
jff.write_data(employees, filename)