# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5
# Object_equality

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        checkEqual = ((self.x == other.x) and (self.y == other.y))
        return checkEqual

class Circle(object):
    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius
