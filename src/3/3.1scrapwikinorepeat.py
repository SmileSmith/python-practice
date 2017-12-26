import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

PAGES = set()

COUNT = 0

def countUp():
    global COUNT
    COUNT = COUNT + 1


def get_links(url):
    global PAGES
    html = urlopen("http://en.wikipedia.org" + url)
    bs = BeautifulSoup(html, "html.parser")
    try:
        print(bs.find("h1").get_text())
        print(bs.find(id="mw-content-text").find_all("p")[0].get_text())
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")
    for link in bs.find_all("a", href=re.compile("^/wiki/((?!:).)*$")):
        if "href" in link.attrs:
            if link.attrs["href"] not in PAGES:
                # it is a new page
                new_page = link.attrs["href"]
                count_str = '%d' %COUNT
                print("----------------\n" + count_str + ' ***' + new_page)
                countUp()
                PAGES.add(new_page)
                get_links(new_page)
# run
get_links("")
