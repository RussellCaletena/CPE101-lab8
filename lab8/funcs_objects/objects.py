# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

class Point(object):
    def __init__(self, newX = 0, newY = 0):
        self.x = newX
        self.y = newY
    
P1 = Point()
P1.x = 5
P1.y = 10
print (P1.x,',',P1.y)

class Circle(object):
    def __init__(self, circleCenter = 0, circleRadius = 0):
        self.center = circleCenter
        self.radius = circleRadius

C1 = Circle()
C1.center = (5,10)
print (C1.center)
