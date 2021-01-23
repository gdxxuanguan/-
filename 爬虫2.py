import requests
import json
import pprint
import xlwt
from chsauwn import bv转av
def bvtocomment(BV,MainReplyNum):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('B站评论')
    worksheet.write(0, 0, '评论')

    # wangzhi="https://www.bilibili.com/video/BV12E411A7ZQ?p=23"
    # wangzhi1=wangzhi.split('BV')
    # BV="BV"+wangzhi1[1].split('?')[0]


    for x in range (1,50):
        str1="https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn="+str(x)+"&type=1&oid="+bv转av.main(BV)+"&sort=2&_=1611217919901"
        r=requests.get(str1)
        data=json.loads(r.text)
        # pprint.pprint(data)
        # for i in data['data']['replies']:
        #     pprint.pprint(i['content']['message'])
        #




        for i in data['data']['replies']:
            if i['like']>5:
                worksheet.write(MainReplyNum, 0, i['content']['message'])
                MainReplyNum += 1
            if i['replies'] is None:
                a=0
            else:
                for j in i['replies']:
                    if j['like']>5:
                        pprint.pprint(j['content']['message'])
                        worksheet.write(MainReplyNum, 0, j['content']['message'])
                        MainReplyNum += 1
    return MainReplyNum
    workbook.save('影流之主评论爬取.xls')
bvtocomment("BV1Qt411T7VS",1)