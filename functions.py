# stat analysis using separate dictionaries

import re

### Airlines/Candidate Analysis PART

def airlines_fcn(airline_index, lines_list):
    airlines_dict = {}
    for line in lines_list[1:]:
        airline = line[airline_index]
        if airline not in airlines_dict:
            airlines_dict[airline] = 1
        else:
            airlines_dict[airline] += 1
    
    airlines_list = list(airlines_dict.keys())
    airlines_list.sort()
    
    print_length = 0
    for item in airlines_dict:
        if len(item) > print_length:
            print_length = len(item)
    
    # Frequency Table
    for item in airlines_list:
        if len(item) > 0:
            print(item, " "*(print_length-len(item)), airlines_dict[item])
    print("\n")
    
    # Histogram
    airlines_count_sum = sum(airlines_dict.values())
    for item in airlines_list:
        if len(item) > 0:
            star = round(airlines_dict[item]/airlines_count_sum*200,2)
            prop = round(airlines_dict[item]/airlines_count_sum*100,2)
            print(item, " "*(print_length-len(item)), "*"*int(star), str(prop)+"%")
    print("\n")



### Sentiment Analysis PART

def sentiment_fcn(sentiment_index, lines_list):
    sentiment_dict = {}
    for line in lines_list[1:]:
        sentiment = line[sentiment_index]
        if sentiment not in sentiment_dict:
            sentiment_dict[sentiment] = 1
        else:
            sentiment_dict[sentiment] += 1
    
    sentiment_list = list(sentiment_dict.keys())
    sentiment_list.sort()
    
    print_length = 0
    for item in sentiment_list:
        if len(item) > print_length:
            print_length = len(item)
    
    # Frequency Table
    for item in sentiment_list:
        print(item, " "*(print_length-len(item)), sentiment_dict[item])
    print("\n")
    
    # Histogram
    sentiment_count_sum = sum(sentiment_dict.values())
    for item in sentiment_list:
        star = round(sentiment_dict[item]/sentiment_count_sum*50,2)
        prop = round(sentiment_dict[item]/sentiment_count_sum*100,2)
        print(item, " "*(print_length-len(item)), "*"*int(star), str(prop)+"%")
    print("\n")



### Negative Reason/Subject Matter Analysis PART

def neg_reason_fcn(neg_reason_index, lines_list):
    
    neg_reason_dict = {}
    for line in lines_list[1:]:
        neg_reason = line[neg_reason_index]
        if neg_reason not in neg_reason_dict:
            neg_reason_dict[neg_reason] = 1
        else:
            neg_reason_dict[neg_reason] += 1
       
    neg_reason_list = list(neg_reason_dict.keys())
    i = 0
    for item in neg_reason_list:
        if len(item) == 0:
            neg_reason_list[i] = 'Not Stated'
        if item == "longlines":
            neg_reason_list[i] = 'Longlines'
        i += 1
    neg_reason_list.sort()
    
    
    print_length = 0
    for item in neg_reason_dict:
        if len(item) > print_length:
            print_length = len(item)
    
    # Frequency Table
    for item in neg_reason_list:
        if item == "Not Stated":
            print(item, " "*(print_length-len("Not Stated")), neg_reason_dict[""])
        elif item == "Longlines":
            print(item, " "*(print_length-len("Longlines")), neg_reason_dict["longlines"])
        else:
            print(item, " "*(print_length-len(item)), neg_reason_dict[item])
    print("\n")
    
    # Histogram
    neg_reason_count_sum = sum(neg_reason_dict.values())
    for item in neg_reason_list:
        if item == "Not Stated":
            star = round(neg_reason_dict[""]/neg_reason_count_sum*200,2)
            prop = round(neg_reason_dict[""]/neg_reason_count_sum*100,2)
            print(item, " "*(print_length-len("Not Stated")), "*"*int(star), str(prop)+"%")
        elif item == "Longlines":
            star = round(neg_reason_dict["longlines"]/neg_reason_count_sum*200,2)
            prop = round(neg_reason_dict["longlines"]/neg_reason_count_sum*100,2)
            print(item, " "*(print_length-len("Longlines")), "*"*int(star), str(prop)+"%")
        else:
            star = round(neg_reason_dict[item]/neg_reason_count_sum*200,2)
            prop = round(neg_reason_dict[item]/neg_reason_count_sum*100,2)
            print(item, " "*(print_length-len(item)), "*"*int(star), str(prop)+"%")
 
            
### Interaction PART
def interaction_fcn(airline_index, sentiment_index, neg_reason_index, airline_analysis, sentiment_analysis, neg_reason_analysis, lines_list, file_choice):
    records_dict = {}
    for line in lines_list[1:]:
        # print(line[5])
        # tweets_list.append(line[tweets_index])
        sentiment = line[sentiment_index]
        airline = line[airline_index]
        neg_reason = line[neg_reason_index]
        
        if airline not in records_dict:
            records_dict[airline] = { "sentiment":{}, "neg_reason":{} }
            if sentiment not in records_dict[airline]["sentiment"]:
                records_dict[airline]["sentiment"][sentiment] = 1
            else:
                records_dict[airline]["sentiment"][sentiment] += 1
            if neg_reason not in records_dict[airline]["neg_reason"]:
                records_dict[airline]["neg_reason"][neg_reason] = 1
            elif neg_reason != " ":
                records_dict[airline]["neg_reason"][neg_reason] += 1
        else:
            if sentiment not in records_dict[airline]["sentiment"]:
                records_dict[airline]["sentiment"][sentiment] = 1
            else:
                records_dict[airline]["sentiment"][sentiment] += 1
            if neg_reason not in records_dict[airline]["neg_reason"]:
                records_dict[airline]["neg_reason"][neg_reason] = 1
            elif neg_reason != " ":
                records_dict[airline]["neg_reason"][neg_reason] += 1
    # print(records_dict)
    
    records_list = list(records_dict.keys())
    records_list.sort()
    
    sentiment_print_length = 0
    for item in records_dict[airline]["sentiment"]:
        if len(item) > sentiment_print_length:
            sentiment_print_length = len(item)
    neg_reason_print_length = 0
    for item in records_dict[airline]["neg_reason"]:
        if len(item) > neg_reason_print_length:
            neg_reason_print_length = len(item) 
    neg_reason_print_length += 2 
    
    # Contingency Table        
    if airline_analysis == "ALL":
        for airline in records_list:
            print(airline)
            
            ## Sentiment
            if sentiment_analysis == "Yes":
                print("   Sentiment")
                
                sentiment_dict = {}
                for line in lines_list[1:]:
                    if line[airline_index] == airline:
                        sentiment = line[sentiment_index]
                        if sentiment not in sentiment_dict:
                            sentiment_dict[sentiment] = 1
                        else:
                            sentiment_dict[sentiment] += 1
                
                sentiment_list = list(sentiment_dict.keys())
                sentiment_list.sort()
                        
                sentiment_count_sum = sum(sentiment_dict.values())            
                for item in sentiment_list:
                    prop = round(sentiment_dict[item]/sentiment_count_sum*100,2)
                    print("\t", '\t'.join([item, str(sentiment_dict[item]), str(prop)+"%"]))
            
            
            ## Negative Reason
            if neg_reason_analysis == "Yes":
                if file_choice == "1":
                    print("   Negative Reason")
                elif file_choice == "2":
                    print("   Subject Matter")
                else:
                    print("   Variable 3")
                    
                neg_reason_dict = {}
                for line in lines_list[1:]:
                    if line[airline_index] == airline:
                        neg_reason = line[neg_reason_index]
                        if neg_reason not in neg_reason_dict:
                            neg_reason_dict[neg_reason] = 1
                        else:
                            neg_reason_dict[neg_reason] += 1
                
                neg_reason_list = list(neg_reason_dict.keys())
                i = 0
                for item in neg_reason_list:
                    if len(item) == 0:
                        neg_reason_list[i] = 'Not Stated'
                    if item == "longlines":
                        neg_reason_list[i] = 'Longlines'
                    i += 1
                neg_reason_list.sort()
                
                neg_reason_count_sum = sum(neg_reason_dict.values())        
                for neg_reason in neg_reason_list:
                    if neg_reason == "Not Stated":
                        prop = round(neg_reason_dict[""]/neg_reason_count_sum*100,2)
                        print("\t", neg_reason, " "*(neg_reason_print_length-len("Not Stated")), neg_reason_dict[""], "\t", str(prop)+"%")
                    elif neg_reason == "Longlines":
                        prop = round(neg_reason_dict["longlines"]/neg_reason_count_sum*100,2)
                        print("\t", neg_reason, " "*(neg_reason_print_length-len(neg_reason)), neg_reason_dict["longlines"], "\t", str(prop)+"%")
                    else:
                        prop = round(neg_reason_dict[neg_reason]/neg_reason_count_sum*100,2)
                        print("\t", neg_reason, " "*(neg_reason_print_length-len(neg_reason)), neg_reason_dict[neg_reason], "\t", str(prop)+"%")
    else:
        print(airline_analysis)
        ## Sentiment
        if sentiment_analysis == "Yes":
            print("   Sentiment")
            
            sentiment_dict = {}
            for line in lines_list[1:]:
                if line[airline_index] == airline_analysis:
                    sentiment = line[sentiment_index]
                    if sentiment not in sentiment_dict:
                        sentiment_dict[sentiment] = 1
                    else:
                        sentiment_dict[sentiment] += 1
            
            sentiment_list = list(sentiment_dict.keys())
            sentiment_list.sort()
            
            sentiment_count_sum = sum(sentiment_dict.values())            
            for item in sentiment_list:
                prop = round(sentiment_dict[item]/sentiment_count_sum*100,2)
                print("\t", '\t'.join([item, str(sentiment_dict[item]), str(prop)+"%"]))
                        
            # for sentiment in sentiment_list:
            #     print("\t", sentiment, " "*(sentiment_print_length-len(sentiment)), records_dict[airline_analysis]["sentiment"][sentiment])
        
        ## Negative Reason
        if neg_reason_analysis == "Yes":
            if file_choice == "1":
                print("   Negative Reason")
            elif file_choice == "2":
                print("   Subject Matter")
            else:
                print("   Variable 3")
            
            neg_reason_dict = {}
            for line in lines_list[1:]:
                if line[airline_index] == airline_analysis:
                    neg_reason = line[neg_reason_index]
                    if neg_reason not in neg_reason_dict:
                        neg_reason_dict[neg_reason] = 1
                    else:
                        neg_reason_dict[neg_reason] += 1
            
            neg_reason_list = list(neg_reason_dict.keys())
            i = 0
            for item in neg_reason_list:
                if len(item) == 0:
                    neg_reason_list[i] = 'Not Stated'
                if item == "longlines":
                    neg_reason_list[i] = 'Longlines'
                i += 1
            neg_reason_list.sort()
            
            neg_reason_count_sum = sum(neg_reason_dict.values())        
            for neg_reason in neg_reason_list:
                if neg_reason == "Not Stated":
                    prop = round(neg_reason_dict[""]/neg_reason_count_sum*100,2)
                    print("\t", neg_reason, " "*(neg_reason_print_length-len("Not Stated")), neg_reason_dict[""], "\t", str(prop)+"%")
                elif neg_reason == "Longlines":
                    prop = round(neg_reason_dict["longlines"]/neg_reason_count_sum*100,2)
                    print("\t", neg_reason, " "*(neg_reason_print_length-len(neg_reason)), neg_reason_dict["longlines"], "\t", str(prop)+"%")
                else:
                    prop = round(neg_reason_dict[neg_reason]/neg_reason_count_sum*100,2)
                    print("\t", neg_reason, " "*(neg_reason_print_length-len(neg_reason)), neg_reason_dict[neg_reason], "\t", str(prop)+"%")
    print("\n")


### Time Analysis PART

def day_fcn(time_index, lines_list):
    day_dict = {}
    for line in lines_list[1:]:
        time = line[time_index]
        day = re.findall('[0-9]/([0-9][0-9])/15', time)
        if day[0] == '18':
            day[0] = 'Wed'
        elif day[0] == '19':
            day[0] = 'Thu'
        elif day[0] == '20':
            day[0] = 'Fri'
        elif day[0] == '21':
            day[0] = 'Sat'
        elif day[0] == '22':
            day[0] = 'Sun'
        elif day[0] == '23':
            day[0] = 'Mon'
        elif day[0] == '24':
            day[0] = 'Tue'
        else:
            continue
        if day[0] not in day_dict:
            day_dict[day[0]] = 1
        else:
            day_dict[day[0]] += 1
    lst = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    
    # Frequency Table
    for item in lst:
        print('\t'.join([str(item), str(day_dict[item])]))
    print("\n")
    
    # Histogram
    day_count_sum = sum(day_dict.values())
    for item in lst:
        star = round(day_dict[item]/day_count_sum*100,2)
        prop = round(day_dict[item]/day_count_sum*100,2)
        print('\t'.join([str(item), "*"*int(star), str(prop)+"%"]))
    print("\n")
    
    

### Time and Sentiment/Negative Reason/Airline Interaction PART

def time_inter_fcn(index, time_index, lines_list):
    records_dict = {}
    day_dict = {}
    for line in lines_list[1:]:
        time = line[time_index]
        day = re.findall('[0-9]/([0-9][0-9])/15', time)
        if day[0] == '18':
            day[0] = 'Wed'
        elif day[0] == '19':
            day[0] = 'Thu'
        elif day[0] == '20':
            day[0] = 'Fri'
        elif day[0] == '21':
            day[0] = 'Sat'
        elif day[0] == '22':
            day[0] = 'Sun'
        elif day[0] == '23':
            day[0] = 'Mon'
        elif day[0] == '24':
            day[0] = 'Tue'
        else:
            continue
        if day[0] not in day_dict:
            day_dict[day[0]] = 1
        else:
            day_dict[day[0]] += 1
        
        
        inter_item = line[index]
        if inter_item not in records_dict:
            records_dict[inter_item] = { "day":{} }
            
            time = line[time_index]
            day = re.findall('[0-9]/([0-9][0-9])/15', time)
            if day[0] == '18':
                day[0] = 'Wed'
            elif day[0] == '19':
                day[0] = 'Thu'
            elif day[0] == '20':
                day[0] = 'Fri'
            elif day[0] == '21':
                day[0] = 'Sat'
            elif day[0] == '22':
                day[0] = 'Sun'
            elif day[0] == '23':
                day[0] = 'Mon'
            elif day[0] == '24':
                day[0] = 'Tue'
            else:
                continue
            
            if day[0] not in records_dict[inter_item]:
                records_dict[inter_item][day[0]] = 1
            else:
                records_dict[inter_item][day[0]] += 1
        else:
            if day[0] not in records_dict[inter_item]:
                records_dict[inter_item][day[0]] = 1
            else:
                records_dict[inter_item][day[0]] += 1
    # print(records_dict)
    
    for inter_item in records_dict:
        print(inter_item)
            
        time_dict = {}
        for line in lines_list[1:]:
            if line[index] == inter_item:
                time = line[time_index]
                day = re.findall('[0-9]/([0-9][0-9])/15', time)
                if day[0] == '18':
                    day[0] = 'Wed'
                elif day[0] == '19':
                    day[0] = 'Thu'
                elif day[0] == '20':
                    day[0] = 'Fri'
                elif day[0] == '21':
                    day[0] = 'Sat'
                elif day[0] == '22':
                    day[0] = 'Sun'
                elif day[0] == '23':
                    day[0] = 'Mon'
                elif day[0] == '24':
                    day[0] = 'Tue'
                else:
                    continue
                
                if day[0] not in time_dict:
                    time_dict[day[0]] = 1
                else:
                    time_dict[day[0]] += 1
        # print(time_dict)
        
        days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        time_count_sum = sum(time_dict.values())            
        for item in days:
            prop = round(time_dict[item]/time_count_sum*100,2)
            print("\t", '\t'.join([item, str(time_dict[item]), str(prop)+"%"]))
            
        
            

### Tweets Analysis PART

def tweet_fcn(tweet_index, lines_list, tweet_analysis, file_choice):
    tweet_dict = {}
    tweet_dict_short = {}
    
    if tweet_analysis == "Yes":
        tweet_use = tweet_dict_short
    else:
        tweet_use = tweet_dict
        
    for line in lines_list[1:]:
        tweet = line[tweet_index]
        if file_choice == "1":
            t_content = re.findall('@[\w]*\s(.*)[http]', tweet)
        else:
            t_content = re.findall('@[\w]*[:](.*)', tweet)
            
        if len(t_content) >0:
            t_words = t_content[0].split()
        
        # Create a dictionary with all the words
        for word in t_words:
            if word not in tweet_dict:
                tweet_dict[word] = 1
            else:
                tweet_dict[word] += 1
        # Create a dictionary with all the words except some irrelavant/non-functional words
        irvt_words = ['I','i',"I'm",'me','my','you','your','we','and','a','an','for','on','to','the','but','with','of','be','is','are','was','been','in','at','t','it','this','that','-']
        for word in t_words:
            if word not in irvt_words:
                if word not in tweet_dict_short:
                    tweet_dict_short[word] = 1
                else:
                    tweet_dict_short[word] += 1
    
    # Find and print the 10 frequently used words in tweets
    def large_find_print(tweet_dict): 
        tweet_list = list(tweet_dict.values())
    
        large1 = 0
        large2 = 0
        large3 = 0
        large4 = 0
        large5 = 0
        large6 = 0
        large7 = 0
        large8 = 0
        large9 = 0
        large10 = 0
        
        for num in tweet_list:
            if num > large1:
                large1 = num
        for num in tweet_list:
            if num > large2 and num < large1:
                large2 = num
        for num in tweet_list:
            if num > large3 and num < large2:
                large3 = num
        for num in tweet_list:
            if num > large4 and num < large3:
                large4 = num
        for num in tweet_list:
            if num > large5 and num < large4:
                large5 = num 
        for num in tweet_list:
            if num > large6 and num < large5:
                large6 = num   
        for num in tweet_list:
            if num > large7 and num < large6:
                large7 = num  
        for num in tweet_list:
            if num > large8 and num < large7:
                large8 = num 
        for num in tweet_list:
            if num > large9 and num < large8:
                large9 = num   
        for num in tweet_list:
            if num > large10 and num < large9:
                large10 = num   
        # print(large1,large2,large3,large4,large5,large6,large7,large8,large9,large10)
        
        print("10 most frequently used words:")
        for item in tweet_dict:
            if tweet_dict[item] == large1:
                # print(type(item))
                # print(type(tweet_dict[item]))
                # print(item,tweet_dict[item])  
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large2:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large3:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large4:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large5:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large6:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])])) 
        for item in tweet_dict:
            if tweet_dict[item] == large7:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large8:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large9:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        for item in tweet_dict:
            if tweet_dict[item] == large10:
                if len(item) < 7:
                    print('\t\t'.join([item,str(tweet_dict[item])]))
                else:
                    print('\t'.join([item,str(tweet_dict[item])]))
        
    if tweet_use == tweet_dict_short:
        large_find_print(tweet_dict_short)
    else:
        large_find_print(tweet_dict)
        
        

### Tweets and Sentiment/Negative Reason/Airline Interaction PART

def tweet_inter_fcn(index, tweet_index, lines_list, file_choice):
    records_dict = {}
    tweet_dict = {}
        
    for line in lines_list[1:]:
        inter_item = line[index]
        if inter_item not in records_dict:
            records_dict[inter_item] = 1
        else:
            records_dict[inter_item] += 1           
    
    for inter_item in records_dict:
        print(inter_item)
            
        for line in lines_list[1:]:
            if line[index] == inter_item:
                tweet = line[tweet_index]
                if file_choice == "1":
                    t_content = re.findall('@[\w]*\s(.*)[http]', tweet)
                else:
                    t_content = re.findall('@[\w]*[:](.*)', tweet)
            
                if len(t_content) >0:
                    t_words = t_content[0].split()
                irvt_words = ['I','i',"I'm",'me','my','you','your','we','and','a','an','for','on','to','the','but','with','of','be','is','are','was','been','in','at','t','it','this','that','-']
                for word in t_words:
                    if word not in irvt_words:
                        if word not in tweet_dict:
                            tweet_dict[word] = 1
                        else:
                            tweet_dict[word] += 1
        
        
        # Find and print the 10 frequently used words in tweets
        def large_find_print(tweet_dict): 
            tweet_list = list(tweet_dict.values())
        
            large1 = 0
            large2 = 0
            large3 = 0
            large4 = 0
            large5 = 0
            large6 = 0
            large7 = 0
            large8 = 0
            large9 = 0
            large10 = 0
            
            for num in tweet_list:
                if num > large1:
                    large1 = num
            for num in tweet_list:
                if num > large2 and num < large1:
                    large2 = num
            for num in tweet_list:
                if num > large3 and num < large2:
                    large3 = num
            for num in tweet_list:
                if num > large4 and num < large3:
                    large4 = num
            for num in tweet_list:
                if num > large5 and num < large4:
                    large5 = num 
            for num in tweet_list:
                if num > large6 and num < large5:
                    large6 = num   
            for num in tweet_list:
                if num > large7 and num < large6:
                    large7 = num  
            for num in tweet_list:
                if num > large8 and num < large7:
                    large8 = num 
            for num in tweet_list:
                if num > large9 and num < large8:
                    large9 = num   
            for num in tweet_list:
                if num > large10 and num < large9:
                    large10 = num   
            
            print("\t 10 most frequently used words:")
            for item in tweet_dict:
                if tweet_dict[item] == large1:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large2:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large3:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large4:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large5:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large6:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])])) 
            for item in tweet_dict:
                if tweet_dict[item] == large7:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large8:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large9:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
            for item in tweet_dict:
                if tweet_dict[item] == large10:
                    if len(item) < 7:
                        print('\t', '\t\t'.join([item,str(tweet_dict[item])]))
                    else:
                        print('\t', '\t'.join([item,str(tweet_dict[item])]))
        
        large_find_print(tweet_dict)
        


### Retweet and Sentiment/Negative Reason/Airline Interaction PART

def retweet_inter_fcn(index, retweet_index, lines_list):
    records_dict = {}
    # print(index)
    for line in lines_list[1:]:
        inter_item = line[index]
        retweet_count = line[retweet_index]
        # print(inter_item,retweet_count)
        if inter_item not in records_dict:
            records_dict[inter_item] = int(retweet_count)
        else:
            records_dict[inter_item] += int(retweet_count)
    # print(records_dict)
    
    records_list = list(records_dict.keys())
    records_list.sort()
    
    print_length = 0
    for item in records_list:
        if len(item) > print_length:
            print_length = len(item)
    
    # Frequency Table
    for item in records_list:
        if len(item) > 0:
            print(item, " "*(print_length-len(item)), records_dict[item])
    print("\n")
    
    # Histogram
    records_count_sum = sum(records_dict.values())
    for item in records_list:
        if len(item) > 0:
            star = round(records_dict[item]/records_count_sum*100,2)
            prop = round(records_dict[item]/records_count_sum*100,2)
            print(item, " "*(print_length-len(item)), "*"*int(star), str(prop)+"%")
    print("\n")
            