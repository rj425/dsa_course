# Common Keys
# Define a function which takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:

# {'a': 1, 'b': 5, 'c': 7, 'd': 5}

def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = dict1.get(key, 0) + value
    return dict1


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))