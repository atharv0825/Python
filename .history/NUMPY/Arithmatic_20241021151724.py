import numpy as np

arr1 = np.array([[1, 2, 3], 
                  [4, 5, 6]])
arr2 = np.array([[10, 20, 30], 
                  [40, 50, 60]])

print("Array 1 : \n",arr1)
print("Array 2 : \n",arr2)

print("Element-wise Addition: ",np.add(arr1,arr2))