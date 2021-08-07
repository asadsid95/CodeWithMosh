def practise():
    """my_name = "Asad Siddiqui"

    print(my_name)
    print(len(my_name))
    print(my_name[0])
    print(my_name[-2])
    print(my_name[0:3])
    print(my_name[:])
    """

    """my_name = "Asad \" \nSiddiqui"
    print(my_name)
    """

    """
    first = "Asad"
    last = "Siddiqui"

    full_name = f"{first} {last}"
    print(full_name)
    """
    """
    who = "I"
    action = "learning"
    what = "Python"
    activity = f"{who}'m {action} {what}."
    print(activity.upper())
    print(activity.title())
    print(activity.find("n"))
    print("ython" in activity)

    print(10**2) #power of
    """
    ''' Comparision/Conditional operators
    temperature = 18 
    if temperature > 30:
        print("hello")
    elif temperature > 20:
        print("it's nice")
    else:
        print("its cold")
    print("done")
    '''
    ''' multi-line conditional
        vs ternary operators (single line)
    age = 19
    if age >= 18:
        message = "eligible"
    else:
        message = "not eligible"    
    print(message)

    message = "elig" if age >= 18 else "not elig"
    print(message)

    age = "8" if age <= 20 else "9"
    print(age)
   
    high_income = True
    good_credit = False
    student = True
    if (high_income or good_credit) and student: # can also use OR & NOT
        print("eligible")
    else:
        print("not elig")

    # chaining comparison operators
    age = 22
    if 18 <= age <= 22:
        print("eligible")
    else:
        print('not elig')

    for i in range(0,3): # for loop
        print("hello", i)
        
    for x in range(5): # Nested loop
        for y in range(3):
            print(f"({x},{y})")

    print(type(5))
    print(type(range(5))) # range is a iterable object

    #### Exercise 
    
    number = 10 # While Loop
    while number < 20:
        print(number)
        number += 2
    command = ""
    while command.lower() != "quit":
        command = input(">")
        print ("ECHO", command)

    count = 0 
    for i in range(1,9):
        if (i%2 != 0):
            i += 1
            print(i)
        elif (i%2 == 0):
            print('')
            count += 1
    print(f"We have {count} even numbers")

    count1 = 0
    for i in range(1,10):
        if i % 2 == 0:
            count1 += 1
            print(i) 
    print(f"we have {count1} even numbers")
    '''