# http://www.pythonchallenge.com/pc/def/oxygen.html
import urllib.request
import urllib.response
from PIL import Image
import sys
import re

local_filename = "oxygen.png"
remote_uri = "http://www.pythonchallenge.com/pc/def/oxygen.png"


def save_url_to_file(url, filename):
    """

    :rtype: Int
    """
    with urllib.request.urlopen(url) as response:
        with open(filename, 'wb') as file:
            if file.write(response.read()):
                return 0;
    return 1

def get_string_from_middle_row(filename, stride):
    im = Image.open(filename)
    w, h = im.size
    return ''.join([chr(im.getpixel((x, h//2))[0]) for x in range(0, w, stride)])

def get_string_from_array_of_character_values_in_string(input_string):
    array_of_values = re.search("\[(.*)\]", input_string).group(1)
    return ''.join([chr(int(i)) for i in array_of_values.split(',')])

def main():
    save_url_to_file(remote_uri, local_filename)
    str1 = get_string_from_middle_row(local_filename,7)
    print(str1)
    print(get_string_from_array_of_character_values_in_string(str1)) #integrity


if __name__ == '__main__':
    status = main()
    sys.exit(status)





