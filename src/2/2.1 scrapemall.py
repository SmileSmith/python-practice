from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

HTML = urlopen("http://www.pythonscraping.com/pages/page3.html")
SOUP = BeautifulSoup(HTML.read(), "html.parser")

# 打印所有商品信息
''' for child in SOUP.find("table", {"id": "giftList"}).tr.next_siblings:
    print(child) '''

# 打印所有图片
''' IMAGES = SOUP.find_all("img", {"src": re.compile("^../img/gifts/img.*.jpg$")})
for image in IMAGES:
    print(image.attrs["src"]) '''

# LAMBDA 函数
TWO = SOUP.find(lambda tag: len(tag.attrs) == 2)
print(TWO)
for item in TWO:
    print(item)
