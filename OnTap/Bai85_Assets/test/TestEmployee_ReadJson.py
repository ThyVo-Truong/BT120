from OnTap.Bai85_Assets.libs.JsonFileFactory import JsonFileFactory
from OnTap.Bai85_Assets.models.Employee import Employee

jff=JsonFileFactory()
filename='../dataset/Employee.json'
employees=jff.read_data(filename, Employee)
print('Danh sách Employee sau khi đọc file:')
for e in employees:
    print (e)
    