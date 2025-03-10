from K244060809_TruongVoTruongThy_K24406H.dataset.DuLieuGiaLap import ds_sach, ds_sinhvien, ds_giangvien, ds_thuthu, \
    ds_phieumuon
from K244060809_TruongVoTruongThy_K24406H.libs.JsonFileFactory import LuuTruJSON

# Lưu vào thư mục dataset/
LuuTruJSON.ghi_du_lieu(ds_sach, "dataset/sach.json")
LuuTruJSON.ghi_du_lieu(ds_sinhvien, "dataset/sinhvien.json")
LuuTruJSON.ghi_du_lieu(ds_giangvien, "dataset/giangvien.json")
LuuTruJSON.ghi_du_lieu(ds_thuthu, "dataset/thuthu.json")
LuuTruJSON.ghi_du_lieu(ds_phieumuon, "dataset/phieumuonsach.json")

print(" Dữ liệu đã được lưu vào JSON!")
