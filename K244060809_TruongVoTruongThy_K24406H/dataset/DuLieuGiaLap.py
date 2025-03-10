import json

from K244060809_TruongVoTruongThy_K24406H.models.NguoiDung import SinhVien, GiangVien, ThuThu
from K244060809_TruongVoTruongThy_K24406H.models.PhieuMuonSach import PhieuMuonSach
from K244060809_TruongVoTruongThy_K24406H.models.Sach import Sach

# Danh sách giả lập
ds_sach = [
    Sach("S1", "Lập trình Python", "Nguyễn Văn A", 2021, 10),
    Sach("S2", "Học máy cơ bản", "Trần B", 2022, 5),
    Sach("S3", "Khoa học dữ liệu", "Lê C", 2020, 7),
    Sach("S4", "Trí tuệ nhân tạo", "Phạm D", 2019, 8),
    Sach("S5", "Lập trình Web", "Hoàng E", 2023, 12)
]

ds_sinhvien = [
    SinhVien("SV1", "Nguyễn Văn A", "nguyenvana", "123456", "CNTT"),
    SinhVien("SV2", "Trần Thị B", "tranb", "654321", "Kinh tế"),
    SinhVien("SV3", "Lê Văn C", "levanc", "111111", "Quản trị"),
    SinhVien("SV4", "Phạm Văn D", "phamvd", "222222", "Công nghệ"),
    SinhVien("SV5", "Hoàng Thị E", "hoangte", "333333", "Marketing")
]

ds_giangvien = [
    GiangVien("GV1", "TS. Nguyễn Mạnh", "nguyenm", "987654", "Công nghệ thông tin"),
    GiangVien("GV2", "ThS. Trần Văn B", "tranvb", "123456", "Khoa học máy tính"),
    GiangVien("GV3", "PGS. TS. Lê Văn C", "levanc", "789012", "Kỹ thuật phần mềm"),
    GiangVien("GV4", "GS. Đinh Quang D", "dinhqd", "456789", "Hệ thống thông tin"),
    GiangVien("GV5", "ThS. Hoàng Anh E", "hoangae", "741852", "Trí tuệ nhân tạo")
]


ds_thuthu = [
    ThuThu("TT1", "Lê Thị Hoa", "lehoa", "000000"),
    ThuThu("TT2", "Nguyễn Minh Tú", "minhtu", "111111"),
    ThuThu("TT3", "Phạm Thành Đạt", "datpham", "222222")
]

ds_phieumuon = [
    PhieuMuonSach("PM1", ds_sinhvien[0], [ds_sach[0], ds_sach[1]]),
    PhieuMuonSach("PM2", ds_sinhvien[1], [ds_sach[2], ds_sach[3]]),
    PhieuMuonSach("PM3", ds_sinhvien[2], [ds_sach[4]])
]


print("Danh sách sách:")
for s in ds_sach:
    print(s)

print("\nDanh sách sinh viên:")
for sv in ds_sinhvien:
    print(sv)

print("\nDanh sách giảng viên:")
for gv in ds_giangvien:
    print(gv)

print("\nDanh sách thủ thư:")
for tt in ds_thuthu:
    print(tt)

print("\nDanh sách phiếu mượn:")
for pm in ds_phieumuon:
    print(pm)
