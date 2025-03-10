from excel_file_oop.Student import Student


class MyDump:
    @staticmethod
    def gen_students_dataset():
        students=[]
        students.append(Student('ST1','Teo', 10))
        students.append(Student('ST2','Ty', 10))
        students.append(Student('ST3','Bin', 10))
        students.append(Student('ST4','Bo', 10))
        students.append(Student('ST5','Tun', 10))

