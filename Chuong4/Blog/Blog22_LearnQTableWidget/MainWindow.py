# Form implementation generated from reading ui file 'D:\Chuong4\Blog\Blog22_LearnQTableWidget\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 667)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidgetSong = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidgetSong.setGeometry(QtCore.QRect(60, 30, 581, 271))
        self.tableWidgetSong.setObjectName("tableWidgetSong")
        self.tableWidgetSong.setColumnCount(3)
        self.tableWidgetSong.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSong.setItem(4, 2, item)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 340, 161, 31))
        self.label.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 410, 161, 31))
        self.label_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 480, 121, 31))
        self.label_3.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEditSongID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSongID.setGeometry(QtCore.QRect(200, 330, 441, 41))
        self.lineEditSongID.setObjectName("lineEditSongID")
        self.lineEditSongName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSongName.setGeometry(QtCore.QRect(200, 400, 441, 41))
        self.lineEditSongName.setObjectName("lineEditSongName")
        self.lineEditSinger = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditSinger.setGeometry(QtCore.QRect(200, 470, 441, 41))
        self.lineEditSinger.setObjectName("lineEditSinger")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(280, 540, 151, 51))
        self.pushButtonClose.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButtonClose.setObjectName("pushButtonClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonClose.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trương Võ Trường Thy - K244060809"))
        item = self.tableWidgetSong.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetSong.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetSong.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidgetSong.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidgetSong.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidgetSong.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Song ID"))
        item = self.tableWidgetSong.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Song Name"))
        item = self.tableWidgetSong.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Singer"))
        __sortingEnabled = self.tableWidgetSong.isSortingEnabled()
        self.tableWidgetSong.setSortingEnabled(False)
        item = self.tableWidgetSong.item(0, 0)
        item.setText(_translate("MainWindow", "S1"))
        item = self.tableWidgetSong.item(0, 1)
        item.setText(_translate("MainWindow", "Chốn Sa Mạc"))
        item = self.tableWidgetSong.item(0, 2)
        item.setText(_translate("MainWindow", "Lam"))
        item = self.tableWidgetSong.item(1, 0)
        item.setText(_translate("MainWindow", "P2"))
        item = self.tableWidgetSong.item(1, 1)
        item.setText(_translate("MainWindow", "Nếu ngày ấy"))
        item = self.tableWidgetSong.item(1, 2)
        item.setText(_translate("MainWindow", "Soobin"))
        item = self.tableWidgetSong.item(2, 0)
        item.setText(_translate("MainWindow", "P3"))
        item = self.tableWidgetSong.item(2, 1)
        item.setText(_translate("MainWindow", "Cháu lên ba"))
        item = self.tableWidgetSong.item(2, 2)
        item.setText(_translate("MainWindow", "Xuân Mai"))
        item = self.tableWidgetSong.item(3, 0)
        item.setText(_translate("MainWindow", "P4"))
        item = self.tableWidgetSong.item(3, 1)
        item.setText(_translate("MainWindow", "Baby"))
        item = self.tableWidgetSong.item(3, 2)
        item.setText(_translate("MainWindow", "Justin"))
        item = self.tableWidgetSong.item(4, 0)
        item.setText(_translate("MainWindow", "P5"))
        item = self.tableWidgetSong.item(4, 1)
        item.setText(_translate("MainWindow", "Enchanted"))
        item = self.tableWidgetSong.item(4, 2)
        item.setText(_translate("MainWindow", "Taylor"))
        self.tableWidgetSong.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Song ID: "))
        self.label_2.setText(_translate("MainWindow", "Song Name: "))
        self.label_3.setText(_translate("MainWindow", "Singer: "))
        self.pushButtonClose.setText(_translate("MainWindow", "CLOSE"))
