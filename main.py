# -- coding: UTF-8 --
import re
import urllib
import sys
import urllib.request
from PIL import Image
def work(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    page = response.read().decode('utf-8')
    #print(page)
    reg=r'src="(.+?\.jpg)"'     #正则表达是筛选图片格式
    img = re.compile(reg)       #创建模式对象
    imglist = re.findall(img,page)   #解析页面源码获取图片列表
    for imgurl in imglist:
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
    return imglist

if __name__=='__main__':
    url = "http://www.qqzhpt.com/meitu/detail/1562014808513"
    for i in range(1,3):
        work(url+str(i))
