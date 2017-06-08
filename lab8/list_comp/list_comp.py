# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from funcs_objects import *
from objects import *
from math import *


listofPoints = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
print (listofPoints[0])

def distance(P1):
    euclidDistance = sqrt(((P1.x)**2) + ((P1.y)**2))
    return euclidDistance

def distance_all(listOfPoints):
    distanceList = list(map(distance, listOfPoints))
    #print (distanceList)
    #return distanceList

'''
def distance_all(list9):
    origin = Point()
    return list(distance(origin, item) for item in map(distance(origin,item),list9))
'''

'''
def distance_all([Point(1,0), Point(-5,4), Point(2,-7), Point(-9, -3)]):
    for item in list1:
        return list(map(sqrt(((item.x)**2) + ((item.y)**2)), list1))
'''
def checkFirstQuadrant(P1):
    if P1.x > 0 and P1.y > 0:
        Point2 = ('({},{})'.format(P1.x, P1.y))
        print (Point2)
        return (Point2)
        #return (P1.x, P1.y)
        #print (Point(P1.x, P1.y))
        #return P1.x, P1.y
    else:
        pass
def are_in_first_quadrant(listOfPoints):
    firstQuadrantList = list(filter(checkFirstQuadrant, listOfPoints))
    #firstQuadrantList = list(filter(lambda P1: P1.x > 0 and P1.y > 0, listOfPoints))
    print (firstQuadrantList)

distance_all(listofPoints)
are_in_first_quadrant(listofPoints)
