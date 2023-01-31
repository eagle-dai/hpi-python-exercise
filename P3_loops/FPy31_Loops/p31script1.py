import score # for local IDE
# T1 ----
# Write a function to loop over the input, printing each element on its own line.
# Terminate the loop if it encounters "b5".
def print_loop1(i):0
ids = ["a1", "b1", "b4", "b5", "b6", "c1"]
print_loop1(ids) # a1  \n  b1  \n  b4 (each on a separate line)


# T2 ----
# Same as in T1, but now don’t terminate the entire loop, 
# just skip that particular iteration.
def print_loop2(i):0
print_loop2(ids) # a1  \n  b1  \n  b4  \n  b6  \n  c1


# T3 ----
# The function 'dosage' should accept an amount as input and in a while loop,
# if the amount is larger than 15, print("another application is possible"),
# decrement (reduce) the amount by 15 and at the end print("the vial is empty")
def dosage(amount):0
dosage(56) # another application is possible (3x), the vial is empty


# T4 ----
# Write a function that prints each element of the input list on its own print line.
# It should also remove all elements from the list.
# Remember there is a function to both remove and return an element from a list.
# Try both a for and a while loop (the latter is more elegant here).
def print_and_remove(x):0
my_list = [3, "things", "here"]
print_and_remove(my_list) # printed: 3  \n  things  \n  here
print("par:", my_list) # is now empty []


# Now continue in script2.py

score.score() # for local IDE
