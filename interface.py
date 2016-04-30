### User Interface

## Choose file
def file_choose():
    while True:    
        file_choice = input("Which file would like to open?\n 1 - airlines.txt\n 2 - gop.txt\n 3 - your own file\n")
        if file_choice != "1" and file_choice != "2" and file_choice != "3":
            print("Invalid input. Please try again. ")
        else:
            break
    return file_choice

## Choose analysis
def analysis_choose_airline():
    while True:
        analysis_choice = input("What do you want to analyze?\n 1 - Airline only\n 2 - Sentiment only\n 3 - Negative reason only\n 4 - Interaction of 1-3\n 5 - Time only\n 6 - Time interaction with 1/2/3\n 7 - Tweets only\n 8 - Tweets interaction with 1/2/3\n")
        choice = ["Airline only", "Sentiment only", "Negative reason only", "Interaction", "Time only", "Time interaction", "Tweets only", "Tweets interaction"]
        choice1 = [1,2,3,4,5,6,7,8]
        if analysis_choice not in choice and int(analysis_choice) not in choice1:
            print("Invalid input. Please try again. ")
        else:
            break
    return analysis_choice

def analysis_choose_gop():
    while True:
        analysis_choice = input("What do you want to analyze?\n 1 - Candidate only\n 2 - Sentiment only\n 3 - Subject matter only\n 4 - Interaction of 1-3\n 5 - Retweet count interaction with 1/2/3\n 6 - Tweets only\n 7 - Tweets interaction with 1/2/3\n")
        choice = [1,2,3,4,5,6,7]
        if int(analysis_choice) not in choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return analysis_choice   
    
def analysis_choose_user():
    while True:
        analysis_choice = input("What do you want to analyze?\n 1 - Variable1 only\n 2 - Variable2 only\n 3 - Variable3 only\n 4 - Interaction of 1-3\n 5 - Variable4 only\n 6 - Variable4 interaction with 1/2/3\n 7 - Variable5 only\n 8 - Variable5 interaction with 1/2/3\n 9 - Variable6 interaction with 1/2/3\n")
        choice = [1,2,3,4,5,6,7,8,9]
        if int(analysis_choice) not in choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return analysis_choice  

## Choose interaction variable
def inter_choose_airline():
    while True:
        inter_analysis = input("What variable would you like to use for interaction analysis?\n 1 - Sentiment\n 2 - Negative Reason\n 3 - Airline\n")
        inter_choice = [1,2,3]
        if int(inter_analysis) not in inter_choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return inter_analysis
    
def inter_choose_gop():
    while True:
        inter_analysis = input("What variable would you like to use for interaction analysis?\n 1 - Sentiment\n 2 - Subject Matter\n 3 - Candidate\n")
        inter_choice = [1,2,3]
        if int(inter_analysis) not in inter_choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return inter_analysis
    
def inter_choose_user():
    while True:
        inter_analysis = input("What variable would you like to use for interaction analysis?\n 1 - Var1 \n 2 - Var2\n 3 - Var3\n")
        inter_choice = [1,2,3]
        if int(inter_analysis) not in inter_choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return inter_analysis
    
    

def analysis_var_choose_airline():
    while True:
        airline_analysis = input("What airline do you want to analyze? Choose from American, Delta, Southwest, US Airways, United, Virgin America and ALL \n")
        airline_choice = ["American", "Delta", "Southwest", "US Airways", "United", "Virgin America", "ALL"]
        if airline_analysis not in airline_choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return airline_analysis
    
def analysis_var_choose_gop():
    while True:
        candidate_analysis = input("What candidate do you want to analyze? Choose from Ben Carson, Chris Christie, Donald Trump, Jeb Bush, John Kasich, Marco Rubio, Mike Huckabee, Rand Paul, Scott Walker, Ted Cruz, No candidate mentioned or ALL \n")
        candidate_choice = ['Ben Carson', 'Chris Christie', 'Donald Trump', 'Jeb Bush', 'John Kasich', 'Marco Rubio', 'Mike Huckabee', 'Rand Paul', 'Scott Walker', 'Ted Cruz', 'No candidate mentioned', 'ALL']
        if candidate_analysis not in candidate_choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return candidate_analysis 
    
def analysis_var_choose_user():
    var1_analysis = input("What item do you want to analyze among all the items of Variable1?  \n")
    return var1_analysis 
    
    
    
def sentiment_include():      
    while True:    
        sentiment_analysis = input("Do you want to analyze sentiment? Choose from Yes or No \n")
        if sentiment_analysis != "Yes" and sentiment_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    return sentiment_analysis

def neg_reason_include():  
    while True:        
        neg_reason_analysis = input("Do you want to analyze negative reasons? Choose from Yes or No \n")
        if neg_reason_analysis != "Yes" and neg_reason_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    return neg_reason_analysis

def sub_matter_include():  
    while True:        
        sub_matter_analysis = input("Do you want to analyze subject matters? Choose from Yes or No \n")
        if sub_matter_analysis != "Yes" and sub_matter_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    return sub_matter_analysis        

def var2_include():      
    while True:    
        var_analysis = input("Do you want to analyze Varaible2? Choose from Yes or No \n")
        if var_analysis != "Yes" and var_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    return var_analysis

def var3_include():      
    while True:    
        var_analysis = input("Do you want to analyze Varaible3? Choose from Yes or No \n")
        if var_analysis != "Yes" and var_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    return var_analysis


def tweet_choose():
    while True:
        tweet_analysis = input("Would you like to use only functional words in tweets? Choose from Yes or No \n")
        if tweet_analysis != "Yes" and tweet_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    return tweet_analysis
    
