"""http://www.pythonchallenge.com/pc/return/5808.html"""

# imports
import sys
from utils import *
from PIL import Image



# constants
image_url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
local_filename = "scratchfiles/cave.jpp"
username = "huge"
password = "file"

# exception classes
# interface functions
# classes
# internal functions & classes


def main():
    save_url_to_file_with_auth(image_url, local_filename, username, password)
    im_in = Image.open(local_filename)
    w_in,h_in = im_in.size

    w_out, h_out = (int(w_in/2), int(h_in/2))
    print(w_out)
    print(h_out)
    im_out = Image.new("RGB", (w_out, h_out))

    for row in range(0,h_in):
        for col in range(0,w_in):
            if (row + col) % 2 == 0:
                im_out.putpixel((int(col/2), int(row/2)), im_in.getpixel((col,row)))

    im_out.show() #evil
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
