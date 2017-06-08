# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Import libraries
from funcs_objects import *
from objects import *
from math import *

# Create two lists containing points
listofPoints = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
listofPoints2 = [Point(3,-2), Point(5, 1), Point(-4, -6), Point(-7,7)]

# Define a function called distance that takes in P1 as a parameter and returns the distance
def distance(P1):
    euclidDistance = sqrt(((P1.x)**2) + ((P1.y)**2))
    return euclidDistance

# Define a function called distance_all that takes in a list of Points as a paramter and returns a list of the distance from each point to the origin
def distance_all(listOfPoints):
    distanceList = list(map(distance, listOfPoints))
    for i in range(len(distanceList)):
        print (distanceList[i])
    print (distanceList)
    return distanceList

# Define a function called checkFirstQuadrant that takes in P1 as a parameter and returns the point if it is in the 1st quadrant
def checkFirstQuadrant(P1):
    if P1.x > 0 and P1.y > 0:
        return (P1)
    else:
        pass

# Define a function called are_in_first_quadrant that takes in a list of Points as a parameter and returns a list of points that are in the 1st quadrant
def are_in_first_quadrant(listOfPoints):
    firstQuadrantList = list(filter(checkFirstQuadrant, listOfPoints))
    for i in range(len(firstQuadrantList)):
        print (firstQuadrantList[i])
    print (firstQuadrantList)
    return firstQuadrantList

# Test functions to run
#distance_all(listofPoints2)
#are_in_first_quadrant(listofPoints)
