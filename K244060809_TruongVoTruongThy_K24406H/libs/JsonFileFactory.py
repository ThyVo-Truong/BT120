import json

class LuuTruJSON:
    @staticmethod
    def ghi_du_lieu(danh_sach, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([obj.__dict__ for obj in danh_sach], file, indent=4, ensure_ascii=False)

    @staticmethod
    def doc_du_lieu(filename, lop_doi_tuong):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                du_lieu = json.load(file)
                return [lop_doi_tuong(**obj) for obj in du_lieu]
        except FileNotFoundError:
            print(f"⚠ File {filename} không tồn tại!")
            return []
