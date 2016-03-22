"""http://www.pythonchallenge.com/pc/return/evil.html"""

# imports
import sys
from utils import *
from PIL import Image



# constants
gfx_url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
gfx_filename = "scratchfiles/evil2.gfx"
username = "huge"
password = "file"

# exception classes
# interface functions
# classes
# internal functions & classes


def main():
    save_url_to_file_with_auth(gfx_url, gfx_filename, username, password)
    with open(gfx_filename, "rb") as gfx:
        gfx_data = gfx.read()
        for filenum in range(5):
            filename_out = "scratchfiles/evil" + str(filenum)
            with open(filename_out, "wb") as fout:
                fout.write(gfx_data[filenum::5])
            Image.open(filename_out).show()
        im = Image.fromarray([gfx_data[0:-1:5]])
        im.show()
    return 0 #disproportional


if __name__ == '__main__':
    status = main()
    sys.exit(status)


