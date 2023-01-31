import score # for local IDE
# T1 ----
# In the blood analysis center of the hospital, measurements are repeated several times.
# This way, individual results can be checked for consistency.
# Write a function `med_avg1` that takes a list of values.
# It should return a tuple containing their median and mean (in that order).
# Tip: use the Python module 'statistics'.
def med_avg1(l):
    return 0
print("ma1:", med_avg1([4.6, 5.8, 4.5, 4.9])) # should be (4.75, 4.95)


# T2 ----
# Python does not have a built-in NA representor, but 'None' is used sometimes.
# Copy the body of `med_avg1` from the previous task for `med_avg2`.
# Change it to exclude inputs that are `None`.
# For this task, not all values will be None.
# Tip: Succesively delete None elements (as long as any are present).
# Tip: If you want to use a for loop, don't modify the iterator (object looped over).
# Note: in real data analysis, numpy.nan is used (see next week).
def med_avg2(l):
    return 0
print("ma2:", med_avg2([None,2,4,4] )) # (4, 3.3333333333333335)
print("ma2:", med_avg2([None,None,4])) # (4, 4)


# T3 ----
# Copy the body of `med_avg2` from the previous task for `med_avg3`.
# `med_avg3` my not fail if all inputs are None, but should return None for both.
# Note: you may use the coding principle from this week, but don't have to.
def med_avg3(l):
    return 0
print("ma3:", med_avg3([None,15,4,3,2] )) # (3.5, 6)
print("ma3:", med_avg3([None,None,None])) # (None, None)

# Now continue in script2.py

score.score() # for local IDE
