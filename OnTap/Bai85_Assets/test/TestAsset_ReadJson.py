from OnTap.Bai85_Assets.libs.JsonFileFactory import JsonFileFactory
from OnTap.Bai85_Assets.models.Asset import Asset

jff=JsonFileFactory()
filename='../dataset/Asset.json'
assets=jff.read_data(filename, Asset)
print('Tài sản sau khi đọc từ file:')
for a in assets:
    print (a)