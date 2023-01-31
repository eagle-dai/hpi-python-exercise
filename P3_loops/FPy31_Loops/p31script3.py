import score # for local IDE
# T8 ----
# 'treasure_hunt' should return the words in the provided sentence that 
# have an odd number of letters or have "o" as the second letter.
# Hint: Convert the sentence to a list of words, then loop over it.
def treasure_hunt(s):
    0

message = "words have four or many letters"
print("th1:",treasure_hunt(message)) # ['words', 'four', 'letters']
message = "your creative messages with programming news on journey "
message = message + "isn't really sure or stoppable"
print("th:",treasure_hunt(message)) # a word of encouragement :)


# T9 ----
# 'translate' should handle a string with an english sentence as input.
# Use the provided ditionary 'woerterbuch' (not a function parameter, just hard-code it).
# to translate each word. The function should return a string (not a list).
woerterbuch = {'we':'wir', 'they':'sie', 'love':'lieben', 'drink':'trinken',
               'eat':'essen', 'cake':'kuchen', 'pears':'birnen', 'juice':'saft'}
def translate(sentence):0
print("t1:", translate("we love cake"))   # "wir lieben kuchen"
print("t2:", translate("they eat pears")) # "sie essen birnen"


# T10 ----
# The function 'mirror' should swap the keys and values of a given dictionary.
# Note: dict keys must be unique, so the provided ditionary woerterbuch has unique values.
# Hint: create an empy output_dict = {}, then put in elements succesively.
def mirror(d):0
print("m:", mirror(woerterbuch)) #  {'wir': 'we', 'sie': 'they', 'lieben':  ...


score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE

# There are two additional optional tasks.
# They are in separate CodeOcean exercises (from a German Python course).
