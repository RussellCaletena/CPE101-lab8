# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5
# List_comp

# Define a class called Point that takes in an object as a parameter
class Point(object):
    # Define a function called __init__ that takes in parameters self, x, and y to initialize attributes
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Define a function called __eq__ that takes in parameters self and other to check object equality
    def __eq__(self, other):
        checkEqual = ((self.x == other.x) and (self.y == other.y) and (type(other) == Point))
        return checkEqual

    # Define a function called __repr__ that takes in parameter of self to format the point
    def __repr__(self):
        return ('({},{})'.format(self.x, self.y))

# Define a class called Circle that takes in an object as a parameter
class Circle(object):
    # Define a function called __init__ that takes in parameters of self, center, and radius to initialize attributes
    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius
