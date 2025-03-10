class Device:
    def __init__(self):
        self.id="DEVICE1"
        self.name="DEVICE 1 - Name of sample"
    def __str__(self):
        return f"{self.id}\t{self.name}"
d1=Device()
print(d1)
d2=Device()
print("Thong tin D2:")
print(d2)
