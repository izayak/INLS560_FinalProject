#!/usr/bin/python3

import re
from functions import *
from interface import *
from helper import *

print("Welcome to this little data analysis program. Hope you will enjoy. Input anything to start. If you need help, input 1 :) ")
inp = input()
if inp == "1":
    useful = help()

## Evaluate the help function
total = 0
use = 0
if useful == "1":
    use += 1
    total += 1
elif useful == "2":
    total+= 1



### Main Part

while True:
    ### Choose file
    file_choice = file_choose()
    if file_choice == "1":
        filename = "airlines.txt"
        sentiment_index = 0
        neg_reason_index = 2
        airline_index = 4
        tweet_index = 5
        time_index = 6
    elif file_choice == "2": 
        filename = "gop.txt"
        candidate_index = 0
        sentiment_index = 2
        sub_matter_index = 4
        retweet_index = 5
        tweet_index = 6
    elif file_choice == "3":
        filename = input("What is the name of the file? Be sure to include the extension name of the file.\n")
        print("Next please input the index of variables. The first 3 variables should be variables that are suitable for analyzed by themselves or with each other,")
        print("varaible 4 should be variable that is suitable for analyzed by itself or with variable 1-3, variable 5 should be tweet-like variable, variable 6 should be count-like varaible. ")
        index1 = input("Please input the index of the first variable that you are interested.\n") - 1
        index2 = input("Please input the index of the second varaible.\n") - 1
        index3 = input("Please input the index of the third variable.\n") - 1
        index4 = input("Please input hte index of the fourth varaible.\n") - 1
        index5 = input("Please input hte index of the fifth varaible.\n") - 1
        index6 = input("Please input hte index of the sixth varaible.\n") - 1
        
        
    ### Open file    
    with open(filename) as f:
        lines = f.readlines()
    
    lines_list = []
    for line in lines:
        lines_list.append(line.split("\t"))
    # print(lines_list[0])
    # for line in lines_list:
    #     print(line[1])
        
    
    if file_choice == "1":
        ## Choose from different analysis
        analysis_choice = analysis_choose_airline()
        
        ## Choose interaction variable for choice 6 or 8
        if analysis_choice == '6' or analysis_choice == '8':
            inter_analysis_airline = inter_choose_airline()
            if int(inter_analysis_airline) == 1: 
                index = sentiment_index
            elif int(inter_analysis_airline) == 2:
                index = neg_reason_index
            elif int(inter_analysis_airline) == 3:
                index = airline_index
        
        ## Choose interaction variable for choice 4
        if analysis_choice == "4":
            airline_analysis = analysis_var_choose_airline()
            sentiment_analysis = sentiment_include()
            neg_reason_analysis = neg_reason_include()
        
        ## Choose to include unfunctional words in tweets analysis or not
        if analysis_choice == '7':
            tweet_analysis = tweet_choose()
    
    elif file_choice == "2":
        analysis_choice = analysis_choose_gop()
        
        if analysis_choice == '5' or analysis_choice == '7':
            inter_analysis_gop = inter_choose_gop()
            if int(inter_analysis_gop) == 1: 
                index = sentiment_index
            elif int(inter_analysis_gop) == 2:
                index = sub_matter_index
            elif int(inter_analysis_gop) == 3:
                index = candidate_index
            
        if analysis_choice == '4':
            airline_analysis = analysis_var_choose_gop()
            sentiment_analysis = sentiment_include()
            neg_reason_analysis = sub_matter_include()
        
        if analysis_choice == '6':
            tweet_analysis = tweet_choose()
    
    elif file_choice == "3":
        analysis_choice = analysis_choose_user()
        
        if analysis_choice == '6' or analysis_choice == '8' or analysis_choice == '9':
            inter_analysis_user = inter_choose_user()
            if int(inter_analysis_user) == 1: 
                index = index1
            elif int(inter_analysis_user) == 2:
                index = index2
            elif int(inter_analysis_user) == 3:
                index = index3
            
        if analysis_choice == '4':
            var1_analysis = analysis_var_choose_user()
            var2_analysis = var2_include()
            var3_analysis = var3_include()
        
        if analysis_choice == '7':
            tweet_analysis = tweet_choose()
            
            
            
    if file_choice == "1":
        if analysis_choice == "Airline only" or analysis_choice == '1':
            airlines_fcn(airline_index, lines_list)
        elif analysis_choice == "Sentiment only" or analysis_choice == '2':
            sentiment_fcn(sentiment_index, lines_list)
        elif analysis_choice == "Negative reason only" or analysis_choice == '3':
            neg_reason_fcn(neg_reason_index, lines_list)
        elif analysis_choice == "Interaction" or analysis_choice == '4':
            interaction_fcn(airline_index, sentiment_index, neg_reason_index, airline_analysis, sentiment_analysis, neg_reason_analysis, lines_list, file_choice)
        elif analysis_choice== "Time only" or analysis_choice == '5':
            day_fcn(time_index, lines_list)
        elif analysis_choice == "Time interaction" or analysis_choice == '6':
            time_inter_fcn(index, time_index, lines_list)
        elif analysis_choice == "Tweets only" or analysis_choice == '7':
            tweet_fcn(tweet_index, lines_list, tweet_analysis, file_choice)
        elif analysis_choice == "Tweets interaction" or analysis_choice == '8':
            tweet_inter_fcn(index, tweet_index, lines_list, file_choice)
    elif file_choice == "2":
        if analysis_choice == '1':
            airlines_fcn(candidate_index, lines_list)
        elif analysis_choice == '2':
            sentiment_fcn(sentiment_index, lines_list)
        elif analysis_choice == '3':
            neg_reason_fcn(sub_matter_index, lines_list)
        elif analysis_choice == '4':
            interaction_fcn(candidate_index, sentiment_index, sub_matter_index, airline_analysis, sentiment_analysis, neg_reason_analysis, lines_list, file_choice)
        elif analysis_choice == '5':
            retweet_inter_fcn(index, retweet_index, lines_list)
        elif analysis_choice == '6':
            tweet_fcn(tweet_index, lines_list, tweet_analysis, file_choice)
        elif analysis_choice == '7':
            tweet_inter_fcn(index, tweet_index, lines_list, file_choice)
    elif file_choice == "3":
        if analysis_choice == '1':
            airlines_fcn(index1, lines_list)
        elif analysis_choice == '2':
            sentiment_fcn(index2, lines_list)
        elif analysis_choice == '3':
            neg_reason_fcn(index3, lines_list)
        elif analysis_choice == '4':
            interaction_fcn(index1, index2, index3, var1_analysis, var2_analysis, var3_analysis, lines_list, file_choice)
        elif analysis_choice == '5':
            day_fcn(index4, lines_list)
        elif analysis_choice == '6':
            time_inter_fcn(index, index4, lines_list)
        elif analysis_choice == '7':
            tweet_fcn(index5, lines_list, tweet_analysis, file_choice)
        elif analysis_choice == '8':
            tweet_inter_fcn(index, index5, lines_list, file_choice)
        elif analysis_choice == '9':
            retweet_inter_fcn(index, index6, lines_list)
    
    while True:
        quit = input("Do you want to exit?\n 1 - Yes 2 - No, I would like to continue\n")
        if quit != "1" and quit != "2":
            print("Invalid input. Please try again.")
        else: 
            break
    if quit == "1":
        break
    


        