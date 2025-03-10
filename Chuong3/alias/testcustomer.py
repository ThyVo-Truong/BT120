from alias.customer import customer

c1=customer("113",'Obama', '0981234567')
c2=customer("114",'Kim Un Un','0905428833')

c1.name='Ho Van A'
print("Thong tin c2 la:")
print(c2)

c5=customer('116', "Newton", "646554")
c3=customer('115','Putin','093253454')
c4=c3
c3=c5
# => Khong co o nho nao bi thu hoi
# Khong phat sinh o nho moi (c4)