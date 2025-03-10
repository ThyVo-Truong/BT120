class NhanVien:
    def __init__(self, ho, ten, so_san_pham):
        self.ho = ho
        self.ten = ten
        self.so_san_pham = max(0, so_san_pham)  # Nếu số sản phẩm âm, gán về 0

    def get_ho(self):
        return self.ho

    def set_ho(self, ho):
        self.ho = ho

    def get_ten(self):
        return self.ten

    def set_ten(self, ten):
        self.ten = ten

    def get_so_san_pham(self):
        return self.so_san_pham

    def set_so_san_pham(self, so_san_pham):
        self.so_san_pham = max(0, so_san_pham)

    def getLuong(self):
        """Tính lương dựa trên số sản phẩm"""
        if 1 <= self.so_san_pham <= 199:
            don_gia = 0.5
        elif 200 <= self.so_san_pham <= 399:
            don_gia = 0.55
        elif 400 <= self.so_san_pham <= 599:
            don_gia = 0.6
        else:  # 600 sản phẩm trở lên
            don_gia = 0.65

        return self.so_san_pham * don_gia

    def IsHigher(self, nv2):
        """So sánh số sản phẩm với nhân viên khác"""
        return self.so_san_pham > nv2.so_san_pham


# Chương trình chính
def main():
    print("Nhập thông tin nhân viên 1:")
    ho1 = input("Nhập họ: ")
    ten1 = input("Nhập tên: ")
    so_san_pham1 = int(input("Nhập số sản phẩm: "))

    print("\nNhập thông tin nhân viên 2:")
    ho2 = input("Nhập họ: ")
    ten2 = input("Nhập tên: ")
    so_san_pham2 = int(input("Nhập số sản phẩm: "))

    nv1 = NhanVien(ho1, ten1, so_san_pham1)
    nv2 = NhanVien(ho2, ten2, so_san_pham2)

    # Tính lương của từng nhân viên
    luong_nv1 = nv1.getLuong()
    luong_nv2 = nv2.getLuong()

    print(f"\nLương của {nv1.ho} {nv1.ten}: {luong_nv1:.2f}")
    print(f"Lương của {nv2.ho} {nv2.ten}: {luong_nv2:.2f}")

    # So sánh số sản phẩm
    if nv1.IsHigher(nv2):
        print(
            f"\nNhân viên {nv1.ho} {nv1.ten} có số sản phẩm nhiều hơn {nv2.ho} {nv2.ten} là {nv1.so_san_pham - nv2.so_san_pham} sản phẩm.")
    elif nv2.IsHigher(nv1):
        print(
            f"\nNhân viên {nv2.ho} {nv2.ten} có số sản phẩm nhiều hơn {nv1.ho} {nv1.ten} là {nv2.so_san_pham - nv1.so_san_pham} sản phẩm.")
    else:
        print("\nCả hai nhân viên có số sản phẩm bằng nhau.")

    # So sánh không dùng IsHigher
    if nv1.so_san_pham > nv2.so_san_pham:
        print(f"(Không dùng IsHigher) Nhân viên {nv1.ho} {nv1.ten} có số sản phẩm nhiều hơn.")
    elif nv2.so_san_pham > nv1.so_san_pham:
        print(f"(Không dùng IsHigher) Nhân viên {nv2.ho} {nv2.ten} có số sản phẩm nhiều hơn.")
    else:
        print("(Không dùng IsHigher) Cả hai nhân viên có số sản phẩm bằng nhau.")


if __name__ == "__main__":
    main()
