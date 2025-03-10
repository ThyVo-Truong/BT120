from excel_file_oop.ListStudent import ListStudent
from excel_file_oop.mydump import MyDump

ls = ListStudent()
arr=MyDump.gen_students_dataset()
ls.add_students(arr)
print('List of Gen Students:')
ls.print_all_students()