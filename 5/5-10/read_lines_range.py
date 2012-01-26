#encoding: UTF-8
import sys

if __name__ == '__main__':

    start_line = int(sys.argv[1])
    end_line = int(sys.argv[2])
    
    data = open('data.txt', 'r')
    data_list = data.readlines()
    data.close()
    
    for line in data_list[start_line:end_line]:
        print line.strip()