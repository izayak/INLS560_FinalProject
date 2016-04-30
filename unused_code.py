# def large_find(tweet_list,upper,lower):
#     for num in tweet_list:
#         if num > lower and num < upper:
#             large = num
#     return large


# tweet_list.sort() <-- does not work


## In time_inter_fcn: have to build a new dictionary
# time_count_sum = sum(records_dict[inter_item].values())            
# for item in records_dict[inter_item]:
#     prop = round(records_dict[inter_item][item]/time_count_sum*100,2)
#     print("\t", '\t'.join([records_dict[inter_item], str(records_dict[inter_item][item]), str(prop)+"%"]))    



# # Frequency Table
# for item in lst:
#     print('\t'.join([str(item), str(day_dict[item])]))
# print("\n")

# # Histogram
# day_count_sum = sum(day_dict.values())
# for item in lst:
#     star = round(day_dict[item]/day_count_sum*100,2)
#     prop = round(day_dict[item]/day_count_sum*100,2)
#     print('\t'.join([str(item), "*"*int(star), str(prop)+"%"]))
# print("\n")