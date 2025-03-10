import xlsxwriter as xr
class ExportTool:
    def export_products_to_excel(self,filename,products):
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # Modify column width
        worksheet.set_column('A:A', 15)
        worksheet.set_column('B:B', 25)
        worksheet.set_column('C:C', 15)
        worksheet.set_column('D:D', 15)
        worksheet.set_column('E:E', 15)

        bold = workbook.add_format({'bold': True})
        # Add header
        worksheet.write('A1', 'Product ID', bold)
        worksheet.write('B1', 'Product Name', bold)
        worksheet.write('C1', 'Unit Price', bold)
        worksheet.write('D1', 'Quantity', bold)
        worksheet.write('E1', 'Cate ID', bold)
        for i in range(len(products)):
            index=i+2
            p=products[i]
            worksheet.write(f'A{index}', p.proid)
            worksheet.write(f'B{index}', p.proname)
            worksheet.write(f'C{index}', p.price)
            worksheet.write(f'D{index}', p.quantity)
            worksheet.write(f'E{index}', p.cateid)
        workbook.close()