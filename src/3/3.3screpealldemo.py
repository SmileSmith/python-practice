import re
import datetime
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())

# 获取页面内的所有内链的集合
def getInternalLinks(bs_obj, includeUrl):
    internal_links = []
    # 找出所有以'/'开头的链接
    for link in bs_obj.findAll("a", href=re.compile("^(/|.*)" + includeUrl + ")")):
        url = link.attrs["href"]
        if url is not None and url not in internal_links:
            internal_links.append(url)
    return internal_links

def getExternalLinks(bs_obj, excludeUrl):
    external_links = []
    # 找出所有以“http”或者“www”或者“//”开头，并且不包含当前url的链接
    for link in bs_obj.findAll("a", href=re.compile("^(http|www|//)((?!" + excludeUrl + ").)*$")):
        url = link.attrs["href"]
        if url is not None and url not in external_links:
            external_links.append(url)
    return external_links

def splitAddress(address):
    addressParts = address.replace("http://", "").replace("//", "").split("/")
    return addressParts

def getRandomExternalPage(startUrl):
    html = urlopen(startUrl)
    print("\nopen: " + startUrl)
    bs_obj = BeautifulSoup(html, "html.parser")
    external_links = getExternalLinks(bs_obj, splitAddress(startUrl)[0])
    if len(external_links) == 0:
        internal_links = getInternalLinks(bs_obj, startUrl)
        return getRandomExternalPage(internal_links[random.randint(0, len(internal_links)) - 1])
    else:
        return external_links[random.randint(0, len(external_links) - 1)]

def followExternalOnly(startSite):
    external_link = getRandomExternalPage(startSite)
    print("\nexternal link is: " + external_link)
    followExternalOnly(external_link)

followExternalOnly("http://oreilly.com")
