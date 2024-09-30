# Question 2 - Find Pairs
# LeetCode 1 - Two Sum

import random


def find_pairs(numbers, target):
    # Possible Solution : O(n^2)
    length = len(numbers)
    pairs = []
    for i in range(length):
        for j in range(i+1, length):
            if numbers[i]+numbers[j] == target:
                pairs.append([i, j])
    return pairs


def find_pairs_leet_code(numbers, target):
    # LeetCode Solution : O(n)
    pairs = []
    seen = {}
    for i, num in enumerate(numbers):
        complement = target-num
        if complement in seen:
            pairs.append([seen[complement], i])
        seen[num] = i
    return pairs


array = [1, 2, 3, 2, 3, 4, 5, 6]
random.shuffle(array)
target = 6
indices = list(range(len(array)))
print(f"INDEX  : {indices}")
print(f"ARRAY  : {array}")
print(f"TARGET : {target}")

print("\nPAIRS : ")
print(find_pairs(array, target))
print(find_pairs_leet_code(array, target))
