from tkinter.font import names


class book:
    def __init__(self, id=None, year=None):
        self.id=id
        self.name=name
        self.year=year
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.year}"
b1=book()
b2=book("B1")
b3=book("B1", 'Python nag cao')
b4=book("B1", "Python nag cao", 2025)

print('thong tin b1:')
print(b1)
print('thong tin b2:')
print(b2)
print('thong tin b3:')
print(b3)
print('thong tin b4:')
print(b4)

b5= book(name='may hoc co ban')
print("thong tin b5")
print(b5)
