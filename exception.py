'''
squared = []

for digit in range(10):
    squared.append(digit**2)

print(squared)
print(digit)

squared1 = map(lambda digit: digit**2, range(10))
print(list(squared1))

stringg = "Helelo"
print(stringg + "world")
'''

# -----

'''
Exceptions - When program encounter something wrong due to missing file/bad input data, program will crash
'''
## Example 1 of error:

# Exception - error that terminates the execution of the program
number = [1,2]
#print(number[3])

## Example 2 of error:
# age = int(input("Age: "))
## If non-integer value in input, program crashes

# My job as a programmer is to prevent the program from crashing/terminating. Lets see how we can do that

# ------
'''
Handling Exceptions
'''
# age = int(input("Age: "))
## Since this will crash the program if non-int value is provided to the program, we need a new way to handle the error using 'try-except' block

# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("a non-int value was provide, try again")

# Since exception handling is done properly such that except block executes if non-int is provided, following code will continue to execute

# print("The rest of the code will continue")
## Remember that if try-except block was missing, the whole program would terminate

#----
'''
# Extention of above code block, to include error message and type, as well as 'else' in try-except block

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Incorrect input. But worry not, following code will continue to execute")
    print(ex) # Shows the actual error
    print(type(ex)) # Show error's type
else: # This blocks executes if the try block executes
    print("Great job! Integer value was given as asked!")

print("...FOLLOWING CODE...")

'''

#-----

'''
Handling different exceptions: 

# Unlike above block where only ValueError was being dealt with, what happens if its another type of error (not listed in the except block)? 
Program will still crash!
'''

'''try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("First exception block: Incorrect input. But worry not, following code will continue to execute")
except ZeroDivisionError:
    # This except block won't execute as the error type for dividing by zero already matched the first except block
    print("First exception block: Incorrect input. But worry not, following code will continue to execute")
else: # This blocks executes if the try block executes
    print("Great job! Integer value was given as asked!")
'''
# -----
'''
Cleaning up - Working with external resources like files, DB, need to be realized before closing the program

Use .close() in 'finally' part of the block

'''
'''try: 
    file = open("app.py")
    age = int(input("Age: "))
except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age.")
else: 
    print("No exceptions were thrown.")
finally:
    file.close()
'''

'''
With Statement - more concise & 'finally' block is no longer needed. With statement automatically closes the resource
'''

'''try: 
    with open("app.py") as file, open("ifthisfileexisted.txt") as target:
        print("File opened. It could also be read or written into")
    
    age = int(input("Age: "))
except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age.")
else: 
    print("No exceptions were thrown.")
'''


#-----
'''
Raising Exceptions - So far we know how to handle exceptions, now we learn how to raise/throw exceptions in my own code

Search Python's built in exceptions
'''

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age
# w/o try-except block, the program crashed. Therefore, try-except is needed

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

#-----
'''
Cost of raising exceptions - Try using return 0 instead of exception to cut on cost of processing time
'''