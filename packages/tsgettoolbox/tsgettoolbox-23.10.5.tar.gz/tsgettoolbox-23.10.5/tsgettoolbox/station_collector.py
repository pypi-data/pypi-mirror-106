from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import os
import pprint

_ndict = {}


def read_url(url):
    url = url.replace(" ", "%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, "html.parser")
    x = soup.find_all("a")
    for i in x:
        file_name = i.extract().get_text()
        url_new = url + file_name
        url_new = url_new.replace(" ", "%20")
        if file_name[-1] == "/" and file_name[0] != ".":
            read_url(url_new)
        year = os.path.dirname(url_new)
        year = os.path.basename(year)
        try:
            year = int(year)
        except ValueError:
            continue
        key = os.path.basename(url_new)
        if ".csv" not in key:
            continue
        _ndict.setdefault(key, []).append(year)
        print(key, year)


read_url("https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/")

for nkey in _ndict:
    _ndict[nkey] = [_ndict[nkey][0], _ndict[nkey][-1]]

pp = pprint.pformat(_ndict)

with open("gsod_stations.py", "w") as file:
    file.write(pp)

_ndict = {}
read_url("https://www.ncei.noaa.gov/data/global-summary-of-the-month/access/")

for nkey in _ndict:
    _ndict[nkey] = [_ndict[nkey][0], _ndict[nkey][-1]]

pp = pprint.pformat(_ndict)

with open("gsom_stations.py", "w") as file:
    file.write(pp)
