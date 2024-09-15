import array

# 1. Create array and traverse
my_array = array.array('i', [1, 2, 3, 4, 5])
for i in my_array:
    print(i)

print()

# 2. Access indvidual elements through indices
print('Step 2')
print(my_array[0])

print()

# 3. Append any value to the array using append() method
print('Step 3')
my_array.append(6)
print(my_array)

print()

# 4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(0, 11)
print(my_array)

print()

# 5. Extend python array using extend() method
print("Step 5")
new_array = array.array('i', [10, 11, 12])
my_array.extend(new_array)
print(my_array)

print()

# 6. Add items from list into array using fromlist() method
print('Step 6')
temp_list = [20, 21, 22]
my_array.fromlist(temp_list)
print(my_array)

print()

# 7. Remove any array element using remove() method
print("Step 7")
my_array.remove(11)
print(my_array)

print()

# 8. Remove last array element using pop() method
print("Step 8")
my_array.pop()
print(my_array)

print()

# 9. Fetch an element through its index using index() method
print("Step 9")
print(my_array.index(21))

# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)

print()

# 11. Get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())

print()

# 12. Check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array)
print(my_array.count(11))

print()

# 13. Convert array to string using tobytes() method
print("Step 13")
array_bytes = my_array.tobytes()
print(array_bytes)
temp_array = array.array('i')
temp_array.frombytes(array_bytes)
print(temp_array)

print()

# 14. Convert array to python list to list() method
print("Step 14")
print(my_array.tolist())

# 15. Slice elements from an array
print("Step 15")
print(my_array[1:4])
