#!/usr/bin/python3

import re
from functions import *
from interface import *

filename = "airlines_concise.csv"
filename1 = "airlines.txt"
with open(filename1) as f:
    lines = f.readlines()

lines_list = []
for line in lines:
    lines_list.append(line.split("\t"))
# print(lines_list[0])
# print(lines_list[1])

sentiment_index = 0
neg_reason_index = 2
airline_index = 4
tweets_index = 5
time_index = 6

index = sentiment_index # or airline_index or neg_reason_index
# analysis_var_choose()
airline_analysis = "American"
sentiment_analysis = True
neg_reason_analysis = False

# analysis_choose()
analysis_choice = "Time only"
if analysis_choice == "Airline only":
    airlines_fcn(airline_index, lines_list)
elif analysis_choice == "Sentiment only":
    sentiment_fcn(sentiment_index, lines_list)
elif analysis_choice == "Negative reason only":
    neg_reason_fcn(neg_reason_index, lines_list)
elif analysis_choice == "Interaction":
    interaction_fcn(airline_index, sentiment_index, neg_reason_index, airline_analysis, sentiment_analysis, neg_reason_analysis, lines_list)
elif analysis_choice== "Time only":
    day_fcn(time_index,lines_list)
elif analysis_choice== "Time interaction":
    time_inter_fcn(index, time_index, lines_list)






        