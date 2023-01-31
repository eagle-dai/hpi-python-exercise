import score # for local IDE
# T1 ----
# Write a function named 'amount_double'.
# For any given input, it should return twice the amount (absolute value) of the input.


# print("am_dob1:", amount_double(-5.5)) # should be 11
# print("am_dob2:", amount_double(7)   ) # should be 14


# T2 ----
# Write the function 'read_number'. It should accept a filename as input.
# It should read the content of that file (google, Refcard, past lesson),
# convert it to a float and print "The number in **.txt is **".
# Replace the asterixes, obviously.
# Note: I ask for _printed_ output here, not for _returned_ output.


if False: # Set to True for execution
    read_number("p14zone1.txt") # "The number in p14zone1.txt is 42.0"
    read_number("p14zone2.txt") # "The number in p14zone2.txt is 99.6"


# T3 ----
# Write a function returning the input +- 5 (i.e. both added and substracted).
# The output should be a tuple with the smallest number first.

# print("pm5:", plus_minus_five(28)) # should be the tuple (23, 33)


score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
