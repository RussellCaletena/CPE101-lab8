# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Import libraries
import unittest
from list_comp import *
from objects import *

# Define a class called TestCases that takes in unittest.TestCase as a parameter
class TestCases(unittest.TestCase):
    # Define a function called test_distance_all that tests the distance function and returns a list of distances
    def test_distance_all(self):
        list1 = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
        self.assertEqual(distance_all(list1), [1.4142135623730951,  6.4031242374328485, 7.280109889280518, 9.486832980505138, 5.656854249492381])

        list2 = [Point(3,-2), Point(5, 1), Point(-4, -6), Point(-7,7)]
        self.assertAlmostEqual(distance_all(list2), [3.605551275463989, 5.0990195135927845, 7.211102550927978, 9.899494936611665])

    # Define a function called test_are_in_first_quadrant that tests the are_in_first_quadrant function and returns a list of points in the 1st quadrant
    def test_are_in_first_quadrant(self):
        list1 = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
        self.assertEqual(are_in_first_quadrant(list1), [Point(1,1), Point(4,4)])

        list2 = listofPoints2 = [Point(3,-2), Point(5, 1), Point(-4, -6), Point(-7,7)]
        self.assertEqual(are_in_first_quadrant(list2), [Point(5,1)])

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
