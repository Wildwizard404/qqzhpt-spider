# qqzhpt-spider
## 情趣综合平台 美图爬虫/批量下载  
虽然站点的title异常涩情，但其实只是一个普通的写真网站。
[url:http://www.qqzhpt.com/meitu/](http://www.qqzhpt.com/meitu/)  
由于众所周知的原因，部分地区可能无法访问网站，请自行解决。   
图片版权归原网站/原作者所有，使用时请注意。   
本项目收录在[awesome-spider](https://github.com/facert/awesome-spider)。  
详细内容发布在[野生巫师页 https://wildwizard.cn/2019/11/09/get_images_from_qqzhpt/]( https://wildwizard.cn/2019/11/09/get_images_from_qqzhpt/)  

## 使用前准备

1. clone代码到本地  
2. 安装依赖  
	>pip install requests   
	>pip install beautifulsoup4   
	>pip install lxml   
3. 访问网站，寻找自己要下载的图集（你不可能打算下载整个站点吧？）  
4. 记录这些图集第一页的url  

## 使用
main.py提供了一个示例，直接运行代码并输入url即可下载该图集。同时可以使用命令行调用：`python main.py url`。  
如果有多条url，可以自己利用qqzhpt.py编写脚本。调用方式为：  
```python
import qqzhpt
if __name__ == '__main__' :
    mission = qqzhpt.meitu("url")
    mission.run()
```
## 注意
仅为下载方便而编写的脚本，完全没有考虑任何异常处理。请严格按照使用方法调用，避免传入错误的url。  
相关内容可于[https://wildwizard.cn/2019/11/09/get_images_from_qqzhpt/](https://wildwizard.cn/2019/11/09/get_images_from_qqzhpt/)查看。