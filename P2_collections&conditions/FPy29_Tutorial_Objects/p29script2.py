import score # for local IDE
# Revisiting our Hospital Information System (HIS) from ex 1.9 Tutorial Intro:
# The HIS is to be connected to a fitness tracker analysis software called fitrac.
# It uses hexadecimal IDs to anonymously identify study participants.
# The app records screentime (in minutes) and
# acceleration (normalized score from the gyroscope).

# T3 ----
# Import the function 'fitrac_generator' from the file 'p29fitrac.py'.
# Run the function and assign the output to the variables
# hexID, screentime and acceleration.
# Tip: You only need a single line of code.
from p29fitrac import fitrac_generator

# print("ID:", hexID, "  Time:", screentime, "\nAcc:", acceleration)


# T4 ----
# With the values below, build a dictionary called `fitrac4`.
# The keys should be the hexIDs, the values the corresponding acceleration as a list.
# Remember: keep the `ALT` key pressed to create a multiline cursor.
# NOTE: The current Rstudio version has a bug. Press ALT again after setting
#       the multiline cursor.https://github.com/rstudio/rstudio/issues/12470#issuecomment-1360085526
# That way you can add the needed syntax to all lines at once.
# You may have line breaks and indentation to keep the code nicely formated below each other.
'''
hexID, acceleration values
9c5147,  1.413, 3.523, 1.410, 4.338, 1.778, 1.518
c76862,  1.426, 1.446, 1.879, 7.327, 3.151, 1.643
6cf5e1,  1.750, 2.357, 1.450, 1.539, 1.965, 4.958
b743e4,  1.827, 1.962, 3.872, 3.917, 1.829, 1.968
'''


import pprint # for pretty printing without full output. str(obj, max.level=1) in R.
pp = pprint.PrettyPrinter(depth=1)
#pp.pprint(fitrac4)


# T5 ----
# 5a. From `orig`, remove the entry 'tz'.
# 5b. Overwrite / expand the information in `orig` with the `new` data.
from p29fitrac import orig, new


print("orig:", orig)

# Note: after deleting an entry, re-importing it will not refresh the object.
# To avoid the KeyError: 'tz' when running the script multiple times, you can:
# - Run subsequent scoring from another script
# - Run   orig = orig.copy()   between importing and changing orig
# - Restart R (CTRL + SHIFT + F10  /  CMD + SHIFT + 0) to restart the Python interpreter
# - Reload the previously imported module and re-import the objects:
if False: # Don't leave this as True after solving the task, or it won't be scored.
    import importlib, p29fitrac
    importlib.reload(p29fitrac)
    from p29fitrac import orig, new
# now you can remove the tz key again


# Now continue in script3.py

score.score() # for local IDE
