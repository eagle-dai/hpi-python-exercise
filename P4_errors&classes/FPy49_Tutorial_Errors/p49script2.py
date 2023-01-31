import score # for local IDE
# T4 ----
# Write the equivalent of R's   sort(table(a_vector))  in Python.
# Note: early slides already covered this particular example.
# Note: Obviously, you can also search online for e.g. "Python count and sort".
# Let me know if the test script is too strict and should accept your solution.
def sorted_table(x):
    return 0
print("st1:", sorted_table(["E","K","A","E","K","E"])) # [('E', 3), ('K', 2), ('A', 1)]


# T5 ----
# If the input list is empty, a custom ValueError should be generated that says:
# "The input list may not be empty."
# Adapt the function above or make a copy with the same name - whatever you prefer.
try:
    sorted_table([])
    print("st2: this should generate an error.")
except Exception as e:
    print(f"st2: {type(e).__name__}: {e} - intentionally generated.")
    # ValueError: The input list may not be empty.


# Now continue in script3.py

score.score() # for local IDE
