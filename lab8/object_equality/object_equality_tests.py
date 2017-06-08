# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Import libraries
import unittest
from objects import *

# Define a class called TestCases with parameter unittest.TestCase
class TestCases(unittest.TestCase):
    # Define a function called test___eq__ that tests the __eq__ function
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
