from jsonfile_oop.JsonFileFactory import JsonFileFactory
from jsonfile_oop.ListEmployee import ListEmployee
from jsonfile_oop.employee import Employee

le=ListEmployee()
jff=JsonFileFactory()
arr=jff.read_data('employees.json', Employee)
le.add_employees(arr)
print('List of Employee after Deserializing:')
le.print_all_employees()
