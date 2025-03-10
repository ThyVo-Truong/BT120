from Access.Products import Products

p1=Products('p1', "thuoc lac", 15,100)
# rtruy suat lay thong tin ten sp
# print(p1.__name) #bao loi vi la private
print(p1.get_name())
#muon doi ten sp
p1.set_name('thuoc tri phong bat')
print("Ten moi cua sp:")
print(p1.get_name())


