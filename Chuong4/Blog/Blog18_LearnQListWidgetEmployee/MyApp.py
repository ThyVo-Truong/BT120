from PyQt6.QtWidgets import QApplication, QMainWindow

from Blog.Blog18_LearnQListWidgetEmployee.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()