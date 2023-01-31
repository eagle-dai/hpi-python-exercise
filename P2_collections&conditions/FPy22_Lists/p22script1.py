import score # for local IDE
# T1 ----
# Create a list with the elements nutrition, activity, obesity, injury.
health = 0

# T2 ----
# Print the nutrition element by selecting the position (indexing).


# T3 ----
# Create a copy of 'health' called 'total_health'.
# If 'total_health' is changed, 'health' should not be affected.


# T4 ----
# Add the following list to 'total_health'.
# Bonus: try different approaches to this task.
more_health = ["environment", "genetics", "aids", "monitoring", "hospital"]


# T5 ----
# Using an Fstring, the 'info' function should print:
"There are __ keywords in __. The last three are: [___]"
# containing the number of elements and the last three elements.
# Hint: use negative indexing.
# We can access variables by name with   globals()["name"]
# (seems uncommon in Python, but see e.g. here https://stackoverflow.com/q/1538342 ):
def info(name):
   x = globals()[name] # globals() gives all the variables in the global environment
   print(x)

info("health") # should print (not return):
# "There are 4 keywords in health. The last three are: ['activity', 'obesity', 'injury']"

# Now continue in script2.py

score.score() # for local IDE
