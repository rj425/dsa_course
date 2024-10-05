# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:

# False

def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for item in lst:
            counter[item] = counter.get(item, 0)+1
        return counter
    same_frequency = count_elements(list1) == count_elements(list2)
    return same_frequency


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))
