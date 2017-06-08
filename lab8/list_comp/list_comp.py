# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from funcs_objects import *
from objects import *
from math import *


listofPoints = [Point(1,0), Point(-5,4), Point(2,-7), Point(-9, -3)]
'''
for item in listofPoints:
    print (x, y)
'''
#origin = (0,0)
#distanceList = []
# for item in listofPoints:
    #distance = 0
    #take x and y coordinates of origin and point and compute distance
    #append distance to a list
    #distanceList.append(distance)
#return distanceList

def distance(P1):
    euclidDistance = sqrt(((P1.x)**2) + ((P1.y)**2))
    return euclidDistance

def distance_all(listOfPoints):
    distanceList = list(map(distance, listOfPoints))
    print (distanceList)
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

def are_in_first_quadrant():
    pass

distance_all(listofPoints)
