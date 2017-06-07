# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
    def test_Point(self):
        P1 = Point(5,3)
        self.assertEqual(P1.x , 5)
        self.assertEqual(P1.y, 3)

        P2 = Point(0,0)
        self.assertEqual(P2.x , 0)
        self.assertEqual(P2.y, 0)

    def test_Circle(self):
        Circle1 = Circle(Point(1, -3), 7)
        self.assertEqual(Circle1.center.x, 1)
        self.assertEqual(Circle1.center.y, -3)
        self.assertEqual(Circle1.radius, 7)

        Circle2 = Circle(Point(), 5)
        self.assertEqual(Circle2.center.x, 0)
        self.assertEqual(Circle2.center.y, 0)
        self.assertEqual(Circle2.radius, 5)

    def test_distance(self):
        P1 = (0,0)
        P2 = (4,0)
        self.assertEqual(distance(P1, P2), 4)


    def test_circles_overlap(self):
        pass

   # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
