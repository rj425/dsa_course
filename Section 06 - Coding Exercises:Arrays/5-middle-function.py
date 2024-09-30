# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# my_list = [1, 2, 3, 4]
# middle(my_list)  # [2,3]

def middle(lst):
    return lst[1:-1]


my_list = [1, 2, 3, 4]
print(middle(my_list))
