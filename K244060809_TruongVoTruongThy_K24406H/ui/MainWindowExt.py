import json
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from K244060809_TruongVoTruongThy_K24406H.dataset.DuLieuGiaLap import ds_sinhvien, ds_giangvien, ds_thuthu
# Import giao diện
from K244060809_TruongVoTruongThy_K24406H.ui.MainWindow import Ui_MainWindow
from K244060809_TruongVoTruongThy_K24406H.ui.welcomeThuThu import Ui_WelcomeLibrarian
from K244060809_TruongVoTruongThy_K24406H.ui.welcomestu import Ui_WelcomeStudent
from K244060809_TruongVoTruongThy_K24406H.ui.welcometeacher import Ui_WelcomeTeacher

# Tạo ACCOUNT từ danh sách giả lập
ACCOUNTS = {}

# Thêm sinh viên vào ACCOUNTS
for sv in ds_sinhvien:
    ACCOUNTS[sv.ma_nguoi_dung] = {"password": sv.mat_khau, "role": "student"}

# Thêm giảng viên vào ACCOUNTS
for gv in ds_giangvien:
    ACCOUNTS[gv.ma_nguoi_dung] = {"password": gv.mat_khau, "role": "teacher"}

# Thêm thủ thư vào ACCOUNTS
for tt in ds_thuthu:
    ACCOUNTS[tt.ma_nguoi_dung] = {"password": tt.mat_khau, "role": "librarian"}

# Kiểm tra kết quả
print(json.dumps(ACCOUNTS, indent=4, ensure_ascii=False))

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Xử lý sự kiện khi nhấn nút Đăng nhập
        self.pushButton.clicked.connect(self.login)

        # Xử lý sự kiện khi nhấn nút Thoát
        self.pushButton_2.clicked.connect(self.close)

    def login(self):
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()

        # Xác định vai trò từ radio button
        if self.radioButton.isChecked():
            role = "student"
        elif self.radioButton_2.isChecked():
            role = "teacher"
        elif self.radioButton_3.isChecked():
            role = "librarian"
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn loại tài khoản!")
            return

        # Kiểm tra tài khoản
        if username in ACCOUNTS and ACCOUNTS[username]["password"] == password:
            if ACCOUNTS[username]["role"] == role:
                QMessageBox.information(self, "Thành công", f"Đăng nhập thành công!\nXin chào {username}")

                # Mở cửa sổ chào mừng
                self.open_welcome_window(username, role)
            else:
                QMessageBox.warning(self, "Lỗi", "Sai loại tài khoản!")
        else:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def open_welcome_window(self, username, role):
        self.welcome_window = WelcomeWindow(role, username)
        self.welcome_window.show()
        self.close()

class WelcomeWindow(QMainWindow):
    def __init__(self, role, username):
        """
        role: Loại tài khoản đăng nhập ('student', 'teacher', 'librarian')
        username: Tên người dùng (hiển thị trên tiêu đề)
        """
        super().__init__()

        # Xác định giao diện phù hợp với vai trò
        if role == "student":
            self.ui = Ui_WelcomeStudent()
            self.setWindowTitle(f"Xin chào Sinh viên {username}")
        elif role == "teacher":
            self.ui = Ui_WelcomeTeacher()
            self.setWindowTitle(f"Xin chào Giảng viên {username}")
        elif role == "librarian":
            self.ui = Ui_WelcomeLibrarian()
            self.setWindowTitle(f"Xin chào Thủ thư {username}")
        else:
            raise ValueError("Vai trò không hợp lệ!")

        # Thiết lập giao diện
        self.ui.setupUi(self)

    def close(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Xác nhận thoát")
        dlg.setText("Bạn có chắc chắn muốn thoát chương trình không?")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            self.close()


