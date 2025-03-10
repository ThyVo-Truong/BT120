class ListStudent:
    def __init__(self):
        self.students=[]
    def add_student(self,st):
        self.students.append(st)
    def add_students(self,arr):
        self.students_extend(arr)
    def print_all_students(self):
        for st in self.students:

    def export_excel(self,filename):
        import xlsxwriter as xr

        workbook = xr.Workbook("Products.xlsx")
        worksheet = workbook.add_worksheet()

        # workbook la 1 file excel
        # worksheet la 1 trang excel

        # Modify column width
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 25)
        worksheet.set_column('C:C', 15)

        bold = workbook.add_format({'bold': True})

        # Add header
        worksheet.write('A1', 'Id', bold)
        worksheet.write('B1', 'Name', bold)
        worksheet.write('C1', 'Price', bold)

        for i in range (len(self.students)):
            index=i+2
            st=self.students[i]
            worksheet.write(f'A')

        # Add first row
        worksheet.write('A2', '1')
        worksheet.write('B2', 'Heineken')
        worksheet.write('C2', '19000')

        # Add second row
        worksheet.write('A3', '2')
        worksheet.write('B3', 'Tiger')
        worksheet.write('C3', '18000')

        # Insert image
        worksheet.insert_image('B5', 'beer.png')

        workbook.close()



