# Lab8
#
# Name: Russell Caletena
# Instructor: S. Einakian
# Section: 5

# Define a function called epsilon_equal with parameters n, m, and epsilon and returns a boolean
def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)
