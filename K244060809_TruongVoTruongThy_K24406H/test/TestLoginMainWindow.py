import sys

from PyQt6.QtWidgets import QApplication

from K244060809_TruongVoTruongThy_K24406H.ui.MainWindowExt import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Mở màn hình đăng nhập trước
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())
