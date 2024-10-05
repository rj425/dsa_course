# 2D Lists
# Given 2D list calculate the sum of diagonal elements.

# Example

# my_list_2d= [[1,2,3],[4,5,6],[7,8,9]]

# diagonal_sum(my_list_2d) # 15

def diagonal_sum(lst):
    sum = 0
    for num in range(len(lst)):
        sum += lst[num][num]
    return sum


my_list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(my_list_2d))
