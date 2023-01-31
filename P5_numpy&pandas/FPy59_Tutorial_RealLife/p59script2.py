import score # for local IDE
import pandas as pd
# The following tasks refer to pandas DataFrame objects.
# T4 ----
# 'numcols' should select all the columns with float64 type.
# Note: filtering on columns with df[cond] only works if cond has the same index as df.
# Hint: df.loc[rows, columns] handles 2 dimensions, not just df.loc[row]
def numcols(x):
    return 0
print("numcols:", numcols(pd.DataFrame({'A':[3,9],'B':[2.7,5.4],'C':[4.2,5]})), sep="\n")
# Should be:
#     B    C
#0  2.7  4.2
#1  5.4  5.0


# T5 ----
# 'na2median' should replace NAs with the median in the respective column.
def na2median(x):
    return 0
print("na2median:", na2median(pd.DataFrame({'A':[7,9,None],'B':[2,None,1]})), sep="\n")
# Should be:
#     A    B
#0  7.0  2.0
#1  9.0  1.5
#2  8.0  1.0


# T6 ----
# 'omitna' should remove rows with less than 2 known values.
def omitna(x):
    return 0
exdf = pd.DataFrame({'A':[7,9,3,None],'B':[2,1,None,None], 'C':[5,None,None,None], 'D':[None]*4})
print("exdf:", exdf, sep="\n")
print("omitna:", omitna(exdf), sep="\n")
# Should be:
#     A    B    C     D
#0  7.0  2.0  5.0  None
#1  9.0  1.0  NaN  None

# Now continue in script3.py

score.score() # for local IDE
