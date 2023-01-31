import score # for local IDE
import numpy as np
# 'array' in this excercise always means a numpy array!

# T1 ----
# Create an array with the integers 156 to 186 (both included).
linear_vals = 0
print("lv:", linear_vals, sep="\n")


# T2 ----
# Write a function that, from a given 1D array, selects + returns the elements
# at position 1,4,7,10,13,... regardless of how long the array is.
# Note: element location 1,4,7,... is 0,3,6,... in Python.
# Note: there is an easy and elegant solution for this.
def every_third(a): # feel free to rename the parameter
    return 0
print("et:", every_third(np.arange(2,20))) # should be [ 2  5  8 11 14 17]


# T3 ----
# Create the 2D array `some_numbers` with the values as shown below.
# Hint: use CTRL+ALT+DOWN (or ALT + mouse) for a multiline cursor.
some_numbers = 0
# 1 1 2 8 2 8
# 6 4 3 5 0 5
# 0 1 1 8 0 1
# 4 4 1 9 8 2
# 3 3 7 5 0 3
# 3 1 1 1 3 4
# 7 2 8 2 1 0
# 2 0 9 1 9 9
# 0 5 9 4 1 4
# 1 7 8 0 4 8
# 5 5 7 5 4 0
# 3 8 0 5 1 5


# T4 ----
# The following function should return the first column of a given 2D array.
def column_one(a):
    return 0
print("co:", column_one(some_numbers)) # should be [1 6 0 4 3 3 7 2 0 1 5 3]

# Now continue in script2.py

score.score() # for local IDE
