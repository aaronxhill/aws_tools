import sys

i = 0

w = open(sys.argv[3], 'w+')

with open(sys.argv[1]) as f:
    for line in f:
        w.write(line)
        i = i + 1
        if (i == int(sys.argv[2]) + 1):
        	break