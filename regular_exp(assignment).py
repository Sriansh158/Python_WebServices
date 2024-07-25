import re 

handle = open('actual_data4_assignment(RE).txt')

num_list = []

for line in handle:
    line = line.rstrip()

    stuff = re.findall('[0-9]+', line)
    
    for num in stuff:
        num_list.append(int(num))
        
print("total sum is :", sum(num_list))