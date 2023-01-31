import score # for local IDE
import numpy as np
import pandas as pd
# T1 ----
# In R, we can create a 1-D random walk with cumsum(rnorm(45)).
# Write the python function `rw` that creates a length 45 random walk starting at a given value.
# It should return the numbers rounded to one decimal place.
# Use the standard normal distribution (mu=0, sd=1) for step change size.
# Note: this task goes beyond the slides in this lesson, I know. It's going to be worth it.
# Hint: numpy has functions equivalent to the R functions.
def rw(start):
    return 0
print("rw:", rw(60), sep="\n") # e.g. [59.7 60.4 62.9 61.9 62.2 61.9 62.3 62.6 62.1  ... etc
# Note: the output differs on each run, of course.


# T2 ----
# Write the function `rwdf` that will return a pandas dataframe with the columns rw20, rw60, rw80.
# Each column should contain a random walk starting at that value (20, 60 and 80).
# Use the rw function from the previous task.
def rwdf():
    return 0
# Uncomment print calls once the task is solved.
# print("rwd:", rwdf().iloc[0:3], sep="\n") # should be e.g.:
#    rw20  rw60  rw80
# 0  21.2  59.7  80.6
# 1  20.4  58.8  81.1
# 2  19.1  60.3  78.9


# T3 ----
# The following function should create a DataFrame using (the code in) rwdf.
# It should then write NA somewhere in column 1.
# Choose any row for the location, except the first or last.
# Column two should obtain two consecutive NAs (immediately following each other).
# Lastly, put 3 consecutive NAs in column 3. Again, the row number does not matter.
# You may use a fixed position for the NAs.
# Note: use whatever NA value you like, as long as it is recognized by the pandas `is.na` method.
def rwdfna():
    return 0
# print("rwd2:", rwdfna().iloc[0:10], sep="\n") # should look like above, but with NAs where you put them.

# Now continue in script2.py

score.score() # for local IDE
