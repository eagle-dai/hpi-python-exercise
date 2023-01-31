import score # for local IDE
# T4 ----
# 31T8: 'treasure_hunt' should return the words in the provided sentence that 
# have an odd number of letters or have "o" as the second letter.
# Hint: Convert the sentence to a list of words, then loop over it.
def treasure_hunt(s):
    return 0
message = "your creative messages with programming news on journey "
message = message + "isn't really sure or stoppable"
print("th:",treasure_hunt(message)) # a word of encouragement :)


# T5 ----
# 31T9: 'translate' should handle a string with an english sentence as input.
# Use the provided ditionary 'woerterbuch' (not a function parameter, just hard-code it).
# to translate each word. The function should return a string (not a list).
woerterbuch = {'we':'wir', 'they':'sie', 'love':'lieben', 'drink':'trinken',
               'eat':'essen', 'cake':'kuchen', 'pears':'birnen', 'juice':'saft'}
def translate(sentence):
    return 0
print("t1:", translate("we love cake"))   # "wir lieben kuchen"
print("t2:", translate("they eat pears")) # "sie essen birnen"


# T6 ----
# 31T10: The function 'mirror' should swap the keys and values of a given dictionary.
# Note: dict keys must be unique, so the provided ditionary woerterbuch has unique values.
# Hint: create an empy output_dict = {}, then put in elements succesively.
def mirror(d):
    return 0
print("m:", mirror(woerterbuch)) #  {'wir': 'we', 'sie': 'they', 'lieben':  ...


# T7 ----
# 'select_key' should reduce the dictionary to only the keys "k","e","y".
# Use None for those not present.
# Hint: we covered failsafe key selection in lesson 2.3 dictionaries.
# The method doing that has a default that comes in handy for this task :)
def select_key(d):
    return 0
long_dict = {'e':29, 'f':83, 'k':42, 'r':50, 'q':46}
print("sk:",select_key(long_dict)) # {'k': 42, 'e': 29, 'y': None}

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
