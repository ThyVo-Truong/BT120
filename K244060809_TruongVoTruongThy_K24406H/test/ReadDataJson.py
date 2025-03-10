from K244060809_TruongVoTruongThy_K24406H.libs.JsonFileFactory import LuuTruJSON
from K244060809_TruongVoTruongThy_K24406H.models.NguoiDung import SinhVien, GiangVien, ThuThu
from K244060809_TruongVoTruongThy_K24406H.models.PhieuMuonSach import PhieuMuonSach
from K244060809_TruongVoTruongThy_K24406H.models.Sach import Sach

# Đọc dữ liệu từ JSON
ds_sach = LuuTruJSON.doc_du_lieu("dataset/sach.json", Sach)
ds_sinhvien = LuuTruJSON.doc_du_lieu("dataset/sinhvien.json", SinhVien)
ds_giangvien = LuuTruJSON.doc_du_lieu("dataset/giangvien.json", GiangVien)
ds_thuthu = LuuTruJSON.doc_du_lieu("dataset/thuthu.json", ThuThu)
ds_phieumuon = LuuTruJSON.doc_du_lieu("dataset/phieumuon.json", PhieuMuonSach)

print(" Dữ liệu đã được tải từ JSON!")
print("\nDanh sách sách từ JSON:")
for s in ds_sach:
    print(s)
