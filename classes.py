# Class: Blueprint for creating new objects
# Objects: Instance of a class

# Class: Human
# Objects: John, Asad, Bob

#---------
'''
 Creating classes
    - naming convention: every word needs to be capitalized & _ are not to be used for multiple words
    Variables & functions convention is to use lowercase and _ between each word
'''
from types import new_class


class MyPoint: 
    # Now define all the functions needed, which will appear on every object 'MyPoint' 
    def draw(self): # All functions in a class must have atleast one parameter; the bare minimum parameter is 'self'
        print("draw")

#point = MyPoint()
# print(type(point)) # Produces <class '__main__.MyPoint'> ; the main is a module, to be learned in a bit

# print(isinstance(point, MyPoint)) # Return whether an object is an instance of a class or of a subclass thereof.

# print(isinstance(point, int)) # This will be false as point is not an instance of the class 'int'

# point.draw() # Apart from this function, more functions show up with typing 'point. ' ; This is part of the concept called Inheritance (to be taught in a bit)

#---------

'''
Constructors - our classes need initial values like x & y. To set these values, we need a constructor
'''

class Point:
    def __init__(self, x, y): 
        ''' __init__ is a special method called, magic method (Python has a few more; to be learned)
        # this method is called a constructor and is executed everytime a new point object is created

        Remember that every method/function inside a class must have atleast one parameter, and thus adding 'self'
        After adding 'self', we also added x & y as additional parameters for initializing the object

        'self' points/references to the current object (remember that objects are instances of classes)
            i.e. on line 'point = Point(1,2)', when Point class is called, Python will internally create the 'point' object and set 'self' to reference that 'point' object.
            This 'point' object will have methods (default from Python), as well as attributes which are variables that include data about the object, such as x and y
            I.O.W, a class or object bundles data and functions related to that data into one unit
        And because it will reference a specific object, we can use it to set the other attributes
'''
    # we know that 'self' is a reference to current object. So we'll use that to set 'x' and 'y' attributes
        # Technically we can rename those attributes to anything (i.e. 'lol' and 'hi') and give them default values... or we can set them to the 'x' and 'y' arguments that we received in the _init_ method
    # Below we will set 'lol' and 'hi' to values that are passed via 'x' & 'y'. IOW, we are simply giving 'lol' and 'hi' initial values, from x and y

        self.lol = x 
        self.hi = y

    def draw(self):
        # The 'self' parameter gives reference to the current object 'point' and with this, we can read values for 'lol' and 'hi' 

        # print("draw")
        print(f"Point ({self.lol},{self.hi})")
        #return 1234

point = Point(1,2)
# print(point.hi)

# point.draw() # Notice that we didn't supply value for 'self' as Python does that by default
# We can technically do point.draw(point) as a reference to the current object but it's unneccessary 
# print(point.draw()) 
# Difference between the above 2 lines is the the latter also returns the 'return' value

class NewClass:

    def __init__(self, first, second):
        self.this_is_a_variable = first
        self.this_is_another_variable = second
    
    def execute(self):
        executes_first_variable = self.this_is_another_variable
        print(executes_first_variable)

trial = NewClass(1,3)
#print(trial.this_is_a_variable)
#print(trial.this_is_another_variable)

# print(trial.execute())

'''
    Class vs Instance attributes

    Previously we defined 2 attributes for an object called 'point' in the constructor of the 'point' class
    So any time, a new object is created from 'Point' class, the object will have these attributes by default

'''
# It's also possible to create new attributes after creating an object as python. This allows us to not needing to define all attributes at the time of class creation

# Lets create a class

class MyPoint1:
    
    def __init__(self,x,y):
        self.first = x
        self.second = y
    
    def draw(self):
        print (f"value of 'first' attribute: {self.first}. \nvalue of 'second'attribute: {self.second}.")
        return 'end of draw()'

myPointInitialized = MyPoint1(20, 30)
#print(myPointInitialized.first)
#myPointInitialized.draw()

# example of creating an attribute after having created the class
myPointInitialized.z = 40
#print(myPointInitialized.z)

# Important thing to remember: all these attributes (x y z) are INSTANCE ATTRIBUTES. I.O.W they belong to objects (recall that objects are instances of class) and their values will belong only to that object
# This means each object can have different values for these attributes. See code below
anotherObjectinitialized = MyPoint1(100, 200)
#anotherObjectinitialized.draw()
# Also note that there's no third attribute present in this initally, as this was applicable only to that instance/object 

# Now, we can define attributes at the class level which will be shared with every instance (as well as their values)
# Lets see this
class MyPoint2:
    default_colour = "red"

    def __init__(self,x,y):
        self.first = x
        self.second = y
    
    def draw(self):
        print (f"value of 'first' attribute: {self.first}. \nvalue of 'second'attribute: {self.second}.")
        return 'end of draw()'

myPoint2Initialized = MyPoint2(50, 60)
#print(myPoint2Initialized.default_colour)

# We can also use the class itself to access the class attribute
#print(MyPoint2.default_colour)

# Now if we were to change value of the class attribute later into a program like this, what happens?
MyPoint2.default_colour = "blue"
#print(MyPoint2.default_colour)
# The value changes! and this change would be implemented into all instances/objects created after this moment and onwards

'''
    Class vs Instance Methods

    Same concept as the attributes being defined in different levels and thereby their values applying either to ALL instances or being instance-dependent

    In MyPoint2, methods '__init__' & 'draw' are instance methods
    So we can call them using an instance of the class, using an object (example of the object is 'myPoint2Initialized' which uses the class 'Mypoint2'  )
    The instance methods are used when an object reference is needed. 

    i.e. when drawing a point, we need to work with a specifc object (to get the correct values for x & y), this is why the draw method is defined as an instance method

    But in times when existing object is not needed, and this is when class method is needed
'''
class MyPoint3:  

    def __init__(self,x,y):
        self.first = x
        self.second = y

    @classmethod  # This is a decorator which extends the behaviour of a method or a function (its functionality to be explored shortly) 
    def zero(cls): # the first parameter ('cls'; its name is due to convention) references to the class itself. Remember we're not working with point object/instance 
         return cls(0, 0) # This is the same as calling MyPoint3(0,0) ; The difference is that at run time when this zero method is called, Python will automatically pass reference to the class to this zero method

    def draw(self):
        print (f"value of 'first' attribute: {self.first}. \nvalue of 'second'attribute: {self.second}.")
        return 'end of draw()'

# point = Point(0,0,1,'a') # Instead of passing these values to create a object, we define the factory method 
point1 = MyPoint3.zero() # .zero() is considered a factory method. It creates new objects
#print(point1)

'''
    Magic methods - methods with '__' in the beginning and end of their name, and they are automatically called by Python interpreter depending on how we use the objects and class

    Lets use the __str__ to see what happens when an object is converted to a string, on an instance of the class
'''
class MyPoint4:  

    def __init__(self,x,y):
        self.first = x
        self.second = y

    def __str__(self):
        return f"({self.first}, {self.second})"

    def draw(self):
        print (f"value of 'first' attribute: {self.first}. \nvalue of 'second'attribute: {self.second}.")
        return 'end of draw()'

point = MyPoint4(1,2)
#print(point) # without __str__ implementation inside of class, this produces ' <__main__.MyPoint4 object at 0x000002DE757A13D0> '; This is the default implementation of the __str__ magic method
# With implementation of __str__, we get the return value from its method in 

# typing 'point. ' shows more magic methods available to 'point' object which were inherited from another object

'''
    Comparing Objects - 

class MyPoint5:  

    def __init__(self,x,y):
        self.first = x
        self.second = y

point = Point(1, 2)
other = Point(1,2) 
print (point == other) # This returns false because the equality operator by default compares references of address of these 2 objects in memory; Since they individually are in seperate memory address, its considered not equal ( check memory address by 'print(point)' & 'print(other)' )
'''

class MyPoint5:  

    def __init__(self,x,y):
        self.first = x
        self.second = y

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second

    def __gt__(self,other):
        return self.first > other.first and self.second > other.second

point = MyPoint5(1,2)
other = MyPoint5(1,2)
other_other = MyPoint5(0.5, 0.5)

#print(point == other)
#print(point > other_other)

'''
    Performing Arithmetic Operations -- There are magic methods for these operations as well
'''

class MyPoint6:  

    def __init__(self,x,y):
        self.first = x
        self.second = y

    def __add__(self, other):
        return MyPoint6(self.first + other.first, self.second + other.second)

point = MyPoint6(1,4)
second_point = MyPoint6(2,2)
# print(point + second_point) # This produces the object with its memory location. This is because there's no __str__ magic method
# However, if result of arithmetic operation is stored in another object, we can see the added value by referring to the first attribute of the 'combined' object
combined = point + second_point
#print(combined.first) # produces 3

'''
    Making customer containers - We've learned about data structures (list, set, tuples, dict). These Data structures AKA containers are pretty sufficient for most cases

    But we can create our own container

    Example below is a class to keep track of various tags (think categorization) on a blog/articles. i.e. how many articles do we have that have Python as a tag 

    Since this class represent a container, it supports functions related to containers

    Once finished, it will be able to do the following operations:
    
    cloud = TagCloud() - this creates an object
    #len(TagCloud) - this gets # of items 
    #cloud["python"] ; to get an item by its key 
    #cloud["python"] = 10 ;To set an a value for its item by a key
    #for tag in cloud: -  this iterates over a container
    #   print(tag)
'''
class TagCloud:
    # We can use one or more of the built-in data struc. In this case, we'll use dictionary because it quickly allows us to get # of given tags

    # 1. Lets define a constructor
    def __init__(self):
        # 2. Lets initialize 'tags' attribute to an empty dictionary. REMEMBER this attribute will be available to all functions within this class + all objects created from this class
        self.tags = {}

    # 3 (optional). a method that takes a tag
    def add(self, tag):
        
        # 4. We can check if a user-provided tag is in the dict; if we don't have it in the dict, set its value to 1. or else (iow if it is present in the dict) increment by 1 
        self.tags[tag] = self.tags.get(tag, 0) + 1 #.get() is for dict's method to return value of the tag 'key'. If the value isn't present, then create the keys and set to default value provided (0)
        # Moreover, .get() is first looking for the tag; by default, it should return a value of 0 if the provided tag is not there... but we have + 1 at the end. This results in the value of a new tag to automatically be 1; Had we removed + 1, the count would've started with 0

        # 5. now, lets run the operations below; {'python': 3} gets returned

        # 6. Why create a custom class for a dictionary... this does exactly the same thing as a dict; Answer is that I want to make this smarter than the built-in dictionary.
        # Smarter? If we added another item such as cloud.add("Python"), a typical dictionary would result in {'python': 2, 'Python': 1}

    #7. So in this class, we'll make the dictionary smarter by making it case sensitive. Remember that 'self.tags' is an instance attribute as its defined in the constructor & add() / add_case_sensitive() is an instance method. This means that whatever value is passed as argument to the instance method will belong only to that object/instance. 
    def add_case_sensitive(self, tag):
        self.tags[tag.upper()] = self.tags.get(tag.upper(), 0) + 1 # Try removing .upper() from get(), and see what happens; think of why it has to be stated on both sides
        # Notice the complexity of this feature is encapsulated and not visible through out the code

    # 9. Syntax: __getitem__(self, key)
    def __getitem__(self, tag): 
        return self.tags.get(tag.lower(), 0) 

    # 11. Syntax: __setitem__(self, key, value)
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # 13. 
    def __len__(self):
        return len(self.tags)

    # 14. To make our custom dict iterable, we need to walk the container and gets one item at a time. 
    # To this see ability, use "for tag in cloud: print(tag)"
    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
#print("Count of tag 'python':", cloud["python"]) # 8. Typical dictionaries cant return count of a tag, so how should we do this?
cloud['java'] = 10 # 10. In 8., we could only read the count of a tag. How can we set it?  
#print(len(cloud.tags)) # 12. how to get length of dict?; Note this results in 2 as 'python' and 'java' are the only members up until now
cloud.add_case_sensitive("python")
cloud.add_case_sensitive("python")

#for tag in cloud:
    #print(tag)
#print("Tags: ", cloud.tags)

#len(TagCloud)
#cloud["python"] = 10
#for tag in cloud:
 #   print(tag)

'''
    Private members - using the same class as above (but change its name to avoid conflict) while ignoring the numbering system (as it applies to the class above)

    TLDR; These are not true private members like other languages have, as they can still be accessed using __dict__ (if the attribute is a dict). Purpose of this feature is to prevent accidental access into attributes
'''
class TagCloud1:
    # We can use one or more of the built-in data struc. In this case, we'll use dictionary because it quickly allows us to get # of given tags

    # 1. Lets define a constructor
    def __init__(self):
        # 2. Lets initialize 'tags' attribute to an empty dictionary. REMEMBER this attribute will be available to all functions within this class + all objects created from this class
        self.tags = {}

    # 3 (optional). a method that takes a tag
    def add(self, tag):
        
        # 4. We can check if a user-provided tag is in the dict; if we don't have it in the dict, set its value to 1. or else (iow if it is present in the dict) increment by 1 
        self.tags[tag] = self.tags.get(tag, 0) + 1 #.get() is for dict's method to return value of the tag 'key'. If the value isn't present, then create the keys and set to default value provided (0)
        # Moreover, .get() is first looking for the tag; by default, it should return a value of 0 if the provided tag is not there... but we have + 1 at the end. This results in the value of a new tag to automatically be 1; Had we removed + 1, the count would've started with 0

        # 5. now, lets run the operations below; {'python': 3} gets returned

        # 6. Why create a custom class for a dictionary... this does exactly the same thing as a dict; Answer is that I want to make this smarter than the built-in dictionary.
        # Smarter? If we added another item such as cloud.add("Python"), a typical dictionary would result in {'python': 2, 'Python': 1}

    #7. So in this class, we'll make the dictionary smarter by making it case sensitive. Remember that 'self.tags' is an instance attribute as its defined in the constructor & add() / add_case_sensitive() is an instance method. This means that whatever value is passed as argument to the instance method will belong only to that object/instance. 
    def add_case_sensitive(self, tag):
        self.tags[tag.upper()] = self.tags.get(tag.upper(), 0) + 1 # Try removing .upper() from get(), and see what happens; think of why it has to be stated on both sides
        # Notice the complexity of this feature is encapsulated and not visible through out the code

    # 9. Syntax: __getitem__(self, key)
    def __getitem__(self, tag): 
        return self.tags.get(tag, 0) 

    # 11. Syntax: __setitem__(self, key, value)
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # 13. 
    def __len__(self):
        return len(self.tags)

    # 14. To make our custom dict iterable, we need to walk the container and gets one item at a time. 
    # To this see ability, use "for tag in cloud: print(tag)"
    def __iter__(self):
        return iter(self.tags)

cloud1 = TagCloud1()
cloud1.add_case_sensitive("python")
cloud1.add_case_sensitive("python")
cloud1.add_case_sensitive("PythOn")
#print(cloud1['python']) # as expected, its going to be 0 because all added tags were converted to upperclass; 
#print(cloud1.tags) # as expected, its results in {'PYTHON': 3}
#print(cloud1['PYTHON']) # unexpectedly, its results in 0; However once __getitem__ was changed to having only (tag, 0) instead of (tag.lower()) resulted in 3 since all keys are kept as 'PYTHON'


#print(cloud1.tags["python"]) # results in KeyError: 'python' as all keys were stored as UPPERCASE
# However the actual problem is that with class 'cloud1', it gives one access to the underlying dictionary that is used to keep count of the tags. To fix this problem, we need to hide this attribute from the outside.
# how to do this?

# lets create another class similar to TagCloud1
class TagCloud2:

    def __init__(self):
        self.__tags = {} # 2. putting the caret on 'tags', press F2, and then inserting '__' before 'tags' will implement that change to all

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1 

    def __getitem__(self, tag): 
        return self.__tags.get(tag, 0) 

cloud2 = TagCloud2()
cloud2.add("python")
cloud2.add("python")
cloud2.add("Python")
#print(cloud2.__tags)
#print(cloud2.__tags['PYTHON']) # 1. TRY THIS W/O '__tags'; Again, the error is related to key not being found as all keys were stored as lowercase. But the problem is the object giving access into underlying attribute (dict) and thus, we need to hide it. How to do this??

# 3. To test if the dict attribute got hidden away, the 2 print statements above give AttributeError as 'tags' is no longer available
# Point of the private member is to let user know, not to touch the attribute

#4. How does one  access it then?
# print(cloud2.__dict__) # every object has this property '__dict__' which holds all dictionary; {'_TagCloud2__tags': {'python': 3}} gets returned;
# NOTICE the name of the attribute gets the prefix of its class (but it has single underscore while the attribute has double underscore) AND we can technically access this attribute by using... guess.. _TagCloud2__tags'
# print(cloud2._TagCloud2__tags)


# Therefore to check if a class has private members that are dictionary, you can use __dict__ which would result in '_ClassName__attribute'

'''
    Properties - This is to have control over attributes in a class

'''

class Product:
    def __init__(self, price):
        # self.price = price # 2. Simple solution: we can make it private and set 2 methods to getting and setting the value of this attribute
        # self.__price = price # 5. Having 3 & 4 in place, we can easily do 'self.set_price(price)' but thats un-python-ic
        self.set_price(price)

        # 6. This is where we use Properties
       

    def get_price(self):     # 3. This simply returns the price
        return self.__price

    def set_price(self, value):     # 4. This takes the value, checks if its negative (if so, ValueError gets raised)
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # 7. A property is an object that sits in front of an attribute and allows getting and setting a value for an attribute
    # Syntax: property(fget, fset, fdel, doc) - all 4 parameters are optional; First 3 parameters are functions for setting, getting and deleting values, and doc is for documentation (not sure how to use this one)
    price = property(get_price, set_price) # Note the functions in parameter are being passed as REFERENCE, not called. This property function will return property object which will use the functions from the parameter to read the value of the attribute (price)

product = Product(1050) # 1. But... price can not be negative so how do we prevent this?
#print(product.price)

# 8. But now, using 'product. ' exposes the instance methods, thereby polluting the object's metaphor (similar to have 50 buttons on a remote control)
# Lets create another class for neatness

class Product1:
    def __init__(self, price):
        
        # 11. We'll insert the property 'price' like an attribute
        # self.set_price(price)
        self.price = price

    # 9. We can for sure make them private using '__' as prefix but that keeps the noise in the code
    # There's a better and cleaner way using decorator (previously used @classmethod to convert an instance method to class method)
    # Instead of calling the property() function to create a property object as done above, we use @property and rename the function to 'price'
    @property
    def price(self):  
        return self.__price

    # 10. And here, we will need to apply another decorator with the its first segment of name, being name of property and then '.setter'
    # This makes the code cleaner
    # We'll learn later about how this internally works
    @price.setter
    def price(self, value): 
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # price = property(get_price, set_price)

#product = Product(-10)
# print(product.price) # As expected this throws the ValueError due to condition in .setter
# In the event we don't create a setter, we will NOT be able to give the attribute new values
product.price = 2

'''
    Inheritance - Having a multiple classes will allow for sharing one or more methods/functions & attributes in common

    3. Having 2 classes (mammal and fish), both have the 'walk' function in common; If there's a bug in the function or its in need of change for behaviour, you would be doing redundant tasks

    4. There is composition or inheritance (to be discussed in this section) -- Inheritance is the ability to define a method that will be used in another class(es) and inherit it in our classes
'''
#class Mammal: # 1.
    #def eat(self): # Common method
    #    print("eat")

#    def walk(self):
#        print("walk")

#class Fish: # 2.
    #def eat(self): # Common method
    #    print("eat")

#    def swim(self):
#        print("swim")

# 5. Lets make this the parent class
class Animal:
    def __init__(self):
        self.age = 100
        print 

    def eat(self): # Common method
        print("eat")

# Animal is called Parent or Base class
# Mammal is called Child or subclass
class Mammal(Animal): # 1.
    #def eat(self): # Common method
    #    print("eat")

    def walk(self):
        print("walk")

class Fish(Animal): # 2.
    #def eat(self): # Common method
    #    print("eat")

    def swim(self):
        print("swim")

m = Mammal()
#m.eat()
#print(m.age)

'''
    The object class - 
'''

#print(isinstance(m, Mammal)) # True
#print(isinstance(m, Animal)) # also True because although it's an instance of Mammal(), it inherited from Animal()

# Another thing to know is that Animal (a parent class) inherits from another class called 'object' which is the base class such that ALL classes indirectly rise from the 'object' class

# So will it be true if we check that 'm' is an instance of 'object' class?
#print(isinstance(m, object)) #; True
o = object() # this is a builtin function to create an empty object; checking 'o. ' shows all the methods that come from the base class

# Another builtin function is 'isSubclass()'; This checks if a class is derived from another class
#print(issubclass(Mammal,object))

'''
    Method Overriding - Given Mammal1 is a subclass of Animal 1, what if we want to add another attribute to Mammal1() in its constructor such as weight

    TLDR; Method overriding means extending a method defined in the base class. Without it, __init__ method in subclass would replace the __init__ method from parent class
'''
class Animal1:
    def __init__(self):
        self.age = 100
        print 

    def eat(self): 
        print("eat")


class Mammal1(Animal1):
    def __init__(self): # 1. Adding another attribute even though this is a subclass of Animal1 
        # 4. by using super(), We'll be able to initialize parent class's attribute and not have it overridden 
        super().__init__() #After 'super(). ' we can call any method from the parent class
        # Note that by changing the order of which super() appears in, we'll change when constructor of Animal1 gets initialized in compared to Mammal1's constructor
        self.weight = 12
        #super().__init__()

    def walk(self):
        print("walk")

m1 = Mammal1()
#print(m1.weight) # 2. While this worked
#print(m1.age) # This gave an error 'AttributeError: 'Mammal1' object has no attribute 'age' ' But why did this happen? especially since Mammal1 is a subclass so shouldn't it have gotten the attribute from its parent class?

# 3. The reason Mammal1 didnt get the 'age' attribute is because the constructor from it replaced the constructor from its parent class
# This is method overriding 
# So what if we want attributes of the parent class as well as the child?

#print(m1.age)

'''
    Multi-level Inheritance - Limit Inheritance to one or two levels only;

    Imagine we have 3 classes: Animal - Bird - Chicken
    Following methods are defined for each: Animal (eat) - Bird (fly) 

    So Chicken would get the method fly but chickens don't fly; So calling 

    Also note the use of 'pass' in class Chicken is because it's an empty class and Python requires pass for empty classes instead of having nothing inside its body
'''

class Animal2:
    def eat(self):
        print("eat")
        
class Bird(Animal2):
    def fly(self):
        print("fly")

class Chicken(Bird): 
    pass

'''
    Multiple Inheritance - we can have multiple base classes (BEWARE of issues if used incorrectly)
'''

class Employee:
    def greet(self):
        print("Employee Greetings")

class Person:
    def grett(self):
        print("Person GREET")

class Manager(Employee, Person):
    pass

manager = Manager()
#manager.greet() # This results in 'Employee Greetings' only; so did it terminate after finding the 'greet' method in Employee class? Yes
# First, Python looked for 'greet' method in Manager but didn't find it. Then it sequentially went to check its first parent class, Employee class and found it there. Now, even though Person class had the method as well, it didn't get called because the program terminated after finding it in Employee class

# Now if the ordering of the parent classes is changed, then the behaviour will also change. Multiple inheritance is only bad when used incorrect. It can be very helpful when used properly.

# If the base classes are small and have unique methods, it's a great idea to use multiple inheritance. If they have similar methods (behaviour wise), be very careful

# Another example of good use of multiple inheritance:
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer): 
    pass 
# since the base classes have unique methods, this is a good use

# When I come back for review, think of use cases using the analogy provided above

'''
    Example of Inheritance

    Lets model a stream of data. This can happen through network, file, memory.
    Common tasks among these types of stream reading is opening, reading from, closing the stream
    BUT how we read them is dependent on the type of stream such that reading from a file is different from reading from a network

'''
# 3. This is to create the custom exception. Convention for custom exception is to contain '...Error' at the end of their name
# For custom exception, they'll be built on top of base class 'Exception'
class InvalidOperationError(Exception):
    pass

# Lets start with a base/parent class
class Stream:
    
    # 1. We'll set a flag to know if the stream is open, to false
    def __init___(self):
        self.opened = False

    def open(self):
        # 2. In case the stream is already open, we need to raise an exception. It wont be a ValueError because we're dealing with a value, so we'll create a custom expection called InvalidOperationError
        if self.opened:
            # 4. Implementing the custom exception
            raise InvalidOperationError("Stream is already open")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = False

# 5. Another class that inherits from Stream; Purpose of creating this and 'NetworkStream' is because reading from these 2 sources will be different
class FileStream(Stream):
    
    # This method would have the unique process of reading from a file
    def read(self):
        print("Reading data from a file")
    
class NetworkStream(Stream):
    
    # This method would have the unique process of reading from a file
    def read(self):
        print("Reading data from a network")

# This is an example of inheritance such that it avoids multi level inheritance although it may be possible to create at max, one more level

'''
    Abstract Base Classes - Using set of classes from above, there are a few issues in the implementation such that we can instantiate the parent class 'Stream1' and call the open method. This is a problem. See 1.

'''

# 4. 'abc' is a module; 'ABC' is a class (hint - it starts with a capital) and 'abstractmethod' is a method (hint - it starts with lowerclass) which will be used as a decorator
from abc import ABC, abstractmethod

# 5. To make this class abstract, we'll pass 'ABC' as base class (IOW, derive it from ABC class)
class Stream1(ABC):
    
    def __init___(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = False

    # 6. Next, we need to provide common interface/method for all stream classes such as .read() method + we need to decorate it w/ 'abstractmethod'. Also, notice that this class is empty... because this provides the interface for subclass to customize as they like
    # This will solve all the issues mentioned before. Lets try to run it... 
    @abstractmethod
    def read(self): 
        pass


# 2. The second issue is that for the other classes 'FileStream1' and 'NetworkStream1', they both have .read() method. If tomorrow that we create another subclass but instead of naming its method '.read()', we name it '.readxyz()', then its not consistent. 

class FileStream1(Stream):
    
    def read(self):
        print("Reading data from a file")
    
class NetworkStream1(Stream):
    
    def read(self):
        print("Reading data from a network")

# 1. We instantiate the parent class and call its method but this is an issue because the class Stream1 is an abstract class. Also what does it mean to 'open' the stream? There is lack of clarity on 'what' are we opening; is it file, network stream? It doesn't specify and thus its abstract (this is not a exhaustive explanation on its being of abstract)
# Therefore we shoudn't be able to directly create an instance of this type of class. Instead, we should use it to create other subclass and then create an instance of that subclass. This is the first problem. Remember that it was created solely for the reason of using its method in other class. 

# 3. IOW, there is no way to enforce a common interface across different stream class. We're currently just using convention. But it would be nice to have a common interface across the different stream classes
# This is where we use Abstract Base Class (ABC); think of half-baked cookie such that it's not ready to be eaten. ABC's purpose is to provide common code to its derivatives (read that again)
# Therefore we want to make Stream1()  class an ABC
#stream = Stream1()

# 7. But we have a red underline under Stream1() and it says 'Abstract class 'Stream1' with abstract methods instantiated'
# This happens when a class has an abstract method, it considered an Abstract class (read that again) and therefore, we can't instantiate them. So running it will give error "TypeError: Can't instantiate abstract class Stream1 with abstract method read". Read 8. and onwards
#stream = Stream1()
#stream.open() 

# 8. Second problem is that if we create another class later and make Stream1 as its parent class. We'll again get a red
class MemoryStream1(Stream1):

    # 10. To avoid making MemoryStream1 an abstract class (due to '.read' method from 'Stream1' class being an abstract method), we'll define '.read()' method here
    def read(self):
        print("Reading from memory stream")
    

# 9. We'll again get a red underline with 'Abstract class 'MemoryStream1' with abstract methods instantiated'. Why? Because Stream1 has an abstract method '.read()', we must implement that method in the subclass otherwise 'MemoryStream1' will also be considered abstract
stream1 = MemoryStream1()
#stream1.read() # It worked!

'''
    Polymorphism - In the following code, draw() function will be utilizing polymorphism ('many forms') as it will take many forms and this determined at run-time. Notice how the use of list (containing various subclasses) in it allows rendering of each subclass's respective outputs... all from one single function. 

    Real life example would be to create an application's components as subclasses, and rendering this through a single function (like draw() ) using a list
'''

class UIControl(ABC):

    # Again, notice this is an empty method. The reason being, is so that it can be re implemented in subclassess and customized as per their need
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(control): # Yes, this may look confusing at first BUT what is happening is that any thing passed into draw() will be an argument to the parameter 'control'. Simple? Yes. 
# Now, I can see that the argument is calling a '.draw()' method which implies that it(argument) must already have a method 'draw()' within itself. This is the same as the class (which is the argument) being instantiated as an object and then calling its method 'draw()'
    control.draw()

# Extending the mention of 'using a list of subclasses' to leverage polymorphism, look at the function below:

def draw1(controls):
    for control in controls:
        control.draw()

tb = TextBox()
ddl = DropDownList()

#print(draw1([tb,ddl])) # it worked!

'''
    Duck Typing - 'if it walks like a duck and quacks like a duck, it is a duck'

    TLDR - referring to code above, its not neccessary to have the parent class 'UIControl' in order to use the .draw() method. As long as the objects doing into the draw() function (function is not the same as method as latter is w/in a class while former stands alone) has the method 'draw()' within them. 
    This capability is due to Python being a dynamic language. This means it doesnt check the object except only for certain methods that are stated. IOW Python is only checking for the 'draw()' method inside of the objects 'TextBox1' & 'DropDownList1'

        HOWEVER, its good to use ABC! This is because it enforces a common interface for the specified methods
'''
# Notice that theres no parent method which is an ABC

class TextBox1():
    def draw(self):
        print("TextBox")

class DropDownList1():
    def draw(self):
        print("DropDownList")

def draw2(controls):
    for control in controls:
        control.draw()

tb1 = TextBox()
ddl1 = DropDownList()

#print(draw2([tb1,ddl1])) # It worked!


'''
    Extending Built in types - We can also use inheritance with built-in types. I.e. creating making a class have 'str' class as base class. This would allow inheriting all features of 'str' class + we can additionally add more features (i.e. duplicating, summarizing)

    We've modify the original 'append' method by using the following approach: First, create a method inside of recently-created class (iow, child class) with the same name as base class's method, implement the modification + use super() to call and use the method of the original 'list' class
'''

class Text(str):
    def duplicate(self):
        return self + self

text = Text("Python")
#print(text.lower())
#print(text.duplicate())

# Lets extend 'list' 
class TrackableList(list):

    # Here we will overwrite the 'append' method by adding the ability to print something everything is adding
    def append(self, object):
        print("Append called")
        # Now we can call the append method of the super AKA base class 'list'. Notice that this is within the 'append' method that we are defining BUT the '.append()' used here is actually from the base class 'list', not the method we just defined. IOW, we're NOT calling the method that we're creating within. 
        super().append(object)
    # Therefore, we've modified the original append method by using the following approach: First, create a method with the same name as base class's method, implement the modification + use super() to call and use the method of the original 'list' class

list = TrackableList()
#list.append(1) # It worked!

# Therefore we've extendind a built-in types 

'''
    Data Classes - So far, we've used classes to bundle data (iow, attributes) with functionality into one unit. I may also come across classes that have no methods/functionality/behaviour, they only have data

    TLDR; This is useful for classes that only have data and no method

    However, remember these are tuples... immutables 
'''

class Point5:
    def __init__(self,x,y):
        self.lol = x
        self.hi = y

    def __eq__(self,other): # 2. This will allow comparison to be equal
        return self.lol == other.lol and self.hi == other.hi

    # 3. while the above is tedious, especially if classes have more data;
    # let's use namedtuples

p1 = Point5(1,2)
p2 = Point5(1,2)

from collections import namedtuple

Point1 = namedtuple('Point1',['x','y'])
p1 = Point1(x=1,y=2)
p2 = Point1(x=1,y=2)
#print(p1 == p2)

# print(id(p1)) - locations of the object
# print(id(p1))

print(p1 == p2) # 1. w/o __eq__(), it would be false as the 2 objects would be stored in different memory locations