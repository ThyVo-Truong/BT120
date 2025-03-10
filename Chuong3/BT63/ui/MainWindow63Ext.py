import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from BT63.models.DanhSachSanPham import DanhSachSanPham
from BT63.models.SanPhamChinhHang import SanPhamChinhHang
from BT63.models.SanPhamXachTay import SanPhamXachTay
from BT63.ui.MainWindow63 import Ui_MainWindow


class MainWindow63Ext(Ui_MainWindow):
    def __init__(self):
        self.dssp=DanhSachSanPham()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.gen_sample_data()
        self.hienthi_sanpham_len_giaodien()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def gen_sample_data(self):
        self.dssp.them_sanpham(SanPhamChinhHang("sp1", "Thuoc Lao", 100))
        self.dssp.them_sanpham(SanPhamChinhHang("sp2", "Thuoc La", 200))
        self.dssp.them_sanpham(SanPhamXachTay("sp3", "Thuoc Lac", 50))
        self.dssp.them_sanpham(SanPhamChinhHang("sp4", "Thuoc Ghe", 300))
        self.dssp.them_sanpham(SanPhamXachTay("sp5", "Thuoc Phien", 150))
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def hienthi_sanpham_len_giaodien(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range (len(self.dssp.list)):
            sp=self.dssp.list[i]
            btn=QPushButton(text=str(sp))
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet,sp))
    def xem_chi_tiet(self,sp):
        self.lineEditId.setText(sp.ma)
        self.lineEditName.setText(sp.ten)
        self.lineEditPrice.setText(str(sp.gia))
        discount=0
        if isinstance(sp,SanPhamXachTay):
            discount=sp.giamgia*sp.gia
            self.radioButtonOfficial.setChecked(True)
        else:
            self.radioButtonNonOfficial.setChecked(True)
        self.lineEditDiscount.setText(str(discount))
    def setupSignalAndSlot(self):
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.pushButtonSave.clicked.connect(self.xuly_luu)
    def xuly_xoa(self):
        msp=self.lineEditId.text()

        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xac nhan xoa")
        dlg.setText(f'E MUON XOA SP [{msp}] HA?')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button=dlg.exec()
        if button==QMessageBox.StandardButton.No:
            return #Ngung ham xoa, khong lam gi ca
        self.dssp.xoa_sanpham_theo_ma(msp)
        self.hienthi_sanpham_len_giaodien()
    def xuly_luu(self):
        if self.radioButtonOfficial.isChecked():
            sp=SanPhamChinhHang()
        else:
            sp=SanPhamXachTay()
        sp.ma=self.lineEditId.text()
        sp.ten=self.lineEditName.text()
        sp.gia=float(self.lineEditPrice.text())
        self.dssp.them_sanpham(sp)
        self.hienthi_sanpham_len_giaodien()

