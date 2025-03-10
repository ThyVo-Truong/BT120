from BT63.models.SanPham import SanPham


class SanPhamChinhHang(SanPham):
    def __init__(self,ma=None, ten=None, gia=None):
        super().__init__(ma,ten,gia)
        self.thue=0.1
        self.giamgia=0
    def __str__(self):
        msg=super().__str__()
        return msg+"(Chinh Hang)"