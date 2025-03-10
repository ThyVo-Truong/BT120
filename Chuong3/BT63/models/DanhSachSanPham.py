from BT63.models.SanPhamChinhHang import SanPhamChinhHang


class DanhSachSanPham:
    def __init__(self):
        self.list=[]
    def them_sanpham(self,sp):
        self.list.append(sp)
    def tim_sanpham_theo_ma(self,msp):
        for sp in self.list:
            if sp.ma==msp:
                return sp
        return None
    def xoa_sanpham_theo_ma(self,msp):
        sp=self.tim_sanpham_theo_ma(msp)
        if sp!=None:
            self.list.remove(sp)
    def xuat_toanbo_sanpham(self):
        for sp in self.list:
            print(sp)
    def loc_sanpham_chinhhang(self):
        dssp=DanhSachSanPham()
        for sp in self.list:
            if isinstance(sp,SanPhamChinhHang):
                dssp.them_sanpham(sp)
        return dssp