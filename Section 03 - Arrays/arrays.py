import array
# import numpy as np


print("# Creation")

## Using in-built array module
my_array =  array.array('i')
print(my_array)

my_array = array.array('i',[1,3,2,4,9])
print(my_array)

## Using numpy module
# np_array = np.array([], dtype=int)
# print(np_array)

# np_array1 = np.array([1,2,3,4])
# print(np_array1)


print("# Insertion")
print(my_array)
my_array.insert(0, 6)
print(my_array)


print("# Traversal Operation")
def traversalArray(array):
    for i in array:
        print(i)

print(my_array)
traversalArray(my_array)


print("# Access array")

def accessElement(array, index):
    if index >= len(array):
        print(f"There is no element in {index} index!")
    else:
        print(array[index])

print(my_array)
accessElement(my_array, 3)


print("# Search")

def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(my_array)
print(linearSearch(my_array, 2))
print(linearSearch(my_array, 0))


print("# Deletion")

print(my_array)
my_array.remove(3)
print(my_array)
