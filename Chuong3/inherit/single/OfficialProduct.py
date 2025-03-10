from inherit.single.Product import Product


class OfficialProduct(Product):
    def __init__(self,id,name,price):
        super().__init__(id,name,price)
        self.vat=0.01
    def __str__(self):
        infor=super().__str__()
        taxpayment=self.price*self.vat
        msg=f"{infor}=>{taxpayment}"
        return msg
