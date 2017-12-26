import re
import random
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

''' HTML = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
SOUP = BeautifulSoup(HTML, "html.parser")

for link in SOUP.find("div", {"id": "bodyContent"}).find_all("a", href = re.compile("^/wiki/((?!:).)*$")):
    print(link.attrs["href"]) '''


TARGET = re.compile('')

#生成随机数种子
random.seed(datetime.datetime.now())

def get_links(url):
    html = urlopen("http://en.wikipedia.org/" + url)
    soup = BeautifulSoup(html, "html.parser")
    return soup.find("div", {"id": "bodyContent"}).find_all("a", href = re.compile("^/wiki/((?!:).)*$"));

links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    href = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(href)
    links = get_links(href)
    
        
