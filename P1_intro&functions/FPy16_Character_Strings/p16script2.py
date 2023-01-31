import score # for local IDE
# T6 ----
# Write a function that returns the last 8 symbols of the input.
def last_eight(i):
    0
print("le:", last_eight("asdfghjklqwert")) # should be jklqwert


# T7 ----
# Write a function that checks whether the input contains "berry".
def has_berry(i):
    0
print("hb1:", has_berry("apple, melon, pear")) # should be False
print("hb2:", has_berry("strawberry is a delecious fruit!")) # should be True


# T8 ----
# Trying some real life application:
# An OCR (optical character recognition) has read nurses notes in a hospital.
# Now we need to find all event logs that start with "op1", the operation room 1.
# Some nurses just wrote op1, some spelled out operation1.
# Sometimes, the o (letter) got transcribed as 0 (the number).
# Some nurses wrote in upper case, some lower, some mixed.
# Some spaces were discerned by the OCR.
# All these instances need to be found.
# Write a function that returns True or False accordingly.
# Note: you can chain charstring methods!
# Hint: we ignore double spaces and all other real life concerns for now.

def is_op1(i):
    0

def print_test_op1(i):
    print(is_op1(i), " (", i, ")", sep="")
print_test_op1("operation 1: fully prepped")      # True
print_test_op1("0peration1 doctor smith arrived") # True
print_test_op1("OP2 cleaned 10:15")               # False


# T9 ----
# NOTE: This is a future task, there is no test implemented yet!
# Now, using regular expressions with the 're' module,
# clean_op_log should return the OP room number and the log as in the examples.
# It must also handle multiple spaces and multi-digit room numbers (e.g. 12).
# Logs that do not start with a discernable OP number should get an x.
# Separators like :, - or _ should be discarded.
# Note: in real life, you might want a list with the number and the log entry.
# For now, we'll just stick with a character string with a minus.
# NOTE again: This task is not autograded yet.

def clean_op_log(i):
    0
print("eo1:", clean_op_log("Op  1 ready 14:35")) # 1 - ready 14:35
print("eo2:", clean_op_log("operation2: restocked")) # 2 - restocked
print("eo3:", clean_op_log("0P13 refilled hand-sanitizer")) # 13 - refilled hand-sanitizer
print("eo4:", clean_op_log("handled 2 patients in op1")) # x - handled 2 patients in op1


score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
