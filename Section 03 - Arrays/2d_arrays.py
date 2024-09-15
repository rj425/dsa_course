import numpy as np

print("# Creating a 2D array")
twoDArray = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
])
print(twoDArray)
print("Time Complexity : O(mn)")
print("Space Complexity : O(mn)")

print()
print()

print("# Insertion in a 2D array")
print("## Adding column to the begining of array (axis=1 for column)")
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)
print(newTwoDArray)

print("Adding a new row at the 2nd place (axis=0 for row)")
newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

print("Insertion at the end using append function")
newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

print()
print()

print("# Accessing elements in a 2D array")
print(twoDArray)
print("a[i][j] -> i is row index and j is column index")

def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= array.shape[0] or columnIndex >=array.shape[1]:
        return "Index out of bound"
    else:
        return array[rowIndex][columnIndex]

print("Accessing element at 2nd row and 3rd column")
print(accessElements(twoDArray, 1, 2))
print("Accessing element at 3rd row and 4th column")
print(accessElements(twoDArray, 2, 3))
print("Time Complexity : O(1)")
print("Space Complexity : O(1)")

print()
print()

print("# Traversal in a 2D array")
print(twoDArray)

def traverse(array):
    for row in range(array.shape[0]):
        for column in range(array.shape[1]):
            print(twoDArray[row][column])

traverse(twoDArray)
print("Time Complexity : O(mn)")
print("Space Complexity : O(1)")

print()
print()

print("# Searching through a 2D array (Linear Search)")
print(twoDArray)

def search(array, element):
    for row in range(array.shape[0]):
        for column in range(array.shape[1]):
            if array[row][column] == element:
                return f"Element found at ({row},{column})"
    return "Element not found"

print("Searching for element 17")
print(search(twoDArray, 17))
print("Searching for element 55")
print(search(twoDArray, 55))
print("Time Complexity : O(mn)")
print("Space Complexity : O(1)")

print()
print()

print("# Deletion in a 2D array")
print(twoDArray)
print("Deleting first row")
newTwoDArray = np.delete(twoDArray, 0, axis=0)
print(newTwoDArray)
print("Deleting second column")
newTwoDArray = np.delete(twoDArray, 1, axis=1)
print(newTwoDArray)
print("Time Complexity : O(mn)")
print("Space Complexity : O(mn)")



