import urllib
import zipfile
import datetime
import re
import sys

zf = zipfile.ZipFile("channel.zip")

print zf.open('readme.txt').read()

filename = '90052.txt'
while(1):
    clue = zf.open(filename).read()
    sys.stdout.write( zf.getinfo(filename).comment )

    match = re.search('Next nothing is ([0-9]*)', clue)
    if match:
        filename = match.group(1)+'.txt'
    else:
        break
