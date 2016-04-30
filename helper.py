## 

def help():
    question_choice = input("What is your question?\n 1 - Files information\n 2 - Functions information (what this program can do)\n")
    if question_choice == "1":
        file_choice = input("Which file do you have question with?\n 1 - airlines.txt\n 2 - gop.txt\n")
        if file_choice == "1":
            print("This data originally came from Crowdflower's Data for Everyone library.\n"
            "A sentiment analysis job about the problems of each major U.S. airline. Twitter data was scraped from February of 2015 and \n"
            "contributors were asked to first classify positive, negative, and neutral tweets, followed by categorizing negative reasons \n"
            "such as 'late flight' or 'rude service'.\n"
            "The fields in the Tweets.csv file / Tweets database table are:\n"
            "sentiment, negativereason, airline, text(tweets), tweet_created(date and time), tweet_location, user_timezone\n")
        elif file_choice == "2":
            print("This data originally came from Crowdflower's Data for Everyone library.\n"
            "They looked through tens of thousands of tweets about the early August GOP debate in Ohio and asked contributors to do both \n"
            "sentiment analysis and data categorization. Contributors were asked if the tweet was relevant, which candidate was mentioned, \n"
            "what subject was mentioned, and then what the sentiment was for a given tweet. The variables included are similar as in file 1.\n")
            redirect = input("If you want to see variables information mentioned in file1 information help, please enter 1.")
            if redirect == "1":
                file_choice = input("Which file do you have question with?\n 1 - airlines.txt\n 2 - gop.txt\n")
    elif question_choice == "2":
        function_choice = input("Which file do you have question with?\n 1 - airlines.txt\n 2 - gop.txt\n")
        if function_choice == "1":
            print("Functions for airline, sentiment and negative reason analysis are to summarize count of tweets in each category,\n"
            "such as for airline, the function summarizes count of tweets of each airline company.\n"
            "Functions for two or more variables interaction analysis are to summarize count of tweets under two or more categories.\n"
            "Function for tweet analysis is to summarize the 10 most frequently used words in tweets.\n")
        if function_choice == "2":
            print("Functions for candidate, sentiment and negative reason analysis are to summarize count of tweets in each category,\n"
            "such as for airline, the function summarizes count of tweets of each airline company.\n"
            "Functions for two or more variables interaction analysis are to summarize count of tweets under two or more categories.\n"
            "Function for tweet analysis is to summarize the 10 most frequently used words in tweets.\n"
            "Function for retweet analysis is to summarize the count of retweets under specific category.\n")
    evaluation = input("Thank you for using the helper. Do you think it is useful?\n 1 - Yes\n 2 - No\n")
    return evaluation
    
        