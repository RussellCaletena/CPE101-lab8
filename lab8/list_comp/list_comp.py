# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from funcs_objects import *
from objects import *
from math import *


listofPoints = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
listofPoints2 = [Point(3,-2), Point(5, 1), Point(-4, -6), Point(-7,7)]


def distance(P1):
    euclidDistance = sqrt(((P1.x)**2) + ((P1.y)**2))
    return euclidDistance

def distance_all(listOfPoints):
    distanceList = list(map(distance, listOfPoints))
    for i in range(len(distanceList)):
        print (distanceList[i])
    print (distanceList)
    return distanceList

def checkFirstQuadrant(P1):
    if P1.x > 0 and P1.y > 0:
        #P1.x *= 1
        #P1.y *= 1
        #Point2 = ('({},{})'.format(P1.x, P1.y))
        #print (P1)
        return (P1)
        #return (P1.x, P1.y)
        #print (Point(P1.x, P1.y))
        #print (P1.x, P1.y)
    else:
        pass
def are_in_first_quadrant(listOfPoints):
    firstQuadrantList = list(filter(checkFirstQuadrant, listOfPoints))
    for i in range(len(firstQuadrantList)):
        print (firstQuadrantList[i])
    print (firstQuadrantList)
    return firstQuadrantList

distance_all(listofPoints2)
#are_in_first_quadrant(listofPoints)
