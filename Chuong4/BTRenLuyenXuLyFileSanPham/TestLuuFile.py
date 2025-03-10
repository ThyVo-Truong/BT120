from XuLyFile import *
masp=input('Nhập mã sản phẩm:')
tensp=input('Nhập tên sản phẩm:')
dongia=float(input('Nhập giá:'))
line=masp+";"+tensp+";"+str(dongia)+";"
LuuFile('database.txt',line)
