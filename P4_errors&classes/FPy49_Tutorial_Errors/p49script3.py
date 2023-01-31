import score # for local IDE
# T6 ----
# You are developing the fitrac fitness tracker app.
# Write a function `scale_acc` that takes a dictionary as input.
# It should compute and return 1/int(maximum acceleration).
# The acceleration values are assumed to be at the key "acc".
# This function is intended for production, so it should never fail. 
# All printout is logged, hence print (not return) an error message if applicable.
# For a KeyError,      print("scale_acc error: there is no key 'acc'.")
# For any other error, print("scale_acc error: another error occured.")
def scale_acc(d):
    return 0
print("sa1:", scale_acc({'hexID':"b81df8", 'acc':[1.209, 1.258, 8.317]})) # 0.125
scale_acc({'hexID':"602b83", 'ACC':[6.546, 2.866, 5.173]}) # [...] no key 'acc'
scale_acc({'hexID':"d7ab81", 'acc':[6.546, "2.8", 5.173]}) # [...] other error


# T7 ----
# Copy `scale_acc` from the last task and rename it to `scale_acc2`.
# Wel'll now improve the printed information. 
# For KeyError,          print("scale_acc error for id 'xxxxxx': there is no key 'acc'")
# For ZeroDivisionError  print("scale_acc error for id 'xxxxxx': the max is zero")
# For any other error,   print("scale_acc error for id 'xxxxxx': xxxError: xxxMessage")
# xxxxxx is a placeholder, the message should contain the actual hexID
# xxxError/xxxMessage should be the error name and message.
# Hint1: Fstrings are nice :)
# Hint2: If you want to use sys.exc_info():
#      `sys.exc_info()[0]` is printed as e.g. "<class 'TypeError'>", but the
#       message should be clean and only contain "TypeError"
#       The output of `sys.exc_info()[0]` is not yet a character string.
#       `sys.exc_info()[1]` contains the actual error message
#       For a much simpler approach, see the slides :).
def scale_acc2(d):
    return 0
print("sa2:",scale_acc2({'hexID':"b81df8", 'acc':[1.209, 1.258, 2.391]})) # 0.5
print("sa2:",scale_acc2({'hexID':"6d83c0", 'acc':[6.546, 2.866, 5.173]})) # 0.166

# The following comments show possible real-life errors, not the intended message.
scale_acc2({'hexID':"602b83", 'ACC':[6.546, 2.866, 5.173]}) # key misspelled
scale_acc2({'hexID':"d7ab81", 'acc':[6.546, "2.8", 5.173]}) # charstring
scale_acc2({'hexID':"ef6f69", 'acc':[-6.546, -2.866, 0]})   # max is zero
scale_acc2({'hexID':"a6e7c6", 'acc':[]})                    # list is empty
scale_acc2({'hexID':"57cd08", 'acc':["seven"]})             # nonnumeric string
scale_acc2({'hexID':"gd916t", 'acc':12345})                 # non-list to max

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
