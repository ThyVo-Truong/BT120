from learnenum.KhachHang import KhachHang
from learnenum.LoaiKhachHang import LoaiKhachHang
from learnenum.QuanLyKhachHang import QuanLyKhachHang

ql=QuanLyKhachHang()
ql.them_khachhang(KhachHang("kh1",'Teo',"098345678", LoaiKhachHang.VIP))
ql.them_khachhang(KhachHang("kh2",'Ty',"097545678", LoaiKhachHang.NORMAL))
ql.them_khachhang(KhachHang("kh3",'Bin',"098345898", LoaiKhachHang.NORMAL))
ql.them_khachhang(KhachHang("kh4",'Bo',"012340876", LoaiKhachHang.POTENTIAL))
ql.them_khachhang(KhachHang("kh5",'Bun',"098390078", LoaiKhachHang.OTHER))
ql.them_khachhang(KhachHang("kh6",'Run',"012346778", LoaiKhachHang.OTHER))
ql.them_khachhang(KhachHang("kh7",'Tun',"097317978", LoaiKhachHang.NORMAL))
ql.them_khachhang(KhachHang("kh8",'Beo',"0980009776", LoaiKhachHang.POTENTIAL))

print('*'*30)
print("DS toan bo khach hang cua cong ty:")
ql.xuat_toanbo_khachhang()

khthuong=ql.loc_khachhang_theo_phanloai(LoaiKhachHang.NORMAL)
print("*"*30)
print("DS Khach hang thuong:")
khthuong.xuat_toanbo_khachhang()
arr_phone_suffix=['098', '097']
kh_nhamang=ql.loc_khachhang_theo_nhamang(arr_phone_suffix)
print("*"*30)
print('DS khach hang theo nha mang Viettel:')
kh_nhamang.xuat_toanbo_khachhang()

print("*"*30)
print("Toan bo khach hang")
ql.xuat_toanbo_khachhang()
