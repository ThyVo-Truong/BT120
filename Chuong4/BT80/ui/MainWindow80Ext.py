from PyQt6.QtWidgets import QLabel, QMainWindow

from BT80.libs.FileFactory import FileFactory
from BT80.models.Product import Product
from BT80.ui.MainWindow80 import Ui_MainWindow


class MainWindow80Ext(QMainWindow, Ui_MainWindow):  # Kế thừa cả 2 class
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.products = []
        self.loadProducts()
        self.pushButtonSave.clicked.connect(self.addProduct)
        self.pushButtonRemove.clicked.connect(self.removeProduct)
        self.pushButtonAscSort.clicked.connect(self.sortAsc)
        self.pushButtonDescSort.clicked.connect(self.sortDesc)

    def loadProducts(self):
        self.products = FileFactory.readData('database.txt')
        print("Loaded products:", self.products)  # Kiểm tra xem có sản phẩm nào được load không
        self.displayProducts()

    def displayProducts(self):
        print("Displaying products:", self.products)  # Kiểm tra dữ liệu
        print("Layout object:", self.verticalLayoutProduct)  # Xem layout có tồn tại không
        self.clearLayout(self.verticalLayoutProduct)
        for product in self.products:
            print(f"Adding {product.productId} - {product.productName} - {product.unitPrice}")
            label = QLabel(f'{product.productId} - {product.productName} - {product.unitPrice}')
            self.verticalLayoutProduct.addWidget(label)

    def addProduct(self):
        productId = self.lineEditId.text().strip()
        productName = self.lineEditName.text().strip()
        try:
            unitPrice = float(self.lineEditPrice.text().strip())
        except ValueError:
            return

        new_product = Product(productId, productName, unitPrice)
        self.products.append(new_product)
        FileFactory.writeData('database.txt', new_product)
        self.displayProducts()

    def removeProduct(self):
        productId = self.lineEditId.text().strip()
        self.products = [p for p in self.products if p.productId != productId]
        self.updateFile()
        self.displayProducts()

    def sortAsc(self):
        self.products.sort(key=lambda p: p.unitPrice)
        self.displayProducts()

    def sortDesc(self):
        self.products.sort(key=lambda p: p.unitPrice, reverse=True)
        self.displayProducts()

    def updateFile(self):
        with open('database.txt', 'w', encoding='utf-8') as f:
            for product in self.products:
                f.write(f'{product.productId};{product.productName};{product.unitPrice}\n')

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
