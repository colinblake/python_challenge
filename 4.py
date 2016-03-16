import urllib
import re
from pprint import pprint
param = 'nothing'
value = 12345

for i in range(0,400):
    params = urllib.urlencode({param: value})
    #print params
    url = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % params)
    page = url.read()
    print page

    #match = re.search('next', 'and the next nothing is 44827')
    match = re.search('next ([a-z]*) is ([0-9]*)', page)

    if match:
        param = match.group(1)
        if param:
            print 'param = ' + param
        else:
            print 'param not found'
            exit(0)
        value = int(match.group(2))
        if param:
            print 'value = ' + str(value)
        else:
            print 'value not found'
            exit(0)
    else:
        print "did not match the key value string"

    if re.search('Divide by two', page):
        value = value/2
        print 'dividing by two: '

    if re.search('html', page):
        exit(0)


    #print urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').getcode()
    #print urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').info()
    #pprint(locals())
    print '-----'
