from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_bs(url):
    try:
        html = urlopen(url)
        bs_obj = BeautifulSoup(html.read(), "html.parser")
    except HttpError:
        return None
    return bs_obj

def get_title(url):
    bs_obj = get_bs(url)
    try:
        title = bs_obj.body.h1
    except AttributeError:
        return None
    return title

TITLE = get_title("http://pythonscraping.com/pages/page1.html")
if TITLE is None:
    print("Title could not be found")
else:
    print(TITLE)

def get_namelist(url):
    bs_obj = get_bs(url)
    bs_obj.ch
    return bs_obj.find_all("span", {"class": "green"})

NAMELIST = get_namelist("http://www.pythonscraping.com/pages/warandpeace.html")
if NAMELIST is None:
    print("Namelist could not be found")
else:
    for name in NAMELIST:
        print(name.get_text())
