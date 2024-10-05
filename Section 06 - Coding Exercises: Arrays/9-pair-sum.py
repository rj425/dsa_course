# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


# Note:

# 4+3 comes from second and third elements from the main list.

# 3+4 comes from third and seventh elements from the main list.

def pair_sum(my_list, sum):
    pairs = []
    seen = set()
    for num in my_list:
        complement = sum-num
        if complement in seen:
            pairs.append(f"{complement}+{num}")
        seen.add(num)
    return pairs


my_list = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
sum = 7
print(pair_sum(my_list, sum))
