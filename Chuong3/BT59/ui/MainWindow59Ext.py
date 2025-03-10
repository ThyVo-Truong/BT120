from BT59.models.PhanSo import PhanSo
from BT59.ui.MainWindow import Ui_MainWindow

class MainWindow59Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonCong.clicked.connect(self.xuly_cong)
        self.pushButtonTru.clicked.connect(self.xuly_tru)
        self.pushButtonNhan.clicked.connect(self.xuly_nhan)
        self.pushButtonChia.clicked.connect(self.xuly_chia)
    def lay_cac_phanso(self):
        tu1=int(self.lineEditPhanSo1Tu.text())
        mau1=int(self.lineEditPhanSo1Mau.text())
        tu2=int(self.lineEditPhanSo2Tu.text())
        mau2=int(self.lineEditPhanSo2Mau.text())
        ps1=PhanSo(tu1,mau1)
        ps2=PhanSo(tu2,mau2)
        return (ps1,ps2)

    def xuly_cong(self):
        ps1,ps2=self.lay_cac_phanso()
        ps3=ps1.cong(ps2).toi_gian()
        self.lineEditPhanSo3Tu.setText(f'{ps3.tu}')
        self.lineEditPhanSo3Mau.setText(f'{ps3.mau}')
        self.labelPhepToan.setText('+')

    def xuly_tru(self):
        ps1,ps2=self.lay_cac_phanso()
        ps3=ps1.tru(ps2).toi_gian()
        self.lineEditPhanSo3Tu.setText(f'{ps3.tu}')
        self.lineEditPhanSo3Mau.setText(f'{ps3.mau}')
        self.labelPhepToan.setText('-')

    def xuly_nhan(self):
        ps1,ps2=self.lay_cac_phanso()
        ps3=ps1.nhan(ps2).toi_gian()
        self.lineEditPhanSo3Tu.setText(f'{ps3.tu}')
        self.lineEditPhanSo3Mau.setText(f'{ps3.mau}')
        self.labelPhepToan.setText('*')

    def xuly_chia(self):
        ps1,ps2=self.lay_cac_phanso()
        ps3=ps1.chia(ps2).toi_gian()
        self.lineEditPhanSo3Tu.setText(f'{ps3.tu}')
        self.lineEditPhanSo3Mau.setText(f'{ps3.mau}')
        self.labelPhepToan.setText('/')

