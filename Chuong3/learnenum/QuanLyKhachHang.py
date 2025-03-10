class QuanLyKhachHang:
    def __init__(self):
        self.list=[]
    def them_khachhang(self,kh):
        self.list.append(kh)
    def xuat_toanbo_khachhang(self):
        for kh in self.list:
            print(kh)
    #Viet ham loc ds kh theo loai tuy y
    def loc_khachhang_theo_phanloai(self,loai):
        ql=QuanLyKhachHang()
        for kh in self.list:
            if kh.loai==loai:
                ql.them_khachhang(kh)
        return ql
    #vi du arr_phone_suffix=['098','097'] la Viettel
    def kiemtra_trung(self,arr_phone_suffix, realphone):
        for phone_suffix in arr_phone_suffix:
            if realphone.startwith(phone_suffix):
                return True
        return False
    def loc_khachhang_theo_nhamang(self,arr_phone_suffix):
        ql=QuanLyKhachHang()
        for kh in self.list:
            if self.kiemtra_trung(arr_phone_suffix, kh.phone):
                ql.them_khachhang(kh)
        return ql
    def sapxep_khachhang_theoloai(self):
        for i in range(len(self.list)):
            for j in range(i+1, len(self.list)):
                khi=self.list[i]
                khj=self.list[j]
                if khi.loai.name>khj.loai.name:
                    self.list[i]=khj
                else:
                    self.list[i]=khj
                    self.list[j]=khi

