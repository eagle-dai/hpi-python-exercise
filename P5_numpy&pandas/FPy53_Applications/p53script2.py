import score # for local IDE
from p53walk import walk
# In these tasks, your code is checked for containing the 'right' solution.
# Sorry for being strict here: there are elegant solutions I want you to use this time.
# Hence you don't need to create objects and can print the desired results directly.
# The "Tx:"-print statements are there for your convenience to keep the printout readable.

print("T4-7: random walk dataset:")
print(walk)

# T4 ----
# Check how many NAs `walk` contains per column.
# As noted above, you can print directly without variable assigment.
print("\nT4: number of NAs per column:")
print(0) # replace the 0 with the solution code.

# T5 ----
# Fill the NAs in `walk` with the mean of the respective column.
print("\nT5: imputation column means")
print(0)

# T6 ----
# The Na filling function also accepts the argument 'method'.
# In the documentation, find (and use) the Last Observation Carried Forwards method.
# Hint: it is not named locf.
print("\nT6: locf imputation:")
print(0)

# T7 ----
# Now impute the NAs by linear interpolation, see:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#interpolation
print("\nT7: linear imputation:")
print(0)

# Now continue in script3.py

score.score() # for local IDE
