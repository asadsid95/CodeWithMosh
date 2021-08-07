    '''
    def show_name():
        print("hello")

    def increment(number, by=1): # 'by' is a default arg
        return number + by

    print(increment(4))
    print(increment(2,1))
    
    def multiply(*args):    # *arg returns a tuple '()'
    return args

    print(multiply(1,5,3,4))

    def save_user(**user):  # **arg returns a dictionary '{}'
        print(user)

    save_user(id = 1, age = 2, height = 3)

'''

def fizz_buzz(input):
# if divisible by 3, return fizz
# if divisible by 5, return buzz
# if divisible by both, return fizz buzz
# if not divisble by either, return the number itself


print(fizz_buzz(3))