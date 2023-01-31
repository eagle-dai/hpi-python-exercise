import score # for local IDE
# T1 ----
# 'safe_division' should divide the first by the second parameter.
# In case of an error, it should return a string as in the examples below.
# Hint: for the latter, Fstrings are elegant as usual.

def safe_division(a,b):
    return 0


print("sd1:", safe_division(12,5)) # 2.4
print("sd2:", safe_division(12,"five")) # 'A TypeError occured for 12/five.'


# T2 ----
# Expanding on T1, 'safer_division' should be more generic and informative.
def safer_division(a,b):
    return 0


print("sd3:", safer_division(12,5)) # 2.4
print("sd4:", safer_division(12,"five")) # "A TypeError occured for 12/five: unsupported operand type(s) for /: 'int' and 'str'."
print("sd5:", safer_division(12,0)) # 'A ZeroDivisionError occured for 12/0: division by zero.'


# T3 ----
# Expanding on T1+2, 'safest_division' should now provide a verbose log.
# This kind of logging can be useful in production code, where instead of being
# returned, the string may be printed to a logfile or a connection.
# Note: You need character string operations to get the intended string.
# Most of it is provided by the traceback mechanism from the lesson.
# Hint: replace linebreaks (and spaces) with something else.
def safest_division(a,b):
    return 0


print("sd6:", safest_division(12,5)) # 2.4
print(safest_division(12,"five")) # should look like this:
# LOGGING ERROR On 2023-01-16 at 17:42, with call: 12/five
# -> File "p41script1.py", line 42, in safest_division
# -> TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Use the current date and time instead of 2023-01-16 17:42.
# Note that spaces and line breaks must match exactly.
# While this is annoying, the logging format may be a given requirement.

    
# Now continue in script2.py

score.score() # for local IDE
