import score # for local IDE
import numpy as np

# T5 ----
# `stri2ar` should take a string with 20 digits and convert them to a 4x5 array.
# Hint: it takes only a single function call to convert a string to a list.
def stri2ar(s):
    return 0
print("s2ar:",stri2ar("51557701318295261880"), sep="\n") # should be:
#[['5' '1' '5' '5' '7']
# ['7' '0' '1' '3' '1']
# ['8' '2' '9' '5' '2']
# ['6' '1' '8' '8' '0']]


# T6 ----
# Now convert the output to integers. We didn't cover this in the slides.
# As with real life requirements, search online how to do this elegantly.
# Feel free to copy your solution from the last task and expand on it.
def stri2numar(s):
    return 0
print("s2numar:",stri2numar("51557701318295261880"), sep="\n") # should be:
#[[5 1 5 5 7]
# [7 0 1 3 1]
# [8 2 9 5 2]
# [6 1 8 8 0]]


# T7 ----
# Now compute one-tenth of each value.
def stri2tenths(s):
    return 0
# The code (incl return) can be 52 symbols short        | <- up to here
# (even without re-using stri2ar / stri2numar)
print("s2tenths:",stri2tenths("51557701318295261880"), sep="\n") # should be:
#[[0.5 0.1 0.5 0.5 0.7]
# [0.7 0.  0.1 0.3 0.1]
# [0.8 0.2 0.9 0.5 0.2]
# [0.6 0.1 0.8 0.8 0. ]]


# T8 ----
# Now determine per column whether all original values in that column are > 2.
# Hint: do not divide by ten. Also, two lines of code will make the function more readable.
#       Or re-use functions from previous tasks.
def stri2logic(s):
    return 0
print("s2logic:",stri2logic("51557701318295261880"), sep="\n") # should be:
# [ True False False  True False]


# B1 ----
# Ungraded Bonus task:
# why is the following comparison False? What can you do about it?
arr = np.arange(1,12)
print("equal:", np.array_equal(arr/10, arr*0.1))

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
