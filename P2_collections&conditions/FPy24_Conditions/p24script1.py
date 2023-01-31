import score # for local IDE
# T1 ----
# between01 should return True if the input is between 0 and 1, False otherwise.
# There is a short elegant solution not needing any conditional code structure.
def between01(x):0

print("b1:",between01(-0.4)) # False
print("b2:",between01( 0.6)) # True
print("b3:",between01( 2.3)) # False 


# T2 ----
# Write a conditional branching procedure that tests whether blood pressure is 
# at or above 130.
# If yes, print("Patient has hypertension"). If not, print("Patient is fine")
def handle_patient(bloodpressure):0


# T3 ----
# James Bond is planning a restaurant meeting with 3 other secret agents.
# He will only accept a table for 4 close to a window or door (escape routes).
# The 'table' function should automate his reply according to the examples below.
# It should __print__ the output.
# Don't use a conditional return here, but practice combining conditions.
def table(n_seats, location):0

        
table(3, "window") # "We need exactly 4 seats. Do you have a different table?"
table(4, "middle") # "The table has the right size, but we need an escape route."
table(2, "middle") # "Please reread my previous request and offer another table."
table(4, "door")   # "We will take the table. Mix the Martinis, please."
table(4, "window") # "We will take the table. Mix the Martinis, please."

# Now continue in script2.py

score.score() # for local IDE
