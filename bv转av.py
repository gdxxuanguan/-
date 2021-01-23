import requests
import codecs


def av2bv(avid):
    site = "https://api.bilibili.com/x/web-interface/view?aid=" + str(avid)
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return "视频不存在！"
    return lst[13]


def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return "视频不存在！"
    return int(lst[16][1:-1])


# print("author：Mengo \n请选择模式（输入1或2）：\n(1：AV号转换为BV号，2：BV号转换为AV号)")
# a = int(input())
# while a not in [1, 2]:
#     print("输入错误！请重新输入！")
#     a = int(input())
# if a == 1:
#     print("\n请输入AV号：")
#     av = input()
#     av = av.replace("av", "")
#     print("\nBV号为：\n" + str(av2bv(int(av))))
# elif a == 2:
#     print("\n请输入BV号：")
#     print("\nAV号为：\nav" + str(bv2av(str(input()))))
# print("\n按任意键退出。")
# input()
def main(a):
    return str(bv2av(str(a)))
# if __name__=='__main__':
#     print(main("BV12E411A7ZQ"))