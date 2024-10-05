# Note-1: 
# Tuples are similar to lists, but they are immutable, 
# meaning they cannot be changed after they are created.

# Note-2:
# Generally use hetrogeneous data types in a tuple and homogeneous data types in a list.
# Iterating through a tuple is faster than a list.

# How to create a tuple?
new_tuple = "a", "b", "c", "d", "e"
print(new_tuple)

new_tuple = ("a", "b", "c", "d", "e")
print(new_tuple)

new_tuple = ("a",)
print(new_tuple)

new_tuple = tuple("abcde")
print(new_tuple)

new_tuple = tuple(["a", "b", "c", "d", "e"])
print(new_tuple)


# How to access elements in a tuple?
print(new_tuple[1])
print(new_tuple[-1])
print(new_tuple[1:3])

# TypeError: 'tuple' object does not support item assignment
# new_tuple[0] = 1


# How to traverse a tuple?
for item in new_tuple:
    print(item)

for i in range(len(new_tuple)):
    print(new_tuple[i])


# Search for an element in a tuple
print("a" in new_tuple)
print("f" in new_tuple)
print(new_tuple.index("a"))
 
def search_tuple(my_tuple, value):
    for index, item in enumerate(my_tuple):
        if item == value:
            return f"The {item} exists at index {index}"
    return "The value does not exist" 

print(search_tuple(new_tuple, "b"))


# Tuple Operations/functions

tuple_a = (1, 2, 3, 4, 5)
tuple_b = (6, 7, 8, 9, 10)
print(tuple_a + tuple_b)
print(tuple_a * 2)

print(4 in tuple_a)

print(tuple_a.count(4))

print(tuple_a.index(4))


# Tuple vs List
list1 = [0, 1, 2, 3, 4, 5]
list1[1] = 3
print(list1)