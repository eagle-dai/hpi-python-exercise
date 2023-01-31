import score # for local IDE
import numpy as np
import pandas as pd
# A 'dataframe' in this exercise refers to a pandas DataFrame.

# T1 ----
# Convert the provided disease dictionary to a dataframe called `illness`.
dict_illness = {'disease':["malaria", "coronary artery disease", "alzheimers", 
                           "stroke", "diabetes", "tuberculosis"], 
                'cases':[21, 79, 267, 384, 225, 162]}
illness = 0
print("i:", illness, sep="\n")


# T2 ----
# Extract the number of row and columns as a tuple. Use the appropriate pandas df property.
nrc = 0
print("nrc:", nrc, sep="\n")


# T3 ----
# Select the third to fifth rows from it (the ones with alzheimers, stroke, diabetes).
# They are NOT obtained with 3:5 as most people would intuitively use. 
illness_subset = 0
print("isub:", illness_subset, sep="\n")


# T4 ----
# Select all the rows where the disease name has less than or equal to 10 letters.
illness_short = 0
print("ishort:", illness_short, sep="\n")


# T5 ----
# Write a function that, for a given dataframe, computes the maximum
# of the values in the column 'n_patients', excluding the last 3 rows.
def max_patients(df): # feel free to rename the parameter
    return 0

hopa = pd.DataFrame({'hospital':range(7,16), 
                     'n_patients':[675,899,682,396,517,620,205,633,946]})
print("mp:", max_patients(hopa)) # should be 899 (not 946)

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
