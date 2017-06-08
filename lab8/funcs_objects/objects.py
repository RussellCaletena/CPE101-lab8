# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Define a class called Point that takes in an object as a parameter
class Point(object):
    # Define a function called __init__ with parameters self, x, and y to initialize attributes
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

# Define a class called Circle that takes in an object as a parameter
class Circle(object):
    # Define a function called __init__ with parameters self, center, and radius to initialize attributes
    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius
