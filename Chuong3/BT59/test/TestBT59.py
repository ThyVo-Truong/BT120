from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication

from BT59.ui.MainWindow59Ext import MainWindow59Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow59Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()

