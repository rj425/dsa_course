# Question -  How to check if an array contains a number

import numpy as np


def find_number(array, number):
    for i, num in enumerate(array):
        if num == number:
            return f"{num} found at {i}!"
    return f"{number} not found!"


my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                     12, 13, 14, 15, 16, 17, 18, 19, 20])
print(find_number(my_array, 21))
