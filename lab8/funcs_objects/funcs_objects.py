# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from math import *


def distance(argument1, argument2):
    euclidDistance = 0
    # This is the distance formula for finding the distance between 2 points
    euclidDistance = sqr(((x2-x1)**2) + ((y2-y1)**2))
    return euclidDistance
    pass

# Write this function using a relational operator and without using any sort of conditional
def circles_overlap(argument1, argument2):
    # Two circles will overlap when the distance between their center points is less than the sum of the radii
    sumRadii = radius1 + radius2
    euclidDistance = sqr(((x2-x1)**2) + ((y2-y1)**2))
    # if circles overlap:
        #return True
    # else:
        #return False
