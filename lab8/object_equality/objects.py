# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5
# Object_equality

# Define a class called Point with parameter of object
class Point(object):
    # Define a function called __init__ that takes in parameters self, x, and y to initialize attributes
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Define a function called __eq__ with parameters self and other to check object equality
    def __eq__(self, other):
        checkEqual = ((self.x == other.x) and (self.y == other.y))
        return checkEqual

# Define a class called Circle with parameter of object
class Circle(object):
    # Define a function called __init__ with parameters self, center, and readius to initialize attributes
    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius
