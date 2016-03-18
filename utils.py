
import urllib.request
import urllib.response
import sys

def save_url_to_file(url, filename):
    with urllib.request.urlopen(url) as response:
        with open(filename, 'wb') as file:
            if file.write(response.read()):
                return 0;
    return 1

def save_url_to_file_with_auth(url, filename, username, password):
    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    password_mgr.add_password(None, url, username, password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)

    with urllib.request.urlopen(url) as response:
        with open(filename, 'wb') as file:
            if file.write(response.read()):
                return 0;
    return 1