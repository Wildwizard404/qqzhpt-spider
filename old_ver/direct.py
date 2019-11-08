# -- coding: UTF-8 --
import re
import urllib
import sys
import urllib.request
from PIL import Image
import os

def work(imgurl):
    try:
        name = imgurl.split("img/")[1]
        print(name)
        picget = urllib.request.urlopen(imgurl).read()
        print(type(picget))
        with open("temp", "wb") as code:
            code.write(picget)
        Image.open("temp").save(name)
    except:
        print('Unexpected error:',sys.exc_info())

if __name__=='__main__':
    url = "http://img.qqzhpt.com/meitustatic/images/img/18248/"
    tot = 10
    route = url.split("img/")[1][:-1]
    if not os.path.exists(route):
        os.mkdir(route)
    for i in range(1,tot+1):
        work(url+str(i)+".jpg")
