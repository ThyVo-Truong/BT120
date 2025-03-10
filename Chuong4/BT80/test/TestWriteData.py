from BT80.libs.FileFactory import FileFactory
from BT80.models.Product import Product

print("Input Products:")
while True:
   productId=input("Input Product ID:")
   productName=input("Input Product Name:")
   unitPrice=float(input("Input Unit Price:"))
   product=Product(productId,productName,unitPrice)

   FileFactory.writeData("database.txt.txt",product)
   ans=input("Continue?(Y/N):")
   if ans!='Y' or ans!='y':
     break
