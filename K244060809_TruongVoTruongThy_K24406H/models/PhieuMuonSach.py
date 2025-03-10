class PhieuMuonSach:
    def __init__(self, ma_phieu, nguoi_muon, sach_muon):
        self.ma_phieu = ma_phieu    # Mã phiếu mượn
        self.nguoi_muon = nguoi_muon  # Người mượn (Sinh viên/Giảng viên)
        self.sach_muon = sach_muon    # Danh sách sách mượn

    def __str__(self):
        sach_str = ", ".join([sach.ten_sach for sach in self.sach_muon])
        return f"Phiếu {self.ma_phieu} - Người mượn: {self.nguoi_muon.ten} - Sách mượn: {sach_str}"
