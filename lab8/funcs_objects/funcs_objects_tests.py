# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Import libraries
import unittest
from objects import *
from funcs_objects import *

# Define a class called TestCases with parameter unittest.TestCase
class TestCases(unittest.TestCase):
    # Define a function called test_Point that tests the Point class
    def test_Point(self):
        P1 = Point(5,3)
        self.assertEqual(P1.x , 5)
        self.assertEqual(P1.y, 3)

        P2 = Point(0,0)
        self.assertEqual(P2.x , 0)
        self.assertEqual(P2.y, 0)

    # Define a function called test_Circle that tests the Circle class
    def test_Circle(self):
        Circle1 = Circle(Point(1, -3), 7)
        self.assertEqual(Circle1.center.x, 1)
        self.assertEqual(Circle1.center.y, -3)
        self.assertEqual(Circle1.radius, 7)

        Circle2 = Circle(Point(), 5)
        self.assertEqual(Circle2.center.x, 0)
        self.assertEqual(Circle2.center.y, 0)
        self.assertEqual(Circle2.radius, 5)

    # Define a function called test_distance that tests the distance function
    def test_distance(self):
        P1 = Point(0,0)
        P2 = Point(4,0)
        self.assertEqual(distance(P1, P2), 4)

        P3 = Point(-7, 3)
        P4 = Point(12, -4)
        self.assertAlmostEqual(distance(P3, P4), 20.2484567)

    # Define a function caled test_circles_overlap that tests circles_overlap function
    def test_circles_overlap(self):
        Circle1 = Circle(Point(), 3)
        Circle2 = Circle(Point(8,0), 1)
        self.assertEqual(circles_overlap(Circle1, Circle2), False)

        Circle3 = Circle(Point(), 2)
        Circle4 = Circle(Point(), 4)
        self.assertEqual(circles_overlap(Circle3, Circle4), True)
        
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
