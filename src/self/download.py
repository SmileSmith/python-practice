import datetime
import re
import os.path
from urllib import request
import requests

def save_file(download_url, path):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    start_time = datetime.datetime.now()
    print(str(start_time)[:-7])
    if (os.path.isfile(path)):
        file_size = os.path.getsize(path)/1024/1024
        print("file size is " + str(file_size) + " MB ...")
        return 
    else:
        print("start downloading ...")
        response = requests.get(download_url, stream = True)
        with open(path.encode("utf-8"), "wb") as code:
            code.write(response.content)
        end_time = datetime.datetime.now()
        use_time = end_time - start_time
        file_size = os.path.getsize(path)/1024/1024
        print(str(end_time)[:-7])
        print(path + " Done ...")
        print("file size is " + str(file_size) + " MB ...")

def get_download_url(website_url):
    web_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = request.Request(website_url, None, web_header)
    content = request.urlopen(req).read().decode('gbk')
    while len(content) < 100:
        print("try again ...")
        request.urlopen(req).read().decode('gbk')
    print("web page all length: " + str(len(content)))

    pattern = re.compile("http://m4.26ts.com/[.0-9-a-zA-Z]*.mp4")
    match_urls = pattern.findall(content)

    if len(match_urls) == 0:
        print("No video found ...")
        return

    while len(match_urls) > 0:
        the_url = match_urls.pop()
        the_url = the_url.replace("http://", "https://")
        save_file(the_url, the_url[19:])

URLS = ["http://www.46ek.com/view/22133.html"]
print("videos to download...")
get_download_url(URLS[0])
print("All done")
