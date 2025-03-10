from Chuong5.ProductManagement.libs.JsonFileFactory import JsonFileFactory
from Chuong5.ProductManagement.models.Category import Category
from Chuong5.ProductManagement.models.Product import Product


class DataConnector:
    def get_all_categories(self):
        categories = []
        jff = JsonFileFactory()
        filename = "../dataset/categories.json"
        categories = jff.read_data(filename, Category)
        return  categories
    def get_all_products(self):
        products = []
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        products = jff.read_data(filename, Product)
        return products
    def get_products_by_category(self,cateid):
        products = self.get_all_products()
        result=[]
        for product in products:
            if product.cateid==cateid:
                result.append(product)
        return result
    def save_new_product(self,product):
        products = self.get_all_products()
        products.append(product)
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        jff.write_data(products, filename)
    def find_index_product(self,proid):
        self.products = self.get_all_products()
        for i in range(len(self.products)):
            product=self.products[i]
            if product.proid==proid:#found
                return i
        return -1
    def save_update_product(self,curent_product):
        index=self.find_index_product(curent_product.proid)
        if index!=-1:
            self.products[index]=curent_product
            jff = JsonFileFactory()
            filename = "../dataset/products.json"
            jff.write_data(self.products, filename)
    def delete_product(self,proid):
        index=self.find_index_product(proid)
        if index!=-1:
            self.products.pop(index)
            jff = JsonFileFactory()
            filename = "../dataset/products.json"
            jff.write_data(self.products, filename)
