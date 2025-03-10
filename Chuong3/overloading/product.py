from multipledispatch import dispatch
class product:
    def __init__(self, id=None, name=None, price=None):
        self.id=id
        self.name=name
        self.price=price
    def __str__(self):
        infor=f"{self.id}\t{self.name}\t{self.price}"
        return infor
    def statistic (self,a=0,b=0):
        return a+b
    @dispatch(int,int)
    def calc (self,a,b):
        return a+b
    @dispatch(int,int,int)
    def calc (self,a,b,c):
        return a+b+c
    @dispatch(float,float)
    def calc(self, a,b):
        return a*b