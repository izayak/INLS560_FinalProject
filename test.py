filename1 = "Tweets copy.csv"
with open(filename1) as f:
    lines = f.readlines()

lines_list = []
for line in lines:
    lines_list.append(line.split(","))
# print(lines_list)
# print(lines_list[1])

for line in lines_list:
    print(line[0])