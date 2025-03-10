from Chuong5.ProductManagement.libs.JsonFileFactory import JsonFileFactory
from Chuong5.ProductManagement.models.Category import Category

categories=[]
jff=JsonFileFactory()
filename="../dataset/categories.json"
categories=jff.read_data(filename,Category)
print("List of Categories after reading Json:")
for cate in categories:
    print(cate)

