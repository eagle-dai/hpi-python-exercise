import score # for local IDE
# T1 ----
# Read the provided story into Python.
# Obtain a character string named `story` that contains the full content.
# Use code that will never leave file connections opened.


# T2 ----
# How often does the word "number" occur in the story?
# Note: this is a subsequent task to T1. It is not related to importing.
# collections.Counter is for lists, not for a character string.

number_of_numbers = 0
print("nn:", number_of_numbers)


# From now on, the function structure is normally already given.
# This way, a print statement can be provided for your convenience.


# T3 ----
# Use the 'random' module to generate a decimal number 
# between 1 (inclusive) and 10 (exclusive).
# Hint: random.random() gives a number between 0 and 1, i.e. 0.0 <= random() < 1.0.
def number1_10(): 
    return 0
print("n1-10:", number1_10())


# T4 ----
# Import the 'initialize' function and 'version' string from the provided tracker file.
# Then use both to generate a fitness tracking descriptor.
fitness_track_description = 0
print("ftd:", fitness_track_description)


score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
