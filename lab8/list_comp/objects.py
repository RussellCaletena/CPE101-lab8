# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5
# List_comp

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        checkEqual = ((self.x == other.x) and (self.y == other.y))
        return checkEqual
    def __repr__(self):
        return ('({},{})'.format(self.x, self.y))

class Circle(object):
    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius
