class NguoiDung:
    def __init__(self, ma_nguoi_dung, ten, ten_dang_nhap, mat_khau):
        self.ma_nguoi_dung = ma_nguoi_dung  # Mã người dùng
        self.ten = ten                      # Tên người dùng
        self.ten_dang_nhap = ten_dang_nhap  # Tên đăng nhập
        self.mat_khau = mat_khau            # Mật khẩu

    def __str__(self):
        return f"{self.ma_nguoi_dung} - {self.ten} ({self.ten_dang_nhap})"

class SinhVien(NguoiDung):
    def __init__(self, ma_nguoi_dung, ten, ten_dang_nhap, mat_khau, ma_lop):
        super().__init__(ma_nguoi_dung, ten, ten_dang_nhap, mat_khau)
        self.ma_lop = ma_lop  # Mã lớp của sinh viên

    def __str__(self):
        return f"Sinh viên: {super().__str__()} - Lớp {self.ma_lop}"

class GiangVien(NguoiDung):
    def __init__(self, ma_nguoi_dung, ten, ten_dang_nhap, mat_khau, khoa):
        super().__init__(ma_nguoi_dung, ten, ten_dang_nhap, mat_khau)
        self.khoa = khoa  # Khoa giảng dạy

    def __str__(self):
        return f"Giảng viên: {super().__str__()} - Khoa {self.khoa}"

class ThuThu(NguoiDung):
    def __init__(self, ma_nguoi_dung, ten, ten_dang_nhap, mat_khau):
        super().__init__(ma_nguoi_dung, ten, ten_dang_nhap, mat_khau)

    def __str__(self):
        return f"Thủ thư: {super().__str__()}"
