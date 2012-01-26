file = open('data.txt', 'r')

for line in file:
    line = line.strip()
    print len(line)