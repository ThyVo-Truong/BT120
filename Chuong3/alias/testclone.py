from alias.customer import customer

c1=customer("111", "Newton", "097865")
c2=c1.clone()

print('Thong tin cua c1:')
print(c1)
print('Thong tin cua c2:')
print(c2)
print("*"*30)
c2.name="Dong Ta"
print('Thong tin cua c1:')
print(c1)
print('Thong tin cua c2:')
print(c2)