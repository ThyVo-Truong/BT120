#thu nghiem tinh ke thua...
from inherit_demo.FulltimeEmployee import FulltimeEmployee
from inherit_demo.ParttimeEmployee import ParttimeEmployee
from inherit_demo.StaffManagement import StaffManagement

staff=StaffManagement()
staff.add_employee(ParttimeEmployee('e1', 'Teo',5))
staff.add_employee(ParttimeEmployee('e2', 'Ty',2))
staff.add_employee(FulltimeEmployee('e3', 'Bin'))
staff.add_employee(FulltimeEmployee('e4', 'Bo'))
staff.add_employee(FulltimeEmployee('e5', 'Tun'))
staff.add_employee(ParttimeEmployee('e6', 'Run',7))
staff.add_employee(FulltimeEmployee('e7', 'Bun'))
print("DS nhan su toan cong ty la:")
staff.print_employees()

print('------------'*2)
staff_fulltime=staff.get_fulltime_employees()
print('So nhan vien chinh thuc=',len(staff_fulltime.employees))
print('DS nhan vien chinh thuc nay la:')
staff_fulltime.print_employees()

print('------------'*2)
staff_parttime=staff.get_parttime_employees()
print('So nhan vien thoi vu=',len(staff_parttime.employees))
print('DS nhan vien thoi vu nay la:')
staff_parttime.print_employees()



