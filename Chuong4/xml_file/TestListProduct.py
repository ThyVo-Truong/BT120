from xml_file.ListProduct import ListProduct

lp=ListProduct()
filename='product.xml'
lp.import_data_from_xml(filename)
print('List of Products after importing:')
lp.print_all_product()