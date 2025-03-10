from BT62.models.DanhMuc import DanhMuc
from BT62.models.SanPham import SanPham


class KhoHang:
    def __init__(self):
        self.database=[]
    def add_danhmuc(self,dm):
        self.database.append(dm)
    def fake_data(self):
        dm1 = DanhMuc("DM1", "Laptop")
        dm2 = DanhMuc("DM2", "Phone")
        dm3 = DanhMuc("DM3", "TV")

        self.add_danhmuc(dm1)
        self.add_danhmuc(dm2)
        self.add_danhmuc(dm3)

        dm1.add_product(SanPham("sp1", "Dell 113", 1100, "Trung Quốc"))
        dm1.add_product(SanPham("sp2", "LG 114", 170, "Hàn Quốc"))
        dm1.add_product(SanPham("sp3", "Apple 115", 9100, "Trung Quốc"))

        dm2.add_product(SanPham("sp4", "Android 3", 350, "Trung quốc"))
        dm2.add_product(SanPham("sp5", "Bphone 3", 750, "Việt Nam"))

        dm3.add_product(SanPham("sp6", "TV Đại Việt", 890, "Việt Nam"))
    def xuat_danhsach_danhmuc(self):
        for dm in self.database:
            print("-" * 30)
            print(dm)
            print("-" * 30)
            for sp in dm.list_products:
                print(sp)
    def loc_sanpham_xuatxu(self,xuatxu):
        list_sanpham=[]
        for dm in self.database:
            for sp in dm.list_products:
                if sp.xuatxu==xuatxu:
                    list_sanpham.append(sp)
        return list_sanpham



