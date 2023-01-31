import score # for local IDE
# T6 ----
# 'has_key' should:
# - remove the "initiator" key-value-pair from the given dictionary,
# - then check whether it has a certain key, given as the second parameter.
# It should not mess with global objects.
# Note: As usual, you may use different parameter names if wanted.
def has_key(d, k): 0

ex_dict = {'info':"example dict", 'initiator':56, 'date':[2023,1,13]}

print("hk1:", has_key(ex_dict,"info"))      # True
ex_dict['initiator'] # must still be present now
print("hk2:", has_key(ex_dict,"amount"))    # False
print("hk3:", has_key(ex_dict,"initiator")) # False


# T7 ----
# For a given dictionary and key, 'get_val' should return a character string
# with "The value of _key_ is: _value_" (substitute the placeholders, of course).
# If the dict does not contain the key, the part after the colon should be
#                                       KEY NOT PRESENT
# Note: you don't need conditional code to solve this!
# Hint F-strings are awesome and make this very simple :)
def get_val(d,k): 0

print("gv1:", get_val(ex_dict, "info")) # The value of info is: example dict
print("gv1:", get_val(ex_dict, "data")) # The value of data is: KEY NOT PRESENT


# T8 ----
old_info = {'D':75, 'A':69, 'C':20, 'B':54, 'E':23}
new_info = {'A':97, 'E':34, 'F':17, 'B':83}
# Combine the two dictionaries so that:
# values in new_info replace values for those keys in old_info,
# keeping all the entries that are not in new_info and
# adding all that are not in old_info.
final_info = old_info.copy() # work with this copy, keeping both other dicts.


print("fi:", final_info)

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
