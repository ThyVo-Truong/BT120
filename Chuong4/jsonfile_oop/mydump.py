from jsonfile_oop.employee import Employee


class mydump:
    @staticmethod
    def gen_sample_employees():
        employees=[]
        employees.append(Employee('e1', 'Teo', 'teo@gmail.com'))
        employees.append(Employee('e2', 'Ty', 'ty@gmail.com'))
        employees.append(Employee('e3', 'Bin', 'bin@gmail.com'))
        employees.append(Employee('e4', 'Bo', 'bo@gmail.com'))
        employees.append(Employee('e5', 'Tun', 'tun@gmail.com'))
        return employees
    
