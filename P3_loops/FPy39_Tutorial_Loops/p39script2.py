import score # for local IDE
# T3 ----
# Write the function `longest_word` that accepts a charstring as input.
# It should return (not print) the length of the longest word.
# Hint: Split the input, then loop over each word checking it's length.
# Tip: Use list comprehension for a quick elegant solution.

def longest_word(sentence): # as usual, feel free to rename the parameter
    return 0

print("lw1:",longest_word("This has abundantly long words")) # should be 10
print("lw2:",longest_word("aaaaaaaa ddd ggggg")) # should be 8


# T4 ----
# Write the function `longest_word_without` that accepts two charstrings as input.
# It should return the length of the longest word that does not contain a given letter.
# If no word exists without that letter, the output should be 0.
# Hint: `max` has the parameter `default`. Just saying.
# Tip: list comprehension!

def longest_word_without(sentence, letter):
    return 0

print("lww1:",longest_word_without("This is a sentence with words" ,  "e")) # 5
print("lww2:",longest_word_without("This is a sentence with words" ,  "a")) # 8
print("lww3:",longest_word_without("aaaaaaaaa ddd gggggg" ,  "a") )         # 6
print("lww4:",longest_word_without("aaaaaaaaa ddd gggggg" ,  "g") )         # 9
print("lww5:",longest_word_without("aaag dddg eeeg" ,  "g") )               # 0


# T5 ----
# In digital health, patients / study participants need to be anonymized.
# One way to keep track of individuals is with a heximal ID, e.g. '9f34c2'.
# hexadecimal symbols include the symbols 0123456789abcdef.
# 'hexID_generator' should randomly generate such a string.
# If a seed is given, it should be used to make it reproducible.
# Use the random module for this task.
# Hint: Remember the character string join method
# Hint: random has a function to choose a random element from a non-empty sequence.
#       It can select directly from a string as those are iterables in Python.
# Note: there may be alternate seed solutions that the test script doesn't accept.
#       Please post in the forum if this happens.

import random
def hexID_generator(seed=0):
    0

print("hg1:",hexID_generator()) # some random variant
print("hg2:",hexID_generator(77)) # 8a6763
print("hg3:",hexID_generator(77)) # 8a6763 (always the same)

# Now continue in script3.py

score.score() # for local IDE
