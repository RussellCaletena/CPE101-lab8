# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from math import *

#              x1,y1
#Point()     = (0,0)
#              x2,y2
#Point(4,0)  = (4,0)

def distance(P1, P2):
    # This is the distance formula for finding the distance between 2 points
    euclidDistance = sqrt(((P2.x-P1.x)**2) + ((P2.y-P1.y)**2))
    return euclidDistance

# Write this function using a relational operator and without using any sort of conditional
def circles_overlap(Circle1, Circle2):
    # Two circles will overlap when the distance between their center points is less than the sum of the radii
    sumRadii = Circle1.radius + Circle2.radius
    euclidDistance = sqrt(((Circle2.center.x-Circle1.center.x)**2) + ((Circle2.center.y-Circle1.center.y)**2))
    overlap = euclidDistance < sumRadii
    return overlap
    # if circles overlap:
        #return True
    # else:
        #return False
