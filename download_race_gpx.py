"""
Download GPX from a running-race page in Strava

For example, let's consider the Brooklyn Half. The link to the race and course map is here:
https://www.strava.com/running-races/2018-popular-brooklyn-half

But there is no option to download the GPX from here. If you visit the page and examine the HTML source code, you'll see this:

var runningRaceJson = {
      "id": 1669,
      "name": "Popular Brooklyn Half",
      "distance": 21097.0,
      "city": "Brooklyn",
      "state": "NY",
      "measurement_preference": null,
      "url": "2018-popular-brooklyn-half",
      "start_date_local": "2018-05-19T07:00:00Z",
      "vanity": "2018-popular-brooklyn-half"
    };

This gives us a route ID of 1669. We can use this to download the GPX data.

"""

import requests
import time

# Visit https://www.strava.com/settings/api to get all this info
CLIENT_ID = 'SEE LINK ABOVE'
ACCESS_TOKEN = 'SEE LINK ABOVE'

headers = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}

###########################

ROUTE_ID = 1669
filename = 'brooklynhalf.gpx'

# save to file
url = 'https://www.strava.com/api/v3/routes/{}/export_gpx'.format(ROUTE_ID)
r = requests.get(url, headers=headers)
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)


