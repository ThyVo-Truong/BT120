from Chuong6.BT117.ui.MainWindow117 import Ui_MainWindow


class MainWindow117Ext(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self,do_task)
    def do_task(self):
        s=self.lineEditInputData.text()
        arr=s.split(',')
        print("Arr before casting Integer:")
        print(arr)
        # for i in range(len(arr)):
        #     arr[i]=int
