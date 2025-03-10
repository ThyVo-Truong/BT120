
class device:
    numberofdevice=0
    def __init__(self,id,name,value):
        self.id=id
        self.name=name
        self.value=value
        device.numberofdevice+=1
    def __str__(self):
        infor = f"{self.id}\t{self.name}\t{self.value}"
        return infor
    @staticmethod
    def printnumberdevice():
        print("Number of Devices=", device.numberofdevice)