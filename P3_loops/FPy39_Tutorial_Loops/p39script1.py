import score # for local IDE
# T1 ----
# Write a function that loops through a list and prints out all even numbers.
# It should not print any numbers that come after 237 in the sequence.
# We don't care if the number is > 237, only if it is in a later position in the list.

def print_even_vals(vals): # feel free to rename the parameter
    0

numbers = [951,402,984,651,360,69,408,319,601]
print_even_vals(numbers) # 402, 984, 360, 408 (each on its own line)
numbers = [951,402,984,651,360,69,237,408,319,601]
print_even_vals(numbers) # 402, 984, 360    (408 no longer there)

# T2 ----
# Write a function with a loop to repeatedly print 'n' as long as it is positive, 
# then decrease it by 5, but if 'n' is exactly 42, the loop should stop running.
# Both n and 42 should be printed. Only use a single call to print().

def print_decreasing_vals(n):
    0

print_decreasing_vals(n=52) # 52,47,42 (each on its own line)
print_decreasing_vals(n=51) # 51,46,41,36,31,26,21,16,11,6,1 (ditto)

# Now continue in script2.py

score.score() # for local IDE
