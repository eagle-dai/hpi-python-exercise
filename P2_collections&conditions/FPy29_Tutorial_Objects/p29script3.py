import score # for local IDE
# T6 ----
# Write a function `max_id` that takes a dictionary and hexID as input.
# It should return (not print) the maximum of the values for that key.
# It should return None if the hexID does not exist.
# You can test it with the dictionary below, just uncomment the block.

def max_id(dic, hid):0

mydict = {"4rbz70":[1,2,9,6,5], "pa05w8":[6,7,8]}
print(max_id(mydict, "4rbz70")) # 9
print(max_id(mydict, "z3gf67")) # None


# T7 ----
# Write a function `to_float` that converts the input to a float (and returns that).
# If the argument is a complex, it should instead print "complex input is not allowed"

def to_float(i):0

print("tf:",to_float(42)) # returns 42.0
to_float(42+007j)   # prints  "complex input is not allowed"


# T8 ----
# The hospital staff must be able to login to the information system.
# Write a function `login` with the parameters `usr` and `pwd`.
# It should conditionally print (not return) one of
# - wrong username
# - wrong password
# - wrong username and password
# - logged in successfully
# The correct login data is "Berry" and "p1234"
# (in real life, don't tell the user that specifically the password is wrong).

def login (usr, pwd):0

login("Berry", "p1234") # "logged in successfully"
login("Berry", "wrong") # "wrong password"

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
