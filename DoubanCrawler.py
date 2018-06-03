import requests
from bs4 import BeautifulSoup

def find_fist_link (link):
    # 1、下载网页源码
    r = requests.get(link)
    soup = BeautifulSoup(r.text,'lxml')
    # 2、找到第一个链接的ID
    fist_link = soup.find(id='mw-content-text')
    # 3、找到链接的tag
    second_step = fist_link.find(class_='mw-parser-output').p
    # 4、得到了第一个链接地址
    get_link = second_step.find('a').get('href')
    return  "https://en.wikipedia.org"+get_link

def check_list(url,target_urls):
    for index,element in enumerate(url):
        if element == target_urls:
            print("find is good")
            return False
        elif len(url) > 25:
            print("no find is over 25")
            return  False
        elif url[-1] in  url[:-1]:
            print("repeat code")
            return  False
        else:
            return  True

# 2、得到第一个链接地址
# 3、得到的网站放入一个列表
link_count = 'https://en.wikipedia.org/wiki/Stefan_Lochner'
target_url = '"https://en.wikipedia.org/wiki/Philosophy"'
limit_links = 21
list =[link_count]
while check_list(list,target_url):
    list.append(find_fist_link(list[-1]))
    print(list)

