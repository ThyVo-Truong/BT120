class KhachHang:
    def __init__ (self, ma=None, ten=None, phone=None, loai=None):
        self.ma=ma
        self.ten=ten
        self.phone=phone
        self.loai=loai
    def __str__(self):
        infor=f"{self.ma}\t{self.ten}\t{self.phone}\t{self.loai.value}"
        return infor
