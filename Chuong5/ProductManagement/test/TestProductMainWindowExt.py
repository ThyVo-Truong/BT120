from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong5.ProductManagement.ui.ProductMainWindowExt import ProductMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=ProductMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()