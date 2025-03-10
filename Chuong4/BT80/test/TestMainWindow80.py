from PyQt6.QtWidgets import QApplication

from BT80.ui.MainWindow80Ext import MainWindow80Ext

app = QApplication([])
myui = MainWindow80Ext()  # Tạo đối tượng giao diện
myui.show()  # Hiển thị cửa sổ chính
app.exec()  # Chạy vòng lặp sự kiện
