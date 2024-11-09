import numpy as np
print("1D array")
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
print("2D array")
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
print("3D array")
arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                 [[10,11,12],[13,14,15],[16,17,18]],
                 [[19,20,21],[22,23,24],[25,26,27]]
                 ])
print(arr2)


print("\n\nArray information : ")

print("Shape of array : ",arr2.shape)
print("Size of array : ",arr2.size)
print("Data type of array : ",arr2.dtype)
print("No of Dimensions : ",arr2.ndim)
print("Item Siz")