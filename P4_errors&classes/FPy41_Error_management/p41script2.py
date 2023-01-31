import score # for local IDE
# T4 ----
# Adapt 'main_code' so that:
# - if run_analysis(x) fails with a NameError, it returns the string 
"Load the analysis functions first."
# - other errors are raised regularly (see examples), simulating unexpected errors
# - in any case, the 'cleaning up' thing is printed, simulating an actual cleanup process.
def main_code(x):
    result = run_analysis(x)
    print("Cleaning up after analysis was done.")
    return result


        
if False: # set to true once task is solved.
    print("mc1:",main_code(77)) # should print/return both of the following:
# Cleaning up after analysis was done.
# mc1: Load the analysis functions first.

def run_analysis(y):
    return y + 42 # in real life, this would be something real

print("mc2:",main_code(77)) # Cleaning up after analysis was done.  +  mc2: 119

if False: # keep False for scoring so script is runnable
    main_code("44") # should do two things:
# raise TypeError: can only concatenate str (not "int") to str
# but still print "Cleaning up after analysis was done."


score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
