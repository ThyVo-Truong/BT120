from Chuong4.BT85.libs.JsonFileFactory import JsonFileFactory
from Chuong4.BT85.models.Asset import Asset

jff=JsonFileFactory()
filename='../dataset/assets.json'
assets=jff.read_data(filename,Asset)
print('Tài sản sau khi đọc từ file:')
for a in assets:
    print(a)
