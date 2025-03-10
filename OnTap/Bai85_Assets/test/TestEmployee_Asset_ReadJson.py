from OnTap.Bai85_Assets.libs.JsonFileFactory import JsonFileFactory
from OnTap.Bai85_Assets.models.Employee_Asset import Employee_Asset

jff=JsonFileFactory()
filename='../dataset/Employee_Assets.json'
eas=jff.read_data(filename, Employee_Asset)
print('Danh sách phân công quản lý tài sản đọc từ file:')
for ea in eas:
    print(ea)