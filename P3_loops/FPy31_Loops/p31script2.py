import score # for local IDE
# I suggest you use actual loops here.
# Exercise 3.2 Comprehension will have all suitable tasks again with the idea of
# using list comprehension then.
# If you already know that concept, feel free to use it here (and copy to ex 3.2)

# T5 ----
# Using a for loop, compute the sum of all integers 1 till 10.
sum110 = 0
print("s110:",sum110)


# T6 ----
# Write a function 'random_is1' with the parameters a and n.
# In n experiments, draw an integer between 1 and a (both included).
# How often is that number equal to 1?
# Hint: range, random.randint
def random_is1(a,n):0
print("ri1:",random_is1(4, 200)) # should be approximately 50
print("ri2:",random_is1(4, 200)) #    often between 40 and 60
print("ri3:",random_is1(4, 200)) #    almost never outside 30...70
print("ri4:",random_is1(13, 10000)) # ca 770
# In excercise 3.2 Comprehension, we'll run some simulations with this :)


# T7 ----
# The function 'select_cities' should as parameters take
# - a list of city names
# - a letter
# - a number.
# It should return (as a list) all names that 
# begin with the letter and have maximally n characters.
# Note that the letter may be lower or upper case.
def select_cities(cities,letter,n):0
names = ['London', 'Berlin', 'Hamburg', 'Bonn', 'Budapest', 'Rom', 'Paris', 
         'Munchen', 'New York', 'Bremen', 'Madrid', 'Beijing']
print("sc:", select_cities(names, "b", 6)) # ['Berlin', 'Bonn', 'Bremen']


# Now continue in script3.py

score.score() # for local IDE
