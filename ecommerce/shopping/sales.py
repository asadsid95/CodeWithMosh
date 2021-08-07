#from ecommerce.customer import contact # Absolute imports are preferred unless a module is buried under too many packages 

#from ..customer import contact
#contact.contact_customer()

# Code above gives error

def calc_shipping():
    pass

def calc_tax():
    pass

## Code below is for exercise 'Executing modules as scripts'

print('Sale initialized')
# Now import this module in 'modules.py' file and execute. This will result in the functions and print statements being loaded 

print(__name__) #This returns '__main__'

if __name__=="__main__":
    print("sales started")
    calc_tax() # print statement and this function would execute if this module is DIRECTLY run, like a script. But if this module runs in another module, this 'if' statement would not work as the __name__ will have changed accordingly