# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]

def remove_duplicates(arr):
    seen = set()
    new_arr = []
    for num in arr:
        if num not in seen:
            new_arr.append(num)
            seen.add(num)
        else:
            pass
    return new_arr


array = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(array))
