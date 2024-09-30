# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5]
# max_product(arr) # Output: 63 (9*7)

import random


def max_product(arr):
    max_num1 = 0
    max_num2 = 0
    for num in arr:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        if num < max_num1 and num > max_num2:
            max_num2 = num
    return max_num1 * max_num2


array = [1, 7, 3, 4, 9, 5]
random.shuffle(array)

print(max_product(array))
