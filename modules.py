'''
    Creating Modules - so far, all code has stayed in a single file but real life programs are divided in various files called modules

        How to decide what part of program goes in which module? think of how superstores use Aisle
        
        Lets shift the functions below into another file, modules1.py

        def calc_tax():
            pass

        def calc_shipping():
            pass
'''

from modules1 import calc_shipping, calc_tax

#calc_tax()
#calc_shipping()

# Another way to import the above is by importing the entire module; This may be undesired if the module contains many functions

from module_samples.modules2 import calc_shipping1, calc_tax1

#calc_tax1()
#calc_shipping1()

'''
    Module Search Path - using 'import' will prompt Python to look in certain directories

    How to see these directories? using the module 'sys'
'''
import sys
#print(sys.path)

# How to import module from sub directory??

'''
    Packages - Packages refer to subdirectories; We created subdirectory 'ecommerce' and created __init__.py so Python treated the subdirectory as a package.

    A pacakge is a container of one or more modules. In filesystem terms, a package is mapped as a subdirectory and a module is mapped as a file

'''

from ecommerce.sales import calc_tax4

#calc_tax4()

'''
    Sub-packages - as the program grows, packages will need to be broken into sub-packages

    So let's create another package inside 'ecommerce' package AND don't forget to create an __init__.py file in it
'''

'''
    Intra-package References - Refer to 'sales' file in sub-package 'shopping' for this lesson

    'Absolute' vs 'relative' imports are also discussed. Former involves explicitly stating name of the package and modules, whereas latter involves using '.' ; Single '.' references the current package & '..' refers to one level up

'''

'''
    dir function - built-in function used to get function and methods defined in an object

'''

from ecommerce.shopping import sales

# After importing sales modules (remember that once imported, sales will be an object), we can use the 'dot' method to access all of its attributes and methods
#sales.calc_shipping()
#sales.calc_tax()

# However as projects and programs grow, things may not work as expected so 'dir' function can be used for debug
print(dir(sales)) # This returns a list containing ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax', 'contact']
# These are all the attributes and methods defined in the object (also note the reason 'contact' is present at end of list is because its imported and therefore it is an object. But aren't only methods and attributes returned by dir function)

#print(sales.__name__) # This returns the name of the module
#print(sales.__package__) # This returns the name of the package
#print(sales.__file__) # This returns the address/path of its file


'''
    Executing modules as scripts - See /shopping/sales module

    Importing the /shopping/sales module in another module, it would have all of its functions and statements loaded only once and then cache it in memory

    Now, if we print 'dir(sales.__name__") in this file, we know that it gives the name of module 'ecommerce.shopping.sales'

    But how about if we print __name__ in 'sales' modules itself? It returns  __main__
'''