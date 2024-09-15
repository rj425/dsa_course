print("# Lists")

print("## Integer List")
integers = [1, 2, 3, 4, 5]
print(integers)

print("## String List")
stringList = ['apple', 'banana', 'cherry']
print(stringList)

print("## Mixed List")
mixedList = [1, 'apple', 2, 'banana', 3, 'cherry']
print(mixedList)

print("## Nested List")
nestedList = [['apple', 'banana'], [1, 2, 3]]
print(nestedList)

print()
print()

print("# Accessing/traversing List")
shoppingList = ['apple', 'banana', 'cherry', 'dates', 'eggplant']
print(shoppingList)
print("## Accessing List")
print(shoppingList[0])
print('apple' in shoppingList)
print(shoppingList[-1])

print("## Traversing List")
for i in shoppingList:
    print(i)

print()
print()

print("# Update/Insert in list")
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
print("## Update List")
myList[2] = 33
print(myList)
myList[4] = 55
print(myList)
print("## Insert in List (insert, append, extend, slice)")
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList.insert(0, 11)
print(myList)
myList.append(55)
print(myList)
newList = [11, 12, 13, 14]
myList.extend(newList)
print(myList)
myList[:2] = ['x', 'y']
print(myList)

print()
print()

print("# Delete from List")
myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("## Delete from List (pop)")
print(myList)
myList.pop(1)
print(myList)
myList.pop()
print("## Delete from List (del)")
print(myList)
del myList[1:3]
print(myList)
print("## Delete from List (remove)")
myList.remove('f')
print(myList)

print()
print()

print("# Searching for an element in List")
myList = [10,20,30,40,50,60,70,80,90]
target = 50
print("## in operator")
if target in myList:
    print(f"{target} found at index {myList.index(target)}")
else:
    print(f"{target} not found")
print("## Linear Search")
def linearSearch(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1
target = 90
index = linearSearch(myList, target)
print(f"{target} found at index {index}")
 
print()
print()

print("# List operation / functions")
a = [1,2,3]
b = [4,5,6]
print(a)
print(b)
print("## + operator")
c = a + b
print(c)
print("## * operator")
a = a * 4
print(a)
print(f"## Length of list using len(): {len(a)}")
print(f"## Max of list using max(): {max(a)}")
print(f"## Min of list using min(): {min(a)}")
print(f"## Sum of list using sum(): {sum(a)}")
average = sum(a) / len(a)
print(f"## Average of list: {average}")

print()
print()

print("# String and lists")
print("## String to List")
a = "spam"
print(list(a))
print("## Split")
a = "spam-spam1-spam2"
b = a.split('-')
print(b)
print("## Join")
a = '-'.join(b)
print(a)

print()
print()

print("# List comprehension")
prevList = [1, 2, 3, 4, 5]
print(prevList)
newList = [item*2    for item in prevList]
print(newList)

print("# Conditional List comprehension")
prevList = [-1, 10, -20, 2, -90, 60, 45, 20]
print(prevList)
newList = [item for item in prevList if item > 0]
print(newList)
newList = [item*item for item in prevList if item < 0]
print(newList)
print("## Complex list comprehension")
sentence = "My name is Rishabh Jain"
print(sentence)
def isConsonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonantsOnly = [ch for ch in sentence if isConsonant(ch)]
print(''.join(consonantsOnly))
print("## More Complex list comprehension")
prevList = [-1, 10, -20, 2, -90, 60, 45, 20]
print(prevList)
def get_number(number):
    return number if number>0 else "Negative Number"
newList = [get_number(item) for item in prevList]
print(newList)

