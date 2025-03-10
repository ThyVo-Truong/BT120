class SanPham:
    def __init_(self, ma=None, ten=None, gia=None):
        self.ma=ma
        self.ten=ten
        self.gia=gia
    def __str__(self):
        return f"{self.ma}\t{self.ten}\t{self.gia}"