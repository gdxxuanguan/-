import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
from io import BytesIO
import gzip


# import sqlite3
def main():
    baseurl="https://www.bilibili.com/video/BV12E411A7ZQ?p=23"
    # getData(baseurl)
    # savepath=".\\批站评论.xlsx"
    # saveDate(savepath)
    getData(baseurl)
    #爬取网页
    # 解析代码
    # 存数据
# 爬取网页

def getData(baseurl):


    dataList=[]
    html=askURL(baseurl)
    soup=BeautifulSoup(html,"html.parser")
    for i in soup.find_all('div',class_="l-con"):
        print(i)
    return dataList

def askURL(url):
    head={     #模拟浏览器头部信息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
    }
    #     伪装
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read()
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode('utf-8')
        # print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html




def saveDate(savepath):
    cnm=0

if __name__=='__main__':
    main()
