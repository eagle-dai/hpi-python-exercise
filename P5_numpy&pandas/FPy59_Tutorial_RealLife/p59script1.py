import score # for local IDE
import numpy as np
# T1 ----
# Write a function that takes a list of 12 values and converts them to a 2x6 numpy array.
def l2ar(x):
    return 0
print("l2ar:", l2ar([9,3,2,0,7,7,8,5,0,8,8,0]), sep="\n") # should be:
#[[9 3 2 0 7 7]
# [8 5 0 8 8 0]]


# T2 ----
# set2seven should accept an array and set the value in the third row, second column to 7.
def set2seven(a):
    return 0
print("set2seven:", set2seven(np.zeros((4,3))), sep="\n") # should be:
#[[0. 0. 0.]
# [0. 0. 0.]
# [0. 7. 0.]
# [0. 0. 0.]]


# T3 ----
# rowmeans should return the arithmetic average per row of an array.
def rowmeans(a):
    return 0
print("rowmeans:", rowmeans(np.array([[3,5,4,7],[7,9,8,5],[2,4,3,1]])), sep="\n")
# should be: [4.75 7.25 2.5 ]

# Now continue in script2.py

score.score() # for local IDE
