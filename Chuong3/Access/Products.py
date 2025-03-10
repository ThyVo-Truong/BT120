from tkinter.font import names


class Products:
    def __init__(self,id,name,quantity,price):
        self.__id=id
        self.__name=name
        self.__quantity=quantity
        self.__price=price
    def get_id(self):
        return self.__id
    def set_id(self):
        self.__id=id
    def get_name(self):
        return self.__name
    def set_name(self):
        self.__name=name
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self):
        self.__quantity=quantity
    def get_price(self):
        return self.__price
    def set_price(self):
        self.__price= price


    id=property(get_id,set_id."id")
    name=property(get_name, set_name, 'name')
    quantity=property(get_quantity, set_quantity,'quantity')
    price=property(get_price,set_price,'price')

    p2=Products('p2','Thuoc giam dep trai', 15,80)
    print('ten thuoc p2:')
    print(p2.name) #Tuwj dong goi getter
    p2.price=800 # tu dong goi setter
    print('Gia cua sp 2:')
    print(p2.price) #tu dong goi getter