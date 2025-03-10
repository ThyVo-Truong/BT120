
from PyQt6.QtWidgets import QApplication
from BT60.ui.MainWindow60Ext import QuanLySinhVien

app = QApplication([])
mainwindow = QuanLySinhVien()
mainwindow.show()
app.exec()
