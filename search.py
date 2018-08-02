from gpapi.googleplay import GooglePlayAPI, RequestError
import sys

server = GooglePlayAPI('it_IT', 'Europe/Rome')

if (len(sys.argv) < 2):
    print "Usage: %s request [nb_results] [offset]" % sys.argv[0]
    print "Search for an app."
    print "If request contains a space, don't forget to surround it with \"\""
    sys.exit(0)

request = sys.argv[1]
nb_res = 20
offset = None

if (len(sys.argv) >= 3):
    nb_res = int(sys.argv[2])

if (len(sys.argv) >= 4):
    offset = int(sys.argv[3])

server.login("stone.shijiahao@gmail.com", "zqxuxnlktqqjjluu", None, None)

apps = server.search(request, nb_res, offset)

# print('\nSearch suggestion for "fir"\n')
# print(server.searchSuggest('fir'))

print('nb_result: %d' % nb_res)
print('number of results: %d' % len(apps))

print('\nFound those apps:\n')
for a in apps:
    print("Title: " + a['title'] + ", PackageName: " + a['docId'] + ", Author: " + a['author'])

# {'files': [{'fileType': 0, 'version': 7, 'size': 23246144L}], 'recentChanges': u'', 'docId': u'com.unity.unitystagingproject', 'description': u'', 'title': u'UDPgame', 'author': u'Stone Shi', 'containsAds': u'', 'versionString': u'', 'aggregateRating': {'commentCount': 0L, 'fourStarRatings': 0L, 'oneStarRatings': 0L, 'twoStarRatings': 0L, 'fiveStarRatings': 0L, 'type': 2, 'starRating': 0.0, 'threeStarRatings': 0L, 'ratingsCount': 0L}, 'versionCode': 7, 'offer': [{'offerType': 1, 'micros': 0L, 'currencyCode': u'USD', 'formattedAmount': u'', 'saleEnds': u'', 'checkoutFlowRequired': False}], 'installationSize': 23246144L, 'unstable': True, 'uploadDate': u'24 lug 2018', 'dependencies': [], 'detailsUrl': u'details?doc=com.unity.unitystagingproject', 'images': [{'url': u'https://lh3.googleusercontent.com/IqqRcOiztNHJKnJlrie6b0x1cFY3otyT6aVrmsendF04tboly4BEIf8cUT8S8G1yBaQ', 'width': 512, 'supportsFifeUrlOptions': True, 'imageType': 4, 'height': 512}, {'url': u'https://lh3.googleusercontent.com/V1pJi6Qx5FbvjybKYnBXZQF_zbrNxksp_dld9GTLKJq5o6yNmkFKubWL20oiTrabOCo', 'width': 1024, 'supportsFifeUrlOptions': True, 'imageType': 2, 'height': 500}], 'permission': [], 'category': {'appCategory': u'GAME_ROLE_PLAYING', 'appType': u'GAME'}, 'numDownloads': u'Pi\xf9 di 0 di download'}