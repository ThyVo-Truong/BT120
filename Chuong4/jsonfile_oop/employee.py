class Employee:
    def __init__(self,id=None, name=None, email=None):
        self.id=id
        self.name=name
        self.email=email
    def __str__(self):
        return f'{self.id}\t{self.name}\t{self.email}'
