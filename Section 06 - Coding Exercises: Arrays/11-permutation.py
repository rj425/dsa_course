# Given two strings, write a method to decide if one is permutation of another

# Permutation - Two strings are said to be in permutation, if they have the same characters in different orders.
# Example -
# - peek, keep
# - rail, liar

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


list1 = [1, 2, 3, 4]
list2 = [4, 2, 3, 1]
print(permutation(list1, list2))
list1 = list('peek')
list2 = list('keep')
print(permutation(list1, list2))
list1 = list('abc')
list2 = list('abcd')
print(permutation(list1, list2))
