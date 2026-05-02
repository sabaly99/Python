import numpy as np

array = np.array([1,2,34,5,6,7])

print("array: ",array)

# matrix creation using array
matrix = np.array([[1,235,6,7,8],[34,345,6,876,3]])
print("matrix:\n",matrix)
#for spacing out the output that we get
print('\n' * 2)

#Arithmetic operations on arrays
array1 = np.array([2,5,7,8,9,3])
array2 = np.array([5,1,5,0,7,0])

print('\n' * 2)
#addition
sum_array = array1 + array2
#subtraction
sub_array= array1 - array2
#multiplication
mult_array = array1 * array2

print(f" sum: {sum_array}\n diff:{sub_array}\n multiplication:{mult_array}")

#multiplying through an array by a scalar value
scalar = 5
scaled1 = array1 * scalar
print(f"scaled values are: {scaled1}")