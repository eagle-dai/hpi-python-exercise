import score # for local IDE
# An ambulant care facility for elderly people hires you for health-related IT.
# You are to program the backbone of their resident management system in Python.

# T1 ----
# Implement a resident class with the initiation parameters 'name' and 'born',
# aka "attributes". Here, born means the year of birth.
# Hint: remember the convention for capitalization.
# We will add methods and input checks successively right here.


# T2 ----
# Create the object 'res1' (instance of the T1 class) for James Smith, born in 1949.
res1 = 0
print("r2:", res1) # <__main__.Resident object at 0x0000023AC9848580>
# Uncomment all further print statements once you have solved T1.
# print("r2b:", res1.born) # 1949


# T3 ----
# Going a little beyond the slides: 
# class instances cannot only have attributes and methods, but also class variables.
# In the referenced tutorial, this is explained at:
# https://dellwindowsreinstallationguide.com/python-creating-a-custom-class-and-using-class-special-methods/#class-variables
# I can also recommend this page:
# https://pynative.com/python-class-variables/
# All Resident objects should have the variable 'current' with the current year.
# Simply change the class definition above.
# Hint: search online how to get the current year.

# print("r3c:", res1.current) # 2023


# T4----
# Now add an 'age' method that returns the age of the resident.
# Use the 'current' variable implemented in T3.
# Again, add the code above.

current = 2013
born = 1996
# print("r4a:", res1.age()) # should be 74 (i.e. not depend on global variables)


# T5 ----
# Create 'res2' for Emma Hill, born in 1961.
# (This is mainly for some scoring tests, hence this now very simple task.)
res2 = 0


# T6 ----
# If the given year for born is not an integer,
# instantiating a Resident should generate a TypeError as below.
# Again, change the class definition above.
# Hint: to replace symbols in 'type' output, first convert it to a string (lesson 1.3).
try:
    res3 = Resident("Hanna Brown", '1954-04-28')
except Exception as e:
    print(f"r6: {type(e).__name__}: {e} - intentionally generated.")
    # TypeError: 'born' must be an integer, not class 'str'.

# T7 ----
# If the given year is not humanly possible (older than 130)
# or younger than the minimal facility resident age (18), a ValueError should
# inform the user of the Resident class right away to check the birthyear.
# Note: this should be valid in any year, so use 'self.current' again.
# Note: in real life in a user interface, a re-entry may be prompted instead.
# To maintain the Resident class, there should only be one source code batch.
# So as before: add the input checks to the class definition above.

try:
    res4 = Resident("John Miller", 1653)
except Exception as e:
    print(f"r7: {type(e).__name__}: {e} - intentionally generated.")
    # ValueError: Please check birth year. 1653 is not allowed.


score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
