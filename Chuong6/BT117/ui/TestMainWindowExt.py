from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong6.BT117.ui.MainWindow117Ext import MainWindow117Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow117Ext()
myui.setupUi