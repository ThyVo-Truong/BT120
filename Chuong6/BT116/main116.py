import numpy as np

arr=np.random.randint(-100,500,10)
#cau1
print(arr)
#cau2
arr2=arr[2:6]
print(arr2)
#cau3
arr3=arr[arr<0]
print(arr3)
indices=np.where(arr<0)
arr3_2=arr[np.where(arr<0)]
print(arr3_2)
arr3_3=np.extract(arr<3,arr)
print(arr3_3)
#cau4
x=300
y=500
arr4=arr[arr>=x]
arr4=arr4[arr4<=y]
print('arr4=',arr4)