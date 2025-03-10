
from jsonfile_oop.JsonFileFactory import JsonFileFactory
from jsonfile_oop.ListEmployee import ListEmployee
from jsonfile_oop.mydump import mydump

le=ListEmployee()
arr_emp_dump=mydump.gen_sample_employees()
le.add_employees(arr_emp_dump)
print('List of Employees after Serialize:')
le.print_all_employees()
jff=JsonFileFactory()
jff.write_data(le.employees, 'employee.csv.json')
