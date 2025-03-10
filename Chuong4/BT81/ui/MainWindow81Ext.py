from PyQt6.QtWidgets import QLabel, QMainWindow
import xml.etree.ElementTree as ET

from BT81.ui.MainWindow81 import Ui_MainWindow


class MainWindow81Ext(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButtonSave.clicked.connect(self.add_employee)
        self.pushButtonRemove.clicked.connect(self.remove_employee)
        self.pushButtonSearchID.clicked.connect(self.search_employee)
        self.pushButtonSortEmployees.clicked.connect(self.sort_employees)

        self.load_employees()

    def load_employees(self):
        '''Hiển thị danh sách nhân viên từ XML'''
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        for emp in root.findall('employee'):
            emp_id = emp.find('id').text
            emp_name = emp.find('name').text
            label = QLabel(f'{emp_id} - {emp_name}')
            self.verticalLayoutEmployees.addWidget(label)

    def add_employee(self):
        '''Thêm nhân viên mới'''
        emp_id = self.lineEditID.text()
        emp_name = self.lineEditName.text()

        if not emp_id or not emp_name:
            return

        tree = ET.parse('employees.xml')
        root = tree.getroot()

        new_emp = ET.Element('employee')
        ET.SubElement(new_emp, 'id').text = emp_id
        ET.SubElement(new_emp, 'name').text = emp_name
        root.append(new_emp)

        tree.write('employees.xml', encoding='utf-8')

        label = QLabel(f'{emp_id} - {emp_name}')
        self.verticalLayoutEmployees.addWidget(label)

    def remove_employee(self):
        '''Xóa nhân viên theo ID'''
        emp_id = self.lineEditID.text()
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        target = None
        for emp in root.findall('employee'):
            if emp.find('id').text == emp_id:
                target = emp
                break

        if target is not None:
            root.remove(target)
            tree.write('employees.xml', encoding='utf-8')
            self.reload_ui()

    def search_employee(self):
        '''Tìm nhân viên theo ID'''
        emp_id = self.lineEditID.text()
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        found = None
        for emp in root.findall('employee'):
            if emp.find('id').text == emp_id:
                found = emp.find('name').text
                break

        if found:
            self.lineEditName.setText(found)
        else:
            self.lineEditName.setText('Không tìm thấy!')

    def sort_employees(self):
        '''Sắp xếp nhân viên theo ID'''
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        employees = sorted(root.findall('employee'), key=lambda x: int(x.find('id').text))

        root.clear()
        for emp in employees:
            root.append(emp)

        tree.write('employees.xml', encoding='utf-8')
        self.reload_ui()

    def reload_ui(self):
        '''Cập nhật lại danh sách trên giao diện'''
        while self.verticalLayoutEmployees.count():
            item = self.verticalLayoutEmployees.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.load_employees()
