import score # for local IDE
# Tasks 1-6 are tasks 5-10 from exercise 3.1 Loops.
# Now solve them using dict/list comprehension.

# T1 ----
# 31T5: Compute the sum of all integers 1 till 10.
sum110 = 0
print("s110:",sum110)


# T2 ----
# 31T6: Write a function 'random_is1' with the parameters a and n.
# In n experiments, draw an integer between 1 and a (both included).
# How often is that number equal to 1?
# Hint: range, random.randint
def random_is1(a,n):return 0
print("ri1:",random_is1(4, 200)) # should be approximately 50
print("ri2:",random_is1(4, 200)) #    often between 40 and 60
print("ri3:",random_is1(4, 200)) #    almost never outside 30...70
print("ri4:",random_is1(13, 10000)) # ca 770

# Run the simulation 3k times and plot histogram:
# Only available locally after installing matplotlib
# That module is not available in the browser
import os
if os.getenv("CODEOCEAN")!="true":
    import matplotlib.pyplot as plt
    sims = [random_is1(5, 100) for _ in range(3000)]
    plt.hist(sims, bins=35)
    plt.show()
    # plt.clf() # clear figure to not have a second run added to the previous graph


# T3 ----
# 31T7: The function 'select_cities' should as parameters take
# - a list of city names
# - a letter
# - a number.
# It should return (as a list) all names that 
# begin with the letter and have maximally n characters.
# Note that the letter may be lower or upper case.
def select_cities(cities,letter,n):
    return 0
names = ['London', 'Berlin', 'Hamburg', 'Bonn', 'Budapest', 'Rom', 'Paris', 
         'Munchen', 'New York', 'Bremen', 'Madrid', 'Beijing']
print("sc:", select_cities(names, "b", 6)) # ['Berlin', 'Bonn', 'Bremen']


# Now continue in script2.py

score.score() # for local IDE
