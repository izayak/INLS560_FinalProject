#!/usr/bin/python3

filename = "airlines_concise.csv"
with open(filename) as f:
    lines = f.readlines()
# print(lines)

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

records = {}
for line in lines_list[1:]:
    # print(line[5])
    # tweets_list.append(line[tweets_index])
    sentiment = line[sentiment_index]
    airline = line[airline_index]
    neg_reason = line[neg_reason_index]
    
    if airline not in records:
        records[airline] = { "sentiment":{}, "neg_reason":{} }
        if sentiment not in records[airline]["sentiment"]:
            records[airline]["sentiment"][sentiment] = 1
        else:
            records[airline]["sentiment"][sentiment] += 1
        if neg_reason not in records[airline]["neg_reason"]:
            records[airline]["neg_reason"][neg_reason] = 1
        else:
            records[airline]["neg_reason"][neg_reason] += 1
    else:
        if sentiment not in records[airline]["sentiment"]:
            records[airline]["sentiment"][sentiment] = 1
        else:
            records[airline]["sentiment"][sentiment] += 1
        if neg_reason not in records[airline]["neg_reason"]:
            records[airline]["neg_reason"][neg_reason] = 1
        else:
            records[airline]["neg_reason"][neg_reason] += 1
print(records)
print("\n")

airlines = {}
for line in lines_list[1:]:
    airline = line[airline_index]
    if airline not in airlines:
        airlines[airline] = 1
    else:
        airlines[airline] += 1
print(airlines)
print("\n")

neg_reason_dict = {}
for line in lines_list[1:]:
    neg_reason = line[neg_reason_index]
    if neg_reason not in neg_reason_dict:
        neg_reason_dict[neg_reason] = 1
    else:
        neg_reason_dict[neg_reason] += 1
print(neg_reason_dict)