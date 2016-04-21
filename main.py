#!/usr/bin/python3

filename = "airlines_concise.csv"
filename1 = "Tweets copy 2.csv"
with open(filename) as f:
    lines = f.readlines()

lines_list = []
for line in lines:
    lines_list.append(line.split(","))
# print(lines_list[0])
# print(lines_list[1])

sentiment_index = 1
sent_conf_index = 2
neg_reason_index = 3
airline_index = 5

# sentiment_list = []
# sent_conf_list = []
# neg_reason_list = []


### Airlines and Negative Count and Negative Reason Analysis TOGETHER

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
print(records_dict)
print("\n")

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
 
# Contingency Table        
for airline in records_list:
    print(airline)
    print("   Sentiment")
    for sentiment in records_dict[airline]["sentiment"]:
        print("\t", sentiment, " "*(sentiment_print_length-len(sentiment)), records_dict[airline]["sentiment"][sentiment])
    print("   Negative Reason")
    for neg_reason in records_dict[airline]["neg_reason"]:
        print("\t", neg_reason, " "*(neg_reason_print_length-len(neg_reason)), records_dict[airline]["neg_reason"][neg_reason])
print("\n")


### Airlines Analysis PART

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
    print(item, " "*(print_length-len(item)), airlines_dict[item])
print("\n")

# Histogram
airlines_count_sum = sum(airlines_dict.values())
for item in airlines_list:
    star = round(airlines_dict[item]/airlines_count_sum*200,2)
    prop = round(airlines_dict[item]/airlines_count_sum*100,2)
    print(item, " "*(print_length-len(item)), "*"*int(star), prop, "%")
print("\n")



### Negative Reason Analysis PART

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
        print(item, " "*(print_length-len("Not Stated")), "*"*int(star), prop, "%")
    elif item == "Longlines":
        star = round(neg_reason_dict["longlines"]/neg_reason_count_sum*200,2)
        prop = round(neg_reason_dict["longlines"]/neg_reason_count_sum*100,2)
        print(item, " "*(print_length-len("Longlines")), prop, "%")
        print(item, " "*(print_length-len("Longlines")), "*"*int(star), prop, "%")
    else:
        star = round(neg_reason_dict[item]/neg_reason_count_sum*200,2)
        prop = round(neg_reason_dict[item]/neg_reason_count_sum*100,2)
        print(item, " "*(print_length-len(item)), "*"*int(star), prop, "%")
        
