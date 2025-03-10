import numpy as np

arr1=np.array([6,6.5,4,5.5,7,8.5])
print(arr1)
print(type(arr1))
print(arr1.dtype)

list_sample=[5,7,6.5,8,9.5]
tuple_sample=(6,4,5.5,8.5)
arr2=np.asarray(list_sample)
arr3=np.asarray(tuple_sample)
print(arr2)
print(arr3)

arr_zeros = np.zeros(4)
arr_ones = np.ones(3, dtype=int)
print(arr_zeros)
print(arr_ones)

arr1 = np.arange(2, 10, 1.5)
arr2 = np.arange(6)
print(arr1)
print(arr2)

arr=np.linspace(5,15,6)
print(arr)
arr1 = np.random.rand(3)
arr2 = np.random.randn(4)
arr3 = np.random.randint(10, 45, 5)
print(arr1)
print(arr2)
print(arr3)

arr1=np.random.uniform(0.0,5.0,20)
print(arr1)

arr2=np.random.normal(5.0,1.0,10000)
print(arr2)

arr = np.random.randint(10, 80, 8)
print(arr)
print(arr[1])
print(arr[-2])
print(arr[[1,3,4]])
print(arr[2:5])
print(arr[arr < 40])

arr = np.random.randint(10, 80, 8)
print(arr)
indices = np.where(arr>40)
print(indices)
print(arr[indices])
print(np.extract(arr>35,arr))
print(np.extract(np.mod(arr,2)==0, arr))

arr = np.random.randint(5, 45, 7)
print(arr)
print(np.min(arr)) # giá trị min
print(np.argmin(arr)) # index phần tử min
print(np.max(arr)) # giá trị max
print(np.argmax(arr)) # index phần tử max
print(np.mean(arr)) # giá trị trung bình
print(np.median(arr)) # giá trị trung vị
print(np.std(arr)) # độ lệch chuẩn

arr = np.array([4, 2, 15, 7, 9, 5, 11, 8])
print(arr)
arr = np.append(arr, [6, 3]) # thêm phần tử vào cuối
print(arr)
arr = np.insert(arr, 2, [6, 1]) # thêm tại vị trí bất kỳ
print(arr)

arr=np.array([4,2,15,7,9,5,11,8])
arr=np.delete(arr,[2,4]) #xóa phần tử theo index
print(arr)

arr=np.array([4,2,15,7,9,5,11,8])
print(np.sort(arr))
print(np.sort(arr)[::-1])

#Tính toán số học
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape) #kich thuoc array(2,3)

arr=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr)
print(arr.shape)

arr=np.zeros([2,3,4],dtype=int)
print(arr)

arr=np.ones([2,3],dtype=int)
print(arr)

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr[0])
print(arr[1][0][2])
print(arr[1][1][1])
print(np.max(arr))
print(np.mean(arr[1]))
print(arr[np.where(arr>8)])

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
arr[1][0][2]=10
print(arr[1],[0])

arr=np.array([[[1,3,2],[6,4,5]],[[7,9,8],[12,10,11]]])
print(np.sort(arr))

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([1,2,3])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

arr1=np.array(range(12))
print(arr1)
arr_reshape=arr.reshape(3,4)
print(arr_reshape)
arr2=arr_reshape.reshape(1,-1)
print(arr2)
arr3=arr_reshape.flatten()
print(arr3)




