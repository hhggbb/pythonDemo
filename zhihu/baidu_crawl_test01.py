"""
百度爬虫
"""
# 导入urllib库的urlopen函数
from urllib.request import urlopen
# 导入BeautifulSoup
# from bs4 import BeautifulSoup as bf
from bs4 import BeautifulSoup
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve

# 发出请求，获取html
html = urlopen("http://www.baidu.com/")
# 获取的html内容是字节，将其转化为字符串
# html_text = bytes.decode(html.read())
# 打印html内容
# print(html_text)
# 用BeautifulSoup解析html
obj = BeautifulSoup(html.read(), 'html.parser')
# 从标签head、title里提取标题
title = obj.head.title
# 打印标题
# print(title)
# 使用find_all函数获取所有图片的信息
pic_info = obj.find_all('img')
# 分别打印每个图片的信息
# for i in pic_info:
#     print(i)

# 只提取logo图片的信息
logo_pic_info = obj.find_all('img', class_="index-logo-src")
# 提取logo图片的链接
logo_url = "https:" + logo_pic_info[0]['src']
# 打印链接
print(logo_url)
# 使用urlretrieve下载图片
urlretrieve(logo_url, 'logo.png')
