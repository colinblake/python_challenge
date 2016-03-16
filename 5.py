import pickle
from pprint import pprint
import sys
with open('banner.p', 'rb') as f:
    data = pickle.load(f)
    #pprint(data)

for line in data:
    #pprint(line)
    for command in line:
        for i in range(0,command[1]):
            sys.stdout.write(command[0])
    print
