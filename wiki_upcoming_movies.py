#!/usr/bin/python
import wikipedia
import requests
import sys
import time
import re
from datetime import datetime

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action': "query",
    'list': "categorymembers",
    'cmtitle': "Category:Upcoming_films",
    'cmlimit': 20,
    'format': "json"
}

#page = wptools.page('Snatch (film)')
#page = wptools.page(pageid=707808)
#page.get_parse()
#date_string=re.search('\d*\|\d*\|\d*\|United States',page.data['infobox']['released'].strip('{}')).group(0).replace('|United States','')
#datetime_object = datetime.strptime(date_string,'%Y|%m|%d')


lastContinue = {}
while True:
    # Modify it with the values returned in the 'continue' section of the last result.
    PARAMS['cmcontinue']=lastContinue
    # Call API
    print(PARAMS)
    result = requests.get(url=URL, params=PARAMS).json()
    if 'error' in result:
        print(result['error'])
	break
    if 'warnings' in result:
        print(result['warnings'])
    if 'query' in result:
        print(result)
    if 'continue' not in result:
        break
    lastContinue = result['continue']['cmcontinue']
    time.sleep(1)
