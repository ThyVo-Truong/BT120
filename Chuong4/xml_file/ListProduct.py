from xml_file.Product import Product
from xml.dom.minidom import parse


class ListProduct:
    def __init__(self):
        self.products=[]
    def print_all_product(self):
        for p in self.products:
            print(p)
    def import_data_from_xml(self, filename):
        DOMTree = parse("product.xml")
        elements = DOMTree.documentElement

        products = elements.getElementsByTagName("product")
        for p in products:  # p la mot the product
            pro_id = (p.getElementsByTagName("id")[0]).childNodes[0].data
            pro_name = (p.getElementsByTagName("name")[0]).childNodes[0].data
            pro_price = (p.getElementsByTagName("price")[0]).childNodes[0].data
            self.products.append(Product(pro_id,pro_name,pro_price))
            print(pro_id + " -> " + pro_name + " -> " + pro_price)



