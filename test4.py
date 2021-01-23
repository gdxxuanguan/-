
import re
import urllib.request
from bs4 import BeautifulSoup
from chsauwn import bv转av
import requests
import json
import pprint
import xlwt
from io import BytesIO
import gzip


FindLink=re.compile(r'href="//www.bilibili.com/video/(.*?)?from=search" target="_blank" title="')
FindLink1=re.compile(r'\d\d\d\d-\d\d-\d\d')

head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
a=1
for j in range(1,5):
    response = urllib.request.Request(
        'https://search.bilibili.com/all?keyword=%E7%96%AB%E6%83%85&order=totalrank&duration=0&tids_1=0&page='+str(j), headers=head)
    r = urllib.request.urlopen(response)
    html = r.read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('div'):
        item = str(item)
        link = re.findall(FindLink, item)
        if (len(link) > 1):
            i = 0
            while (i < len(link)):
                response1=urllib.request.Request('https://www.bilibili.com/video/'+link[i].strip('?')+'?from=search',headers=head)
                r1=urllib.request.urlopen(response1)



                html1 = r1.read()
                buff = BytesIO(html1)
                f = gzip.GzipFile(fileobj=buff)
                html1 = f.read().decode('utf-8')

                soup1 = BeautifulSoup(html1, 'html.parser')
                for item1 in soup1.find_all('div',class_='video-data'):
                    item1 = str(item1)
                    # print(item1)
                time = re.findall(FindLink1, item1)
                print(time)
                a=bvtocomment(link[i].strip('?'),a)  # 打印bv号
                i += 2
            break
    # print('--------------------------------------------------') #分割线