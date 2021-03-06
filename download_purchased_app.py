GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

from gpapi.googleplay import GooglePlayAPI, RequestError
import sys
from config import *

server = GooglePlayAPI('en_US', 'America/New_York')

if (len(sys.argv) < 2):
    print "Usage: %s packagename [filename]"
    print "Download an app."
    print "If filename is not present, will write to packagename.apk."
    sys.exit(0)

packagename = sys.argv[1]

if (len(sys.argv) == 3):
    filename = sys.argv[2]
else:
    filename = packagename + ".apk"

server.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, None, None)
# check whether this app can be downloaded
# should return error if app not purchased
fl = server.delivery(packagename)
with open(filename, 'wb') as apk_file:
    for chunk in fl.get('file').get('data'):
        apk_file.write(chunk)
    if fl['additionalData'] != []:
        print('\nDownloading additional files\n')
    for obb in fl['additionalData']:
        name = obb['type'] + '.' + str(obb['versionCode']) + '.' + fl['docId'] + '.obb'
        with open(name, 'wb') as second:
            for chunk in obb.get('file').get('data'):
                second.write(chunk)
    print('\nDownload successful\n')