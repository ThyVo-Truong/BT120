from Chuong5.ProductManagement.libs.JsonFileFactory import JsonFileFactory
from Chuong5.ProductManagement.models.Product import Product

products=[]
jff=JsonFileFactory()
filename="../dataset/products.json"
products=jff.read_data(filename,Product)
print("List Of Products after Loading Json:")
for product in products:
    print(product)

