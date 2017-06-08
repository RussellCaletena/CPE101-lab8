# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

import unittest
from objects import *

class TestCases(unittest.TestCase):
    def test___eq__(self):
        aPoint = Point(5,5)
        thePoint = Point(5,5)
        self.assertEqual(aPoint, thePoint)

        anotherPoint = Point(-2,2)
        theOnePoint = Point()
        self.assertNotEqual(anotherPoint, theOnePoint)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
