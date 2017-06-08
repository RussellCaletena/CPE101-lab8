# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Import libraries
from math import *
from objects import *

# Define a function called distance with parameters P1 and P2 that returns distance between two points
def distance(P1, P2):
    euclidDistance = sqrt(((P2.x-P1.x)**2) + ((P2.y-P1.y)**2))
    return euclidDistance

# Define a function called circles_overlap with parameters Circle1 and Circle2 that returns a boolean statement if two circles overlap
def circles_overlap(Circle1, Circle2):
    sumRadii = Circle1.radius + Circle2.radius
    euclidDistance = sqrt(((Circle2.center.x-Circle1.center.x)**2) + ((Circle2.center.y-Circle1.center.y)**2))
    overlap = euclidDistance < sumRadii
    return overlap
