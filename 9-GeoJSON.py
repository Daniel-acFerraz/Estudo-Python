import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42'

while True:
    adress = input('Enter location: ')
    if len(adress) < 1 : break

    url = serviceurl + urllib.parse.urlencode({"adress": adress})
    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characteres')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==========Failure To Retrieve==========')
        print(data)
        continue

    print(json.dumps(js, intend = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print("lat", lat, "lng", lng)
    location = js['results'][0]['formatted_adress']
    print(location)