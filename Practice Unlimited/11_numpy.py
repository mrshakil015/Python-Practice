import numpy as np

array1 = np.array([1,2,3,4])
print("One dimensional array",array1)

listarray = np.array([(1,2,3,8),(5,6,4,7),(3,5,7,2)])
print("Original array: ",listarray)
print("Array dimension: ",listarray.ndim)
print("Array Data Type: ",listarray.dtype)
print("Array item size: ",listarray.itemsize)
print("Array size: ",listarray.size)
print("Array shape: ",listarray.shape)
listarray2 = np.array([(1,2,3,8),(5,6,54,7),(3,5,7,2)])
print("Original array:\n",listarray2)
print("Reshape the array:\n",listarray2.reshape(6,2))
array3= listarray2.copy()
print("Copy value one array to another:\n",array3)
array4 = np.array([25,8,97,16])
print("Array4: ",array4)
array4[1] = 44
print("Another array: ",array4)

print("Iterate on the elements of the 1-D array")
for y in array4:
    print(y)
print("Iterate on the elements of the 2-D array")
for x in array3:
    for y in x:
        print(y)


print("Array3: ",array3)
print("Find max number from Array3: ",array3.max())
print("Find min number from Array3: ",array3.min())
print("Summation of Array3: ",array3.sum())
print("Column wise Summation of Array3: ",array3.sum(axis=0))
print("Row wise Summation of Array3: ",array3.sum(axis=1))
print("Square root of array4: ",np.sqrt(array4))
print("Arange: ",np.arange(10))
print("Array4: ",array4)
array5= np.array([4,22,7,33,132])
print("Search value index: ",np.searchsorted(array5,132))
print("Search value index using where: ",np.where(array5 == 7))
print("Search value odd value index: ",np.where(array5%2 == 1))
print("Search value even value index: ",np.where(array5%2 == 0))
print("Maximum Value index: ",array4.argmax())
print("Minimum Value index: ",array4.argmin())
