"""Solves http://www.pythonchallenge.com/pc/def/integrity.html"""
# imports
import sys
import bz2

# constants
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


# exception classes
# interface functions
# classes
# internal functions & classes

def main():
    clearun = bz2.decompress(un))  # huge
    clearpw = bz2.decompress(pw))  # file

    # log in by clicking the bee


    if __name__ == '__main__':
        status = main()
    sys.exit(status)
