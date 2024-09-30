# Best Score
# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# my_list = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(my_list) # 90 87

def first_second(my_list):
    first_best = 0
    second_best = 0
    for score in my_list:
        if score > first_best:
            second_best = first_best
            first_best = score
        elif score < first_best and score > second_best:
            second_best = score
    return first_best, second_best


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))
