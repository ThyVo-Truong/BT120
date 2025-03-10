import os
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox

from Chuong5.ProductManagement.libs.DataConnector import DataConnector
from Chuong5.ProductManagement.models.Product import Product
from Chuong5.ProductManagement.ui.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt (Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.categories = self.dc.get_all_categories()
        self.products = self.dc.get_all_products()
        self.selected_cate = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_categories_gui()
        self.show_products_gui()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def show_categories_gui(self):
        #clear all previous data from QListWidget:
        self.listWidgetCategory.clear()
        #load cate objects into QListWidget:
        for cate in self.categories:
            cate_item=QListWidgetItem(str(cate))
            self.listWidgetCategory.addItem(cate_item)

    def show_products_gui(self):
        #clear all previous data from QTableWidget:
        self.tableWidgetProduct.setRowCount(0)
        #load product into QTableWidget:
        for product in self.products:
            #get number of row (meaning last index):
            row=self.tableWidgetProduct.rowCount()
            #insert new row (last row, at the end of row in the Table):
            self.tableWidgetProduct.insertRow(row)
            #creating 5 columns for each row:
            col_proid=QTableWidgetItem(product.proid)
            col_proname=QTableWidgetItem(product.proname)
            col_price=QTableWidgetItem(str(product.price))
            col_quantity=QTableWidgetItem(str(product.quantity))
            col_cateid=QTableWidgetItem(str(product.cateid))
            #set column for row:
            self.tableWidgetProduct.setItem(row,0,col_proid)
            self.tableWidgetProduct.setItem(row,1,col_proname)
            self.tableWidgetProduct.setItem(row,2,col_price)
            self.tableWidgetProduct.setItem(row,3,col_quantity)
            self.tableWidgetProduct.setItem(row,4,col_cateid)
            if product.price>=800 and product.price<=1000:
                col_proid.setBackground(Qt.GlobalColor.red)
                col_proname.setBackground(Qt.GlobalColor.red)
                col_price.setBackground(Qt.GlobalColor.red)
                col_quantity.setBackground(Qt.GlobalColor.red)
                col_cateid.setBackground(Qt.GlobalColor.red)

    def setupSignalAndSlot(self):
        self.listWidgetCategory.itemSelectionChanged.connect(self.filter_products)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.show_detail_product)
        self.pushButtonClear.clicked.connect(self.clear_product_detail)
        self.pushButtonSave.clicked.connect(self.save_product)
        self.pushButtonDelete.clicked.connect(self.delete_product)

    def filter_products(self):
        #get current selected index:
        row=self.listWidgetCategory.currentRow()
        if row<0:#not found selected index
            return
        self.selected_cate=self.categories[row]
        #filter products by cate id
        self.products=self.dc.get_products_by_category(self.selected_cate.cateid)
        #re-display products into QTableWidget
        self.show_products_gui()
    def show_detail_product(self):
        index=self.tableWidgetProduct.currentRow()
        if index<0:
            return
        product=self.products[index]
        self.lineEditProductId.setText(product.proid)
        self.lineEditProductName.setText(product.proname)
        self.lineEditPrice.setText(str(product.price))
        self.lineEditQuantity.setText(str(product.quantity))
        self.lineEditCateId.setText(product.cateid)
    def clear_product_detail(self):
        self.lineEditProductId.setText("")
        self.lineEditProductName.setText("")
        self.lineEditPrice.setText(str(""))
        self.lineEditQuantity.setText(str(""))
        self.lineEditCateId.setText("")
        self.lineEditProductId.setFocus()
    def save_product(self):
        #step 1: Create a Product Object:
        proid=self.lineEditProductId.text()
        proname=self.lineEditProductName.text()
        price=float(self.lineEditPrice.text())
        quantity=int(self.lineEditQuantity.text())
        cateid=self.lineEditCateId.text()
        product=Product(proid,proname,price,quantity,cateid)
        #step 2: write object into hard disk
        index=self.dc.find_index_product(product.proid)
        if index==-1:
            self.dc.save_new_product(product)
        else:
            self.dc.save_update_product(product)
        #step 3: reload database
        if self.selected_cate==None:
            self.products=self.dc.get_all_products()
        else:
            cateid=self.selected_cate.cateid
            self.products=self.dc.get_products_by_category(cateid)
        self.show_products_gui()
    def delete_product(self):
        proid=self.lineEditProductId.text()

        msgbox=QMessageBox(self.MainWindow)
        msgbox.setText("Ê muốn xóa sản phẩm ["+proid+"] này hả?")
        msgbox.setWindowTitle("Xác nhận xóa")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec()==QMessageBox.StandardButton.No:
            return #No action, cuz customer selects NO
        self.dc.delete_product(proid)
        if self.selected_cate == None:
            self.products = self.dc.get_all_products()
        else:
            cateid = self.selected_cate.cateid
            self.products = self.dc.get_products_by_category(cateid)
        self.show_products_gui()

    # def exit_program(self):
    #     msgbox = QMessageBox(self.MainWindow)
    #     msgbox.setText('Muốn thoát phần mềm hả?')
    #     msgbox.setWindowTitle("Xác nhận thoát")
    #     msgbox.setIcon(QMessageBox.Icon.Critical)
    #     buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    #     msgbox.setStandardButons(buttons)
    #     if msgbox.exec() == QMessageBox.StandardButton.Yes:
    #         exit()  # No action, cuz customer selects No
    #     def __init__(self):
#         self.dc=DataConnector()
#         self.categories =[]
#         self.products =[]
#         # self.categories=self.dc.get_all_categories()
#         # self.products=self.dc.get_all_products()
#         self.selected_cate=None
#     def setupUi(self,MainWindow):
#         super().setupUi(MainWindow)
#         self.MainWindow = MainWindow
#         self.show_categories_gui()
#         self.show_products_gui()
#         self.setupSignalAndSlot()
#     def showWindow(self):
#         self.MainWindow.show()
#     def show_categories_gui(self):
#         #clear all previous data from QListWidget
#         self.listWidgetCategory.clear()
#         # load cate objects into QListWidget
#         for cate in self.categories:
#             cate_item=QListWidgetItem(str(cate))
#             self.listWidgetCategory.addItem(cate_item)
#     def show_products_gui(self):
#         self.tableWidgetProduct.setRowCount(0)
#         for product in self.products:
#             row=self.tableWidgetProduct.rowCount()
#             self.tableWidgetProduct.insertRow(row)
#             col_proid=QTableWidgetItem(product.proid)
#             col_proname=QTableWidgetItem(product.proname)
#             col_price=QTableWidgetItem(product.price)
#             col_quantity=QTableWidgetItem(product.quantity)
#             col_cateid=QTableWidgetItem(product.cateid)
#             #set column for row
#             self.tableWidgetProduct.setItem(row, 0, col_proid)
#             self.tableWidgetProduct.setItem(row, 1, col_proname)
#             self.tableWidgetProduct.setItem(row, 2, col_price)
#             self.tableWidgetProduct.setItem(row, 3, col_quantity)
#             self.tableWidgetProduct.setItem(row, 4, col_cateid)
# #to do nhung san pham co gia tu 800 den 1000
#             if product.price>=800 and product.price<=1000:
#                 col_proid.setBackground(Qt.GlobalColor.red)
#                 col_proname.setBackground(Qt.GlobalColor.red)
#                 col_price.setBackground(Qt.GlobalColor.red)
#                 col_quantity.setBackground(Qt.GlobalColor.red)
#                 col_cateid.setBackground(Qt.GlobalColor.red)
#
#     def setupSignalAndSlot(self):
#         self.listWidgetCategory.itemSelectionChanged.connect(self.filter_product)
#         self.tableWidgetProduct.itemSelectionChanged.connect(self.show_detail_product)
#         self.pushButtonClear.clicked.connect(self.clear_product_detail)
#         self.pushButtonSave.clicked.connect(self.save_product)
#         self.pushButtonDelete.clicked.connect(self.delete_product)
#         self.actionExit.triggered.connect(self.exit_program)
#         self.actionExport.triggered.connect(self.export_to_excel)
#         self.actionExcel_File_Import.triggered.connect(self.import_from_excel)
#         # self.actionHelp.
#
#     def filter_product(self):
#         row=self.listWidgetCategory.currentRow()
#         if row<0:
#             return
#         self.selected_cate=self.categories(row)
#         self.product=self.dc.get_products_by_categories(self.selected_cate.cateid)
#         self.show_products_gui()
#
#     def show_detail_product(self):
#         index=self.show_detail_product.currentRow()
#         if index < 0:
#             return
#         product=self.products[index]
#         self.lineEditProductId.setText(product.proid)
#         self.lineEditProductName.setText(product.proname)
#         self.lineEditPrice.setText(product.price)
#         self.lineEditQuantity.setText(product.quantity)
#         self.lineEditCateId.setText(product.cateId)
#
#     def clear_product_detail(self):
#         self.lineEditProductId.setText("")
#         self.lineEditProductName.setText("")
#         self.lineEditPrice.setText("")
#         self.lineEditQuantity.setText("")
#         self.lineEditCateId.setText("")
#         self.lineEditProductId.setFocus() # Thay con tro chuot
#
#     def save_product(self):
#         proid=self.lineEditProductId.text()
#         proname=self.lineEditProductName.text()
#         price=self.lineEditPrice.text()
#         quantity=int(self.lineEditQuantity.text())
#         cateId=self.lineEditCateId.text()
#         product=Product(proid,proname,price,quantity,cateId)
#         # step 2 luu xun o cung
#         index=self.dc.find_index_product(product.proid)
#         if index==-1:
#             self.dc.save_new_product(product)
#         else:
#             self.dc.save_update_product(product)
#
#         # step 3 reload database
#         if self.selected_cate==None:
#             self.products=self.dc.get_all_products()
#         else:
#             cateid=self.selected_cate.cateid
#             self.products=self.dc.get_products_by_categories(cateid)
#
#     def delete_product (self):
#         proid=self.lineEditProductId.text()
#
#         msgbox=QMessageBox(self.MainWindow)
#         msgbox.setText('e mun xoa ha')
#         msgbox.setWindowTitle("xac nhan xoa")
#         msgbox.setIcon(QMessageBox.Icon.Critical)
#         buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
#         msgbox.setStandardButons(buttons)
#         if msgbox.exec()==QMessageBox.StandardButton.No:
#             return #No action, cuz customer selects No
#
#         self.dc.delete_product(proid)
#         if self.selected_cate==None:
#             self.products=self.dc.get_all_products()
#
#             cateid=self.selected_cate.cateid
#             self.products=self.dc.get_products_by_categories(cateid)
#         self.show_products_gui()



# On toi day laf du thi GK, tuong tac, xu ly file
#     def exit_program(self):
#         msgbox = QMessageBox(self.MainWindow)
#         msgbox.setText('Muốn thoát phần mềm hả?')
#         msgbox.setWindowTitle("Xác nhận thoát")
#         msgbox.setIcon(QMessageBox.Icon.Critical)
#         buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
#         msgbox.setStandardButons(buttons)
#         if msgbox.exec() == QMessageBox.StandardButton.Yes:
#             exit()  # No action, cuz customer selects No
    # def export_to_excel(self):
    #      filename="../dataset/product.xlsx"
    #      extool=ExportTool()
    #      extool.export_product_to_excel(filename,self.products)
    #
    #      filename_cate='../dataset/categories.xlxs'
    #      extool.export_categories_to_excel(filename_cate, self.categories)
    #
    #      msgbox = QMessageBox(self.MainWindow)
    #      msgbox.setText('Da export excel thanh cong')
    #      msgbox.setWindowTitle('Thong bao')
    #      msgbox.exec()
    #
    # def import_from_excel(self):
    #     filename = "../dataset/product.xlsx"
    #     filename ='../dataset/categories.xlxs'
    #     extool=ExportTool()
    #     self.categories=extool.import_categories_excel(filename_cate)
    #     self.products=extool.import_products_excel(filename_product)
    #     self.show_categories_gui()
    #     self.show_products_gui()
    # def open_help(self):
    #     file_help='HELP.pdf'
    #     # Ta can mo file help len
    #     # lấy đường dẫn hiện tại của phần mềm:
    #     current_path = os.getcwd()
    #     file_help = f"{current_path}/../assets/{file_help}"
    #     webbrowser.open_new(file_help)
    #
    #
    #





















