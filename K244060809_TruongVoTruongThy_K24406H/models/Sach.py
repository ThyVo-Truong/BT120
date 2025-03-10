class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia, nam_xb, so_luong):
        self.ma_sach = ma_sach      # Mã sách
        self.ten_sach = ten_sach    # Tên sách
        self.tac_gia = tac_gia      # Tác giả
        self.nam_xb = nam_xb        # Năm xuất bản
        self.so_luong = so_luong    # Số lượng sách trong kho

    def __str__(self):
        return f"{self.ma_sach} - {self.ten_sach} ({self.tac_gia}, {self.nam_xb}) - {self.so_luong} cuốn"
