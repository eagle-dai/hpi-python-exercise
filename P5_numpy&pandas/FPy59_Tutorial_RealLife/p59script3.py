import score # for local IDE
import pandas as pd
# T7 ----
# Read the provided hospitalbeds dataset. 
# Note: the first lines contain metadata.
hosp = 0
print("hosp:", hosp, sep="\n") # should begin with:
#    country  year  beds
#0       AUT  2017  7.37
#1       AUT  2018  7.27


# T8 ----
# Compute the maximum hospital capacity (beds) per country.
# Sort the aggregated data by beds in decreasing order.
maxbeds = 0
# print("maxbeds:", maxbeds.head(6), sep="\n") # should be:
#         year   beds
#country             
#JPN      2019  13.05
#KOR      2019  12.44
#RUS      2019   8.06
#DEU      2019   8.00
#AUT      2019   7.37
#HUN      2020   7.02

score.score() # for local IDE

# If you want to see your score on openHPI, click Submit after scoring.
# score.score(submit=True) # for local IDE
