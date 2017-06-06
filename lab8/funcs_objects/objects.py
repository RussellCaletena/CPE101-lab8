# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Circle(object):
    def __init__(self, center = Point(), radius = 0):
        self.center = center
        self.radius = radius
