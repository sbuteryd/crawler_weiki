import requests

#1、下载网页
r = requests.get('https://en.wikipedia.org/wiki/Stefan_Lochner')
print(r.text)