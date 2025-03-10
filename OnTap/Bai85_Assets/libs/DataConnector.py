from OnTap.Bai85_Assets.libs.JsonFileFactory import JsonFileFactory
from OnTap.Bai85_Assets.models.Asset import Asset
from OnTap.Bai85_Assets.models.Employee import Employee
from OnTap.Bai85_Assets.models.Employee_Asset import Employee_Asset


class DataConnector:
    def get_all_employees(self):
        jff=JsonFileFactory
        filename='../dataset/Employee.json'
        employees=jff.read_data(filename,Employee)
        return employees
    def get_all_assets(self):
        jff=JsonFileFactory
        filename='../dataset/Asset.json'
        assets=jff.read_data(filename, Asset)
        return assets
    def get_all_employee_assets(self):
        jff=JsonFileFactory
        filename='../dataset/Employee_Asset.json'
        eas=jff.read_data(filename, Employee_Asset)
        return eas
