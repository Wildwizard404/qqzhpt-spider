from bs4 import BeautifulSoup
import requests
import _thread
import os,time
class meitu(object):
    def __init__(self,url):
        self.url = url
        self.urls = []
        self.dir = url.split('/')[5]+'/'
        if os.path.exists(self.dir) == False:
            os.mkdir(self.dir)
        self.locks = []
        self.nloops = []
        self.direct = ''
    def download(self,url,lock):
        web_content = requests.get(url)
        soup = BeautifulSoup(web_content.text,'lxml')
        imgs_list = soup.body.find(class_ = "imgs-list").div.find_all("img")
        imgs_urls = []
        for i in imgs_list:
            imgs_urls.append(i.attrs["src"])
        print("解析图片地址成功，开始下载！")
        self.direct = imgs_urls[0].split('/')[:-1][-1]
        for u in imgs_urls:
            r = requests.get(u)
            with open(self.dir+u.split('/')[-1].split('?')[0], "wb") as code:
                code.write(r.content)
        lock.release()
    def geturls(self):
        web_content = requests.get(self.url)
        soup = BeautifulSoup(web_content.text,'lxml')
        detail_page = soup.body.find(class_ = ['detail-pag','meitu-page']).find_all("a")
        for i in detail_page:
            self.urls.append(i.attrs["href"])
        print("解析页面地址成功！")
    def check(self):
        files = os.listdir(self.dir)
        fails = []
        for i in files:
            if os.path.getsize(self.dir+i) == 0:
                fails.append(i)
        if fails != []:
            self.direct = "http://img.qqzhpt.com/meitustatic/images/img/"+self.direct+'/'
            print("存在文件下载失败，尝试重新下载")
            for f in fails:
                r = requests.get(self.direct+f)
                with open(self.dir+f, "wb") as code:
                    code.write(r.content)
    def run(self):
        print("爬取开始！")
        self.geturls()
        self.nloops = range(len(self.urls))
        for i in self.nloops:
            lock = _thread.allocate_lock()
            lock.acquire()
            self.locks.append(lock)
        for i in self.nloops:
            _thread.start_new_thread(self.download,(self.urls[i],self.locks[i],))
        while True:
            flag = 0
            for i in self.nloops:
                if self.locks[i].locked():
                    flag = 1
            if flag == 0:
                break
        self.check()
