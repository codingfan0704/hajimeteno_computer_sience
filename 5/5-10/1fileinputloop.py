#encoding: utf8

data = open('data.txt', 'r')
for line in data:
    print len(line)