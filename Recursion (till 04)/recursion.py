def factorial(n):
    '''Finds the factorial of number n'''
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"
    # Base case
    if n in [0, 1]:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)


def fibonacci(n):
    '''Finds the nth fibonacci number'''
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"
    # Base case
    if n < 2:
        return n
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sumOfDigits(n):
    '''Finds the sum of digits of a positive integer number '''
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"
    # Base case
    if n == 0:
        return 0
    # Recursive case
    else:
        quotient = n//10
        remainder = n%10
        return remainder + sumOfDigits(quotient)


def power(x, n):
    '''Finds the power of a number'''
    assert int(n) == n, "The exponent number must be a integer only!"
    # Base case
    if n == 0:
        return 1
    # Recursive case
    elif n < 0:
        return (1/x) * power(x, n+1) 
    else:
        return x * power(x, n-1)


def gcd(a, b):
    '''Finds the greatest common divisor of two numbers'''
    assert int(a) == a and int(b) == b, "The numbers must be a integer!"
    if a < 0:
        a = a * (-1)
    if b < 0:
        b = b * (-1)
    # Base case
    if b == 0:
        return a
    # Recursive case
    else:
        return gcd(b, a%b)


def decimalToBinary(n):
    '''Converts a number from decimal to binary number'''
    assert int(n) == n, "The number must be a positive integer!"
    # Base case
    if n == 0:
        return 0
    # Recursive case
    else:
        quotient = n//2
        remainder = n%2
        return remainder+10*decimalToBinary(quotient)


def productOfArray(array):
    '''Returns the product of the all elements in array'''
    assert type(array) == list, "The parameter must be of type array!"
    # Base case
    if len(array) == 1:
        return array[0]
    # Recursive case
    else:
        return array[0] * productOfArray(array[1:])


def recursiveRange(n):
    '''Returns the sum of numbers from 0 to n'''
    assert n>=0, "The parameter must be a positive integer!"
    # Base case
    if n == 0:
        return 0
    # Recursive case
    else:
        return n+recursiveRange(n-1)


def reverse(string):
    '''Returns the reversed string'''
    assert type(string) == str, "The parameter must be of type str!"
    # Base case
    if len(string) == 1:
        return string
    # Recursive case
    else:
        return reverse(string[1:])+string[0]


def isPalindrome(string):
    '''Returns true if the given string is a palindrome'''
    assert type(string) == str, "The parameter must be of type str!"        
    # Base case
    if len(string) == 1:
        return True
    # Recursive case
    elif string[0] != string[-1]:
        return False
    else:
        return isPalindrome(string[1:-1])


def isOdd(num):
    if num%2==0:
        return False
    else:
        return True


def someRecursive(array, callback):
    '''Returns true if a single value in the array returns true 
    when passed to the callback. Otherwise it returns false.'''
    assert type(array) == list, "First parameter must be of type list!"
    # Base case
    if len(array) == 0:
        return False
    elif callback(array[0]) == True:
        return True
    # Recursive case
    else:
        return someRecursive(array[1:],callback)


def flatten(array):
    '''Accepts an array of arrays and returns a new array 
    with all values flattened.'''
    assert type(array) == list, "array must be of type list!"
    resultArray = []
    for subarray in array:
        # Base case
        if type(subarray) != list:
            resultArray.append(subarray)
        # Recursive case
        else:
            resultArray.extend(flatten(subarray))
    return resultArray


def capitalizeFirst(array):
    '''Given an array of strings, capitalize the first letter 
    of each string in the array'''
    assert type(array) == list, "array must be of list type!"
    resultArray = []
    # Base case
    if len(array) == 0:
        return array
    # Recursive case
    else:
        resultArray.append(array[0].capitalize())
        return resultArray+capitalizeFirst(array[1:])


def nestedEvenSum(obj):
    '''Return the sum of all even numbers in an object which 
    may contain nested objects.'''
    assert type(obj) == dict, "obj must be of dict type!"
    sum=0
    for key, value in obj.items():
        # Base case
        if (type(value) == int) and (value%2 == 0):
            sum = sum + value
        # Recursive case
        elif (type(value) == dict):
            sum = sum + nestedEvenSum(obj[key])
    return sum


def capitalizeWords(array):
    ''' return a new array containing each word capitalized.'''
    assert type(array) == list, "array must be of type list!"
    resultArray = []
    # Base case
    if len(array) == 0:
        return array
    # Recursive case
    else:
        resultArray.append(array[0].upper())
        return resultArray+capitalizeWords(array[1:])


def stringifyNumbers(obj):
    '''Takes in an object and finds all the values which are 
    numbers and converts them to strings'''
    assert type(obj) == dict, "obj must be of type dict!"
    resultDict = {}
    for key, value in obj.items():
        # Base case
        if type(value) != dict:
            if type(value) == int:
                value = str(value)
            resultDict[key] = value
        # Recusrive case
        elif type(value) == dict:
            resultDict[key] = stringifyNumbers(value)
    return resultDict


def collectStrings(obj):
    '''Takes an object and returns an array of all the values 
    in the object that have a typeof string.'''
    assert type(obj) == dict, "obj must be of type dict!"
    resultArray = []
    for key, value in obj.items():
        # Base case
        if type(value) == str:
            resultArray.append(value)
        # Recursive case
        elif type(value) == dict:
            resultArray.extend(collectStrings(value))
    return resultArray


if __name__ == "__main__":
    n = 4
    print(f"- Factorial of {n} is {factorial(n)}")
    n = 10
    print(f"- {n}th fibonacci number is {fibonacci(n)}")
    n = 413
    print(f"- Sum of digits of {n} number is {sumOfDigits(n)}")
    x, n = 2, 3
    print(f"- {x} power {n} is {power(x, n)}")
    a, b = 18, 48
    print(f"- GCD of {a} and {b} is {gcd(a, b)}")
    n = 11
    print(f"- Binary conversion of {n} is {decimalToBinary(n)}")
    array = [1, 2, 3, 4, 5]
    print(f"- Product of array {array} is {productOfArray(array)}")
    n = 10
    print(f"- Sum of first {n} numbers is {recursiveRange(n)}")
    string = "Rishabh Jain"
    print(f"- Reversed string of '{string}' is '{reverse(string)}'")
    print(f"- Is '{string}' a palindrome? {isPalindrome(string)}")
    string = "redivider"
    print(f"- Is '{string}' a palindrome? {isPalindrome(string)}")
    array = [4,6,8,9]
    print(f"- Does {array} contains an odd number? - {someRecursive(array, isOdd)}")
    array = [4,6,8]
    print(f"- Does {array} contains an odd number? - {someRecursive(array, isOdd)}")
    array = [1, 2, 3, [4, 5]]
    print(f"- Flattened array of {array} is {flatten(array)}")
    array = [[1], [2], [3]]
    print(f"- Flattened array of {array} is {flatten(array)}")
    array = [[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]
    print(f"- Flattened array of {array} is {flatten(array)}")
    array = ['car', 'taco', 'banana']
    print(f"- Capitalized array of {array} is {capitalizeFirst(array)}")
    obj1 = {
        "outer": 2,
        "obj": {
            "inner": 2,
            "otherObj": {
                "superInner": 2,
                "notANumber": True,
                "alsoNotANumber": "yup"
            }
        }
    }
    print(f"- Sum of even numbers in {obj1} is {nestedEvenSum(obj1)}")
    obj2 = {
        "a": 2,
        "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
        "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
        "d": 1,
        "e": {"e": {"e": 2}, "ee": 'car'}
    }
    print(f"- Sum of even numbers in {obj2} is {nestedEvenSum(obj2)}")
    array = ['i', 'am', 'learning', 'recursion']
    print(f"- Captialize words in this {array} are {capitalizeWords(array)}")
    obj = {
        "num": 1,
        "test": [],
        "data": {
            "val": 4,
            "info": {
                "isRight": True,
                "random": 66
            }
        }
    }
    print(f"- Stringified numbers in this {obj} are {stringifyNumbers(obj)}")
    obj = {
        "stuff": 'foo',
        "data": {
            "val": {
                "thing": {
                    "info": 'bar',
                    "moreInfo": {
                        "evenMoreInfo": {
                            "weMadeIt": 'baz'
                        }
                    }
                }
            }
        }
    }
    print(f"- String values in this {obj} are {collectStrings(obj)}")
