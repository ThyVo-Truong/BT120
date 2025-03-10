from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong4.BT85.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()