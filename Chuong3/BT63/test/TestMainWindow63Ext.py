from PyQt6.QtWidgets import QApplication, QMainWindow

from BT63.ui.MainWindow63Ext import MainWindow63Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow63Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
