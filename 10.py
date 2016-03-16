"""module docstring"""

# imports
import sys
import itertools
from pprint import pprint

# constants
# exception classes
# interface functions
# classes
# internal functions & classes

def group_description(group):
    return str(len(group))+str(group[0])

def describe_number(number):
    parsed_number = ([list(g) for k, g in itertools.groupby(number)])
    return "".join([group_description(g) for g in parsed_number])

def main():
    a=['1']
    while len(a)<31:
        next_number = describe_number(a[-1])
        #print(next_number)
        a.append(next_number)
    print(len(a[30])) #5808




if __name__ == '__main__':
    status = main()
    sys.exit(status)
