import sys
import functools
import random
from datetime import datetime
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QPushButton, QLabel

from BT60.ui.MainWindow import Ui_MainWindow


class QuanLySinhVien(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Liên kết các nút với hàm xử lý
        self.pushButtonAdd.clicked.connect(self.them_sinh_vien)
        self.pushButtonDelete.clicked.connect(self.xoa_sinh_vien)
        self.pushButtonSearch.clicked.connect(self.tim_sinh_vien)
        self.pushButtonSort.clicked.connect(self.sap_xep_theo_tuoi)

        # Danh sách sinh viên
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self):
        mssv = self.lineEdit_mssv.text()
        ho_ten = self.lineEdit_hoten.text()
        ngay_sinh = self.lineEdit_date.text()

        if not mssv or not ho_ten or not ngay_sinh:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            ngay_sinh = datetime.strptime(ngay_sinh, "%d/%m/%Y")
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Ngày sinh không hợp lệ! (Định dạng: dd/mm/yyyy)")
            return

        tuoi = datetime.now().year - ngay_sinh.year
        self.danh_sach_sinh_vien.append((mssv, ho_ten, ngay_sinh, tuoi))
        self.cap_nhat_danh_sach()

    def xoa_sinh_vien(self):
        dong_dang_chon = self.verticalLayout_list.count() - 1
        if dong_dang_chon >= 0:
            widget = self.verticalLayout_list.itemAt(dong_dang_chon).widget()
            if widget:
                widget.deleteLater()
                del self.danh_sach_sinh_vien[dong_dang_chon]
        else:
            QMessageBox.warning(self, "Lỗi", "Danh sách trống, không thể xóa!")

    def tim_sinh_vien(self):
        ho_ten_tim = self.lineEdit_hoten.text().strip()

        if not ho_ten_tim:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên sinh viên để tìm kiếm!")
            return

        ket_qua = []
        for mssv, ho_ten, ngay_sinh, tuoi in self.danh_sach_sinh_vien:
            if ho_ten_tim.lower() in ho_ten.lower():  # Tìm theo một phần tên
                ket_qua.append(f"{mssv} - {ho_ten} - {ngay_sinh.strftime('%d/%m/%Y')} - {tuoi} tuổi")

        if ket_qua:
            QMessageBox.information(self, "Kết quả tìm kiếm", "\n".join(ket_qua))
        else:
            QMessageBox.information(self, "Kết quả", "Không tìm thấy sinh viên!")

    def sap_xep_theo_tuoi(self):
        self.danh_sach_sinh_vien.sort(key=lambda x: x[3])
        self.cap_nhat_danh_sach()

    def cap_nhat_danh_sach(self):
        while self.verticalLayout_list.count():
            item = self.verticalLayout_list.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for mssv, ho_ten, ngay_sinh, tuoi in self.danh_sach_sinh_vien:
            label = QLabel(f"{mssv} - {ho_ten} - {ngay_sinh.strftime('%d/%m/%Y')} - {tuoi} tuổi")
            self.verticalLayout_list.addWidget(label)







