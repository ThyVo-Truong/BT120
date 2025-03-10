from OnTap.Bai85_Assets.libs.JsonFileFactory import JsonFileFactory
from OnTap.Bai85_Assets.models.Employee_Asset import Employee_Asset

eas=[]
eas.append(Employee_Asset('E1', "AS1", 'MAIN'))
eas.append(Employee_Asset('E2', "AS2", 'MAIN'))
eas.append(Employee_Asset('E3', "AS3", 'MAIN'))
eas.append(Employee_Asset('E4', "AS4", 'MAIN'))
eas.append(Employee_Asset('E5', "AS5", 'MAIN'))
eas.append(Employee_Asset('E6', "AS6", 'MAIN'))
eas.append(Employee_Asset('E7', "AS7", 'MAIN'))
eas.append(Employee_Asset('E8', "AS8", 'MAIN'))
eas.append(Employee_Asset('E9', "AS9", 'MAIN'))
eas.append(Employee_Asset('E10', "A10", 'MAIN'))

print('Danh sách phân công quản lý tài sản:')
for ea in eas:
    print(ea)

jff=JsonFileFactory()
filename='../dataset/employee_assets.json'
jff.write_data(eas, filename)
