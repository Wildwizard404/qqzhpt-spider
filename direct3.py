# -- coding: UTF-8 --
import re
import urllib
import sys
import urllib.request
from PIL import Image
import os
import subprocess
import _thread
def work(imgurl,route):
    try:
        #print(r"aria2c "+imgurl+r" -d "+route)
        subprocess.call(r"aria2c "+imgurl+r" -d "+route,shell = True)
    except:
        print('Unexpected error:',sys.exc_info())

if __name__=='__main__':
    url = "http://img.qqzhpt.com/meitustatic/images/img/18248/"
    tot = 10
    route = url.split("img/")[1][:-1]
    if not os.path.exists(route):
        os.mkdir(route)
    for i in range(1,tot+1):
        _thread.start_new_thread(work,(url+str(i)+".jpg",route,))
        print("_thread"+str(i)+"started")
