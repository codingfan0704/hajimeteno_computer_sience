number_weight_list = []

file = open('alkaline_metals.txt')
for line in file:
    item = line.split()
    number_weight_list.append(item)

print number_weight_list