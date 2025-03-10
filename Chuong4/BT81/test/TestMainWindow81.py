from PyQt6.QtWidgets import QApplication

from BT81.ui.MainWindow81Ext import MainWindow81Ext

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow81Ext()
    window.show()
    app.exec()
