import random

from Chuong5.ProductManagement.libs.JsonFileFactory import JsonFileFactory
from Chuong5.ProductManagement.models.Product import Product

products=[]
for i in range(1,1001):
    proid=f"P{i}"
    proname=f"Product {i}"
    price=random.randrange(10,1000)
    quantity=random.randrange(1,10)
    cateid=f"c{random.randrange(1,21)}"
    p=Product(proid,proname,price,quantity,cateid)
    products.append(p)
print("List of Products:")
for product in products:
    print(product)
jff=JsonFileFactory()
filename="../dataset/products.json"
jff.write_data(products,filename)
