import requests
from bs4 import BeautifulSoup

def find_fist_link (link):
    # 1、下载网页源码
    soup = BeautifulSoup(r.text,'lxml')
    # 2、找到第一个链接的ID
    fist_link = soup.find(id='mw-content-text')
    # 3、找到链接的tag
    second_step = fist_link.find(class_='mw-parser-output').p
    # 4、得到了第一个链接地址
    get_link = second_step.find('a').get('href')
    return  "https://en.wikipedia.org"+get_link

# 2、得到第一个链接地址
# 3、得到的网站放入一个列表
link_count = ['https://en.wikipedia.org/wiki/Stefan_Lochner']
limit_links = 21
while len(link_count)<limit_links:
    # 1、最后一个连接
    r = requests.get(link_count[-1])
    # 2、函数找下一个链接
    add_list = find_fist_link(r)
    # 3、找到的链接添加到列表
    link_count.append(add_list)
    print(link_count)