import requests
import json
import pprint
r=requests.get("https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn=1&type=1&oid=97960469&sort=2&_=1611217919901")
data=json.loads(r.text)
pprint.pprint(data['data'])
# for i in data['data']['replies']:
#     pprint.pprint(i['content']['message'])