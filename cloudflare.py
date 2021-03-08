from 内置 import *
from urllib.request import urlopen as 打开网址
from urllib.error import HTTPError as HTTP错误
from builtins import bool as 判断
from builtins import int as 整数


def 检测有效(ip: 字符串) -> 判断:
    请求 = 网络请求('http://'+ip, 无, {'Host': 'cp.cloudflare.com'})
    try:
        答复 = 打开网址(请求, 无, 5)
        结果 = 整数(答复.状态) is 204
        return 结果
    except HTTP错误:
        return 否
    pass
