import numpy as np

# Array Creation and generation
print("Array Creation and generation: ")
array1D = np.array([2, 5, 7], dtype=np.uint32)
array2D = np.array([[2, 3, 5], [4, 6, 8], [4, 7, 3]])
array3D = np.array([[[3, 6, 3], [5, 7, 5]], [[4, 6, 3], [5, 7, 4]]])


print("1 dimensional array", array1D)
print("2 dimensional array", array2D)
print("3 dimensional array", array3D)

seq1 = np.arange(2, 3, 0.1)
seq2 = np.arange(10)

print("np.arange(2(start value), 3(end value), 0.1(step))", seq1)
print("np.arange(10(start value))", seq2)

arr = np.linspace(2, 3, 6)
print("np.linspace(2(start), 3(stop), 6(no of equidistance values))", arr)

arr2D = np.vander(np.linspace(0, 2, 5), 2)
print("np.vander(np.linspace(0, 2, 5), 2)", arr2D)

zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((2, 3, 2))

print("zeros array:", zeros_arr)
print("ones array:", ones_arr)

# INDEXING
print("Indexing: ")
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])

ar = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd dim: ", ar[1, -1])


# Manipulation
print("Manipulation: ")
x = np.arange(35)
print("x =", x)
y = x.reshape((7, 5))

print("x.reshape((7, 5))", y)

a = np.array([3, 2, 0, 1])

print("sorting", np.sort(a))

b = np.array(["banana", "cherry", "apple"])

print("sorting", np.sort(b))

print("Accessing elements using some condition")
z = np.array([41, 42, 43, 44])
condition = [True, False, True, False]

newarr = z[condition]
print("array", z)
print("condition", condition)
print("new array", newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr1)
print(arr2)
print("Concatenation", arr3)

arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6 = np.concatenate((arr4, arr5), axis=1)
print(arr4)
print(arr5)
print("Concatenation", arr6)
