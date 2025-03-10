from BT80.libs.FileFactory import FileFactory

products=FileFactory.readData("database.txt")
def printProducts(products):
   for product in products:
     print(product)
   print()
printProducts(products)
def sortProducts(products):
   for i in range(len(products)):
     for j in range(len(products)):
       pi=products[i]
       pj=products[j]
       if pi.unitPrice<pj.unitPrice:
          products[i]=pj
          products[j]=pi
sortProducts(products)
print("Products after UnitPrice Sorting:")
printProducts(products)
