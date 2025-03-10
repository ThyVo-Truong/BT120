class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=float(price)
    def __str__(self):
        infor=f"{self.id}\t{self.name}\t{self.price}"
        return infor
