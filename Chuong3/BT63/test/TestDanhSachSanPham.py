from BT63.models.DanhSachSanPham import DanhSachSanPham
from BT63.models.SanPhamChinhHang import SanPhamChinhHang
from BT63.models.SanPhamXachTay import SanPhamXachTay

dssp=DanhSachSanPham()
dssp.them_sanpham(SanPhamChinhHang("sp1","Thuoc Lao",100))
dssp.them_sanpham(SanPhamChinhHang("sp2","Thuoc La",200))
dssp.them_sanpham(SanPhamXachTay("sp3","Thuoc Lac",50))
dssp.them_sanpham(SanPhamChinhHang("sp4","Thuoc Ghe",300))
dssp.them_sanpham(SanPhamXachTay("sp5","Thuoc Phien",150))
print("Danh sach toan bo san pham:")
dssp.xuat_toanbo_sanpham()
print("#"*30)
print("DS san pham chinh hang:")
dsspch=dssp.loc_sanpham_chinhhang()
dsspch.xuat_toanbo_sanpham()

msp="sp4"
sp=dssp.tim_sanpham_theo_ma(msp)
if sp!=None:
    print("Tim thay san pham co ma =", msp)
    print(sp)
else:
    print("Khong tim thay sp nao co ma", msp)

msp="sp5"
dssp.xoa_sanpham_theo_ma(msp)
print("%"*30)
print("DS san pham sau khi xoa msp=", msp)
dssp.xuat_toanbo_sanpham()