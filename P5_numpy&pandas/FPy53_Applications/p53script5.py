import score # for local IDE
import pandas as pd
# T13 ----
# sumdict should take a dataframe as input and return a dictionary
# with the sums of the column `value` grouped by `category`.
def sumdict(df): # feel free to rename the parameter
    return 0

exdf = pd.DataFrame()
exdf["value"] = pd.to_numeric(list("896388720514464300483"))
exdf['category'] = list("KFFHFKFHFHFKHKHHFKHHF")
print("exdf:", exdf, sep="\n")
print("sumdict(exdf):", sumdict(exdf), sep="\n") # {'F': 34, 'H': 33, 'K': 26}


# T14 ----
trdf = pd.DataFrame()
trdf['category'] = list("TTRTTRRRTRRRTTRRRR")
trdf["value"]    = list("112213232213322131")
print("trdf:", trdf, sep="\n")
# Count the number of occurences per category-value combination.
# The solution check is strict here to enforce the elegant solution.
print(0) # replace 0 with the solution code.
# The printout should look like this:
# category  value
# R         2        4
#           3        4
#           1        3
# T         1        3
#           2        3
#           3        1

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
