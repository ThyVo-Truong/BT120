from BT62.models.KhoHang import KhoHang

kho_binhduong=KhoHang()
kho_binhduong.fake_data() #Giả lập một số dữ liệu để thử nghiệm
print('Danh sách sản phẩm trong kho Bình Dương:')
kho_binhduong.xuat_danhsach_danhmuc()
lsp=kho_binhduong.loc_sanpham_xuatxu("Trung Quốc")
print("Các sản phẩm có xuất xứ Trung Quốc:")
for sp in lsp:
    print(sp)
