# Question -  How to check if an array contains a number

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                   12, 13, 14, 15, 16, 17, 18, 19, 20])


def findNumber(array, number):
    for i, num in enumerate(array):
        if num == number:
            return f"{num} found at {i}!"
    return f"{number} not found!"


print(findNumber(myArray, 21))
