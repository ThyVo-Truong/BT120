from PyQt6.QtWidgets import QApplication, QMainWindow

from Blog.Blog22_LearnQTableWidget.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()