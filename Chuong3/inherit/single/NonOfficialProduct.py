from inherit.single.Product import Product


class NonOfficialProduct(Product):
    def __init__(self,id,name,price):
        super().__init__(id,name,price)
        self.discount=0.08
    def __str__(self):
        infor=super().__str__()
        discount_value=self.discount*self.price
        realpayment=self.price-discount_value
        msg=f"{infor}=>{discount_value}=>{realpayment}"
        return msg