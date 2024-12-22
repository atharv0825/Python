import numpy as np

array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])

print("Array 1 :",array1)
print("Array 2 :",array2)

sum_array = array1+array2
print("\n Element-wise Addition : ",sum_array)

sub_array = array1-array2
print("\n Element-wise Subtraction : ",sub_array)

product_array = array1*array2
print("\n Element-wise Product : ",product_array)

scaler_array = array1*2
print("\n Element-wise scaler : ",scaler_array)

matrix = np.array([1,2],[3,4])
matrix1 = np.array([5,6],[7,8])
result_matrix = np.dot(matrix,matrix1)
print("\n Matrix Multiplication : ",result_matrix)

print("Statistical Operations")
print("mean of Array : ",np.mean(array1))
print()