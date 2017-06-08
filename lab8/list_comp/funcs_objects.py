# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from math import *
from objects import *

def distance(P1, P2):
    euclidDistance = sqrt(((P2.x-P1.x)**2) + ((P2.y-P1.y)**2))
    return euclidDistance

def circles_overlap(Circle1, Circle2):
    sumRadii = Circle1.radius + Circle2.radius
    euclidDistance = sqrt(((Circle2.center.x-Circle1.center.x)**2) + ((Circle2.center.y-Circle1.center.y)**2))
    overlap = euclidDistance < sumRadii
    return overlap
