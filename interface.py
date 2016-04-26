## User Interface

def analysis_choose():
    while True:
        analysis_choice = input("What do you want to analyze? Choose from Airline only, Sentiment only, Negative reason only, Interaction, Time only and Time interaction. \n")
        choice = ["Airline only", "Sentiment only", "Negative reason only", "Interaction", "Time only", "Time interaction"]
        if analysis_choice not in choice:
            print("Invalid input. Please try again. ")
        else:
            break
    return analysis_choice
    

def analysis_var_choose():
    
    while True:
        airline_analysis = input("What airlines do you want to analyze? Choose from American, Delta, Southwest, US Airways, United, Virgin America and ALL \n")
        airline_choice = ["American", "Delta", "Southwest", "US Airways", "United", "Virgin America", "ALL"]
        if airline_analysis not in airline_choice:
            print("Invalid input. Please try again. ")
        else:
            break
        
    while True:    
        sentiment_analysis = input("Do you want to analyze sentiment? Choose from Yes or No \n")
        if sentiment_analysis != "Yes" and sentiment_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
    
    while True:        
        neg_reason_analysis = input("Do you want to analyze negative reasons? Choose from Yes or No \n")
        if neg_reason_analysis != "Yes" and neg_reason_analysis != "No":
            print("Invalid input. Please try again. ")
        else:
            break
        
    return airline_analysis, sentiment_analysis, neg_reason_analysis
        
