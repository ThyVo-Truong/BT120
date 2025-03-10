class Employee:
  def __init__(self,id,name,age):
      self.id=id
      self._name=name
      self.__age=age
  def __str__(self):
      info=f"{self.id}\t{self._name}\t{self.__age}"
      return info
