# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
    '''
    def test_distance_all(self):
        list1 = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
        self.assertAlmostEqual(distance_all(list1), [1.4142136, 6.4031242, 7.2801099, 9.486833, 5.656854])

        list2 = listofPoints2 = [Point(3,-2), Point(5, 1), Point(-4, -6), Point(-7,7)]
        self.assertAlmostEqual(distance_all(list2), [3.60555513, 5.099019, 7.2110255, 9.8994949])
        pass
    '''
    def test_are_in_first_quadrant(self):
        list1 = [Point(1,1), Point(-5,4), Point(2,-7), Point(-9, -3), Point(4,4)]
        self.assertEqual(are_in_first_quadrant(list1), [(1,1), (4,4)])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
