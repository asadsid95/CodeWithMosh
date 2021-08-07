#alphabet = ["a", "b", "c", "e", "f"]

# matrix = [[0,1],[2,3]]

# zeros = [0] * 10
#combined = alphabet + matrix + zeros

# numbers=list(range(20))
# chars = list("hello world")
# print(numbers)
# print(chars)
# print(len(chars))

# Accessing items in list
#####
# print(alphabet[0])
# print(alphabet[-1])

#alphabet[0] = "A"
# print(alphabet[0])
# print(alphabet[1:])
# print(alphabet[:])
# print(numbers[::3]) # [start:stop:step]
# print(numbers[:8:2]) # [start:stop:step]

# List unpacking
#####

number1 = [1,2,3,3,3,3,6,7,8]
first, second, *last = number1
# print(last)

# for i in number1:
#     print(i)

# for i in enumerate(number1):
#     print(i)

# for index, digit in enumerate(number1):
#     print(index, digit)


alphabet = ["a", "f", "c", "e", "b"]
# alphabet.append('a') # add to back of list
# alphabet.insert(0,0) # inserts at the index 
# alphabet.pop() # removes element in the back of list
# del alphabet[0:3]

# print(alphabet.index("c"))
if "d" in alphabet:
    print(alphabet.index("c"))

# print(sorted(alphabet))

# --------

products = [        # This is a list of complex objects
    ("p1", 10),
    ("p2", 111),
    ("p3", 25),
    ("p4", 316)
]

# def p_sorted(item):
#     return item[1]

"""
 Now we need to pass the function 'p_sorted' when sorting the list

products.sort(key=p_sorted) # Note this is NOT calling the function 'p_sorted'. Calling it would've looked like p_sorted(). Instead we're passing a reference to the  function  
# print(products)

# Next we'll look at how to make the process better (without creating a function like p_sorted)
"""
# --------

# Lambda Function - Take any # of arguments but can have only one expression
    # Lambda function helps create a function that would be use as an argument to another function

# Instead of 'products.sort(key=p_sorted)' on line 69,

products.sort(key=lambda item : item[1])
# print(products)

# -----
# More use of Lambda functions follow:
 
# Map function - 

# Transforming the products list into a new list of numbers that is - a list of prices

'''
prices = []
for product in products:
    prices.append([product[1]])
print(prices)
'''
# Above is the basic way

# Below is a more concise way by using .map function. 
    # map() takes a function (lambda function) and applies it to the iterable (i.e products)

x = list(map(lambda product : product[1], products)) # W/O list() around map(), it results in map object which is an iterable - This would require the use of for-in loop which is a basic way to code. To iterate over the map object, use list()
# print(x)

''' Filter Function - Results in an iterable containing items that pass a user-defined filter. Remember to use list() '''

y = list(filter(lambda product : product[1] >= 100, products))
# print(y)

# -------
# --------
'''
While map() & filter() is from functional programming, in Python we have Comprehension

[expression for item in items]

We are iterating over an iterable and applying an expression each time

This one is a [] comprehension
'''

prices_mapped = [product[1] for product in products]
# print(prices_mapped)

prices_filtered = [product[1] >= 110 for product in products] # This results in a list of booleans for each value in the tuple from the list, indicating if each value meets the expression or not
# print(prices_filtered)

prices_filtered1 = [product for product in products if product[1] > 100]
# print(prices_filtered1)

# Zip function - How to create [(1,10),(2,20),(3,30)]?

list1 = [1,2,3]
list2 = [10, 20, 30]

# map() and filter() work one list at a time so we need to use zip()

# print(zip(list1,list2))
# print(list(zip(list1,list2)))
# print(list(zip('abc', list1, list2)))

# -----
# ----
'''
Stacks

LIFO - Last In First Out
Think of the browser history and sessions when you click back button, it takes you to the last visited page
'''
browsing_session = [1,2,3]
browsing_session.append(4) # Adds element to the back of the list
# print(browsing_session)
last = browsing_session.pop() # Removes the last element (one in the back) of the list
# print(last)
# print("redirect", browsing_session[-1]) # This shows the last element of the list

# -----

'''
Queue - FIFO (first in first out)

[1,2,3] - we would first remove 1 then 2 then 3. This also means that once 1 is removed, 2 & 3 need to be shifted one space 'up'

'''

from collections import deque # think of a module as a bucket with a bunch of reusable code -- More about module later

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# print(queue)
queue.popleft()
# print(queue)


# ----
'''
Tuple - read-only 'list'
    Read only & immutable
'''

point = (1,2,3,4)
point1 = 1,2
# print(type(point1))
point2 = 1,
# print(type(point2))
point3 = (1,2) +((3,4))
# print(point3)
point4 = (1,2) * 3
# print(point4)
point5 = tuple([2,3])
# print(point5)

# print(point[0:4])
x,y,z,a = point

#if 2 in point:
#    print("it's here!")

# -----
'''
Swapping variables
'''

x = 10
y = 11

# hint: We need a third variable

# z = x
# x = y
# y = z
# print ("x", x, "y", y, 'z (holder variable)', z)

# Now, we'll swap without a third variable

x,y = y, x

# print ("x", x, "y", y)

# -------

'''
Array = needs for a lot of values (< 1000)for performance
'''

from array import array

numbers = array("i", [1,2,3,4]) # "i" is the typecode to specify data type
numbers[2]
# print(numbers[2])

# ------
'''
Set {#, #, #...} - Collection of numbers with NO DUPLICATE & unordered (therefore not accessible using [] notation)
 
'''
nhumber = [1,2,3,4,4,5]
uniques = set(nhumber)
# print(uniques)
second = {1,4}

uniques| second # Union of 2 sets
# print(uniques & second)
# print(uniques - second)
# print(uniques ^ second)

# # print(uniques[2]) # gives error
# instead do this
# if 2 in uniques:
#    print("set includes 2 but it cant be accessed using [] notation")

# -----
'''
Dictionary {key: value, key1:value1,...}
        value can be of any type (set, tuple, list, dict)
'''
# point = {"x": 1, "y": 2}

point = dict(x=1,z=3) # another way of making dict
point["z"]
# print(point.get("f", 0)) # This 'gets' value of key or else returns a default value 0
del point["x"]
# print(point)

# for key in point:
#     print(key, point[key]) # This unpacks the dict

# for key in point.items(): # This returns a tuple of the key-value
#     print(key)

# for key, value in point.items(): # This unpacks the dict as well
#     print(key, value)

# ----
# Dict comprehension

''' 
Just like list comprehension [expression for item in items]
'''
values= {x*2 for x in range(3)}
print(values)
values1 = {x: x*2 for x in range(4)} # this is dict comprehension
print(values1)

values3 = (x * 2 for x in range(5)) # This gives a generator object
print(values3)

print(*nhumber)
print(*nhumber,*number1)

first = dict(x=2,y=6,z=7)
second = dict(a=5,b=5,c=5)
print({**first, **second})