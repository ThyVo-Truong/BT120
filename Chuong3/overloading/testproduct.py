from overloading.product import product
p1=product()
p2=product('111')
p3=product('111', 'coca')
p4=product('111', 'coca', 20)

print(p1)
print(p2)
print(p3)
print(p4)

print("statistic=>",p4.statistic())
print("statistic=>",p4.statistic(100))
print("statistic=>",p4.statistic(100,200))

print(p3.calc(4,5))
print(p3.calc(4,5,6))
print(p3.calc(4.0,5.0))

