# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5]
# max_product(arr) # Output: 63 (9*7)

import random


def max_product(arr):
    maxNum1 = 0
    maxNum2 = 0
    for num in arr:
        if num > maxNum1:
            maxNum2 = maxNum1
            maxNum1 = num
        if num < maxNum1 and num > maxNum2:
            maxNum2 = num



array = list(range(40))
random.shuffle(array)

max_product(array)
