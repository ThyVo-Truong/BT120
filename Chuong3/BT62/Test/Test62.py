from BT62.models.DanhMuc import DanhMuc
from BT62.models.KhoHang import KhoHang
from BT62.models.SanPham import SanPham

kho_hang=[]
dm1=DanhMuc("DM1","Laptop")
dm2=DanhMuc("DM2","Phone")
dm3=DanhMuc("DM3","TV")
kho_hang.extend([dm1,dm2,dm3])
print("Danh sách danh mục sản phẩm trong kho hàng:")
for dm in kho_hang:
    print(dm)
dm1.add_product(SanPham("sp1", "Dell 113", 1100, "Trung Quốc"))
dm1.add_product(SanPham("sp2", "LG 114", 170, "Hàn Quốc"))
dm1.add_product(SanPham("sp3", "Apple 115", 9100, "Trung Quốc"))

dm2.add_product(SanPham("sp4", "Android 3", 350, "Trung quốc"))
dm2.add_product(SanPham("sp5", "Bphone 3", 750, "Việt Nam"))

dm3.add_product(SanPham("sp6", "TV Đại Việt", 890, "Việt Nam"))

print("*"*30)
print("Sản phẩm phân loại theo danh mục:")
for dm in kho_hang:
    print("-"*30)
    print(dm)
    print("-" * 30)
    for sp in dm.list_products:
        print(sp)


