
from BT62.models.SanPham import SanPham

class DanhMuc:
    def __init__(self, ma=None, ten=None):
        self.ma = ma
        self.ten = ten
        self.list_products = []  # Lưu danh sách sản phẩm

    def __str__(self):
        return f"{self.ma}\t{self.ten}"

    def add_product(self, p):
        self.list_products.append(p)

    def print_products(self):
        for p in self.list_products:
            print(p)

    def remove_product(self, ma_san_pham):
        """Xóa sản phẩm dựa trên mã"""
        for p in self.list_products:
            if p.ma == ma_san_pham:
                self.list_products.remove(p)
                print(f"Đã xóa sản phẩm: {p.ten}")
                return
        print(f"Không tìm thấy sản phẩm với mã: {ma_san_pham}")

    def update_product(self, ma_san_pham, ten_moi=None, gia_moi=None):
        """Cập nhật thông tin sản phẩm dựa trên mã sản phẩm"""
        for p in self.list_products:
            if p.ma == ma_san_pham:
                if ten_moi:
                    p.ten = ten_moi
                if gia_moi:
                    p.gia = gia_moi
                print(f"Đã cập nhật sản phẩm: {p}")
                return
        print(f"Không tìm thấy sản phẩm với mã: {ma_san_pham}")

    def total_value(self):
        """Thống kê tổng giá trị của các mặt hàng"""
        total = sum(p.gia for p in self.list_products)
        print(f"Tổng giá trị các mặt hàng: {total}")
        return total

if __name__ == "__main__":
    # Khởi tạo đối tượng DanhMuc để thực hiện các phương thức
    dm = DanhMuc("DM1", "Laptop")  # Tạo đối tượng DanhMuc

    # Thêm sản phẩm vào danh mục
    dm.add_product(SanPham("SP1", "DELL 113", 1100, "Trung Quốc"))
    dm.add_product(SanPham("SP2", "LG 114", 800, "Trung Quốc"))

    # In danh sách sản phẩm
    print("Danh sách sản phẩm:")
    dm.print_products()

    # Xóa sản phẩm
    print("\nXóa sản phẩm :")
    dm.remove_product("SP1")

    # In danh sách sản phẩm sau khi xóa
    print("\nDanh sách sản phẩm sau khi xóa:")
    dm.print_products()

    # Cập nhật sản phẩm
    print("\nCập nhật sản phẩm :")
    dm.update_product("SP2", ten_moi="LG 115", gia_moi=850)

    # In danh sách sản phẩm sau khi cập nhật
    print("\nDanh sách sản phẩm sau khi cập nhật:")
    dm.print_products()

    # Thống kê tổng giá trị các mặt hàng
    print("\nThống kê tổng giá trị các mặt hàng:")
    dm.total_value()

