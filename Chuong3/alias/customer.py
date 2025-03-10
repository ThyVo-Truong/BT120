import copy
class customer:
    def __init__(self,id,name,phone):
        self.id=id
        self.name=name
        self.phone=phone
    def __str__(self):
        inf=f"{self.id}\t{self.name}\t{self.phone}"
        return inf
    def clone(self):
        return copy.copy(self)
