import re

Sum=0

with open("regex_sum_222010.txt") as open_file:
    data = open_file.read()
    num = re.findall('[0-9]+', data)
    for i in range(len(num)):
    	Sum += int(num[i])
    print Sum
