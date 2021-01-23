import requests
import codecs


def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return "视频不存在！"
    return int(lst[16][1:-1])


def main(a):
    return str(bv2av(str(a)))
