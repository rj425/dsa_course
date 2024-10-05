# Creating dictionary


# Using the dict() constructor
my_dict1 = dict()
print(my_dict1)

# OR
my_dict2 = {}
print(my_dict2)

# Examples
eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)

eng_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng_sp)

eng_sp = dict([('one', 'uno'), ('two', 'dos'), ('three', 'tres')])
print(eng_sp)


# Update/ add an element to the dictionary

# Update
my_dict = {'name': 'Edy', 'age': 26}
print(my_dict)
my_dict['age'] = 27
print(my_dict)

# Addition
my_dict['address'] = 'Downtown'
print(my_dict)


# Traversing through a dictionary
def traverse_dict(my_dict):
    for key in my_dict:
        print(key, my_dict[key])


traverse_dict(my_dict)


# Search for an element in a Dictionary
def search_dict(my_dict, value):
    for key in my_dict:
        if my_dict[key] == value:
            return key, value
    return 'The value does not exist'


print(search_dict(my_dict, 26))
print(search_dict(my_dict, 27))


# Delete/remove an element in a dictionary
# Using the del keyword
my_dict = {'name': 'Edy', 'age': 26,
           'address': 'Downtown', 'phone': '1234567890'}
del my_dict['age']
print(my_dict)

# Using the pop() method
my_dict.pop('address', None)
print(my_dict)

# Deleting the last inserted item
my_dict.popitem()
print(my_dict)

# Using the clear method to empty the dictionary
my_dict.clear()
print(my_dict)


# Dictionary Methods
my_dict = {'name': 'Edy', 'age': 26,
           'address': 'Downtown', 'phone': '1234567890'}

# Ccopy() method
my_dict2 = my_dict.copy()
print(my_dict2)

# clear() method
my_dict2.clear()
print(my_dict2)

# fromkeys() method
new_dict = {}.fromkeys([1, 2, 3], 0)
print(new_dict)

# get() method
print(my_dict.get('name'))
print(my_dict.get('education', 'masters'))

# items() method
print(my_dict.items())

# keys() method
print(my_dict.keys())

# values() method
print(my_dict.values())

# popitem() method
print(my_dict.popitem())
print(my_dict)

# setdefault() method
print(my_dict.setdefault('address', 'London'))
print(my_dict.setdefault('education', 'masters'))
print(my_dict)

# pop() method
print(my_dict.pop('education'))

# update() method
my_dict.update({'education': 'masters'})
print(my_dict)


# Dictionary Operations

# Membership Test
my_dict = {'name': 'Edy', 'age': 26,
           'address': 'Downtown', 'phone': '1234567890'}
print('name' in my_dict)
print(26 in my_dict.values())

# length
print(len(my_dict))

# all() method - returns True if all keys of the dictionary are True(1,2,anyvalue)
# all() method - returns false if any key of the dictionary is False(0)
print(all(my_dict))

# any() method - returns True if any key of the dictionary is True(1,2,anyvalue)
# any() method - returns False if all keys of the dictionary are False(0)
print(any(my_dict))

# sorted() method
print(sorted(my_dict))


# Dictionary Comprehension
import random

city_names = ["Delhi", "Bangalore", "Chennai", "Mumbai"]

city_temps = {city: random.randint(30,40) for city in city_names}
print(city_temps)
city_temps ={city:temp for city, temp in city_temps.items() if temp > 35}
print(city_temps)