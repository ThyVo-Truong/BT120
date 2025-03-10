import csv
with open('new_employee.csv', mode='w') as f:
    fieldnames = ['Id', 'Name', 'Dob']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Id': '1', 'Name': 'Tú Linh', 'Dob': '02/02/2002'})
    writer.writerow({'Id': '2', 'Name': 'Nam Giao', 'Dob': '03/04/2000'})
    writer.writerow({'Id': '3', 'Name': 'Huỳnh Anh', 'Dob': '05/11/2001'})
import pandas
df = pandas.read_csv('employee.csv', index_col="Id")
df.to_csv('another_employee.csv')

