class customer:
    def __init__(self,id=None, name=None, age=None):
        self.id=id
        self.name=name
        self.age=age
    def print_info(self):
        print(f'{self.id}\t{self.name}\t{self.age}')
c1=customer('c1', 'tran a na', 22)
print('Thong tin cua khach hang c1:')
c1.print_info() # c1 goi instance method print_infor
                # c1 is instance of class customer


