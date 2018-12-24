import requests 
from bs4 import BeautifulSoup as bs
import sys
import time


def printVisa(url):

    r = requests.get(url)

    tables = bs(r.text).findAll('table')

    for table in tables:
        rows = table.findAll('tr')
        data = []
        for row in rows:
            cols = row.findAll('td')
            data.append(cols)
        header = data[0]
        try:
            if header[0].text.lower().find('employment') >=0 and header[0].text.lower().find('based') >=0:
                return '%10s%10s' % ( data[2][2].text.strip(),  data[3][2].text.strip())
        except:
            pass

dates = [
(2019, 'january', 2019),
(2019, 'december', 2018),
(2019, 'november', 2018),
(2019, 'october', 2018),
]

fiscal = (
(2018, 'september', 2018),
(2018, 'august', 2018),
(2018, 'july', 2018),
(2018, 'june', 2018),
(2018, 'may', 2018),
(2018, 'april', 2018),
(2018, 'march', 2018),
(2018, 'february', 2018),
(2018, 'january', 2018),
(2018, 'december', 2017),
(2018, 'november', 2017),
(2018, 'october', 2017),
)

for y in range(7):
    for f in fiscal:
        dates.append( (f[0]-y , f[1], f[2]-y ) )


baseurl = 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/%d/visa-bulletin-for-%s-%d.html'

for d in dates:
    url = baseurl % d
    print "%10s%10s%s" % ( d[2], d[1] , printVisa(url)) 
