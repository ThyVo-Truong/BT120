from PyQt6.QtWidgets import QApplication, QMainWindow
from Blog.Blog23_LearnQTableWidgetPart2.MainWindowExt import MainWindowExt

app=QApplication([])
myWindow=MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()