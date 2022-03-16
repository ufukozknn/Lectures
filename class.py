class Apple:
    i = 10

    def __init__(self) -> None: # a constructor function for instance objects
        pass

    def __init__(self, color, size = 'sz') -> None: # a constructor function for instance objects
        self._color = color # here we define a new attribute for instance object of Apple
        self._size = size # here we define a new attribute for instance object of Apple

    def f():
        print (3)
        print (Apple.i)

    def g(self): # is a method of an instance object of Apple
        pass

# This the end of the class declaration. Python creates an object of class Apple 
# (not an instance object but a class object) automatically

print (Apple.i)
Apple.f() # f is a function of class Apple

x = Apple("red", "large") # creates an instance object. This implicitly calls Apple.__init__(x)
x.i = 20
y = Apple("green")
y.i = 30

print (x._color) ## not object oriented
print (y._color)

x.g() # Python calls Apple.g(x)
