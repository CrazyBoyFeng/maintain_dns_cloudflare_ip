from 组件 import *
from urllib.request import urlopen as 打开网址
from urllib.error import HTTPError as Http错误
from builtins import bool as 判断
from builtins import int as 整数
from builtins import str as 字符串


def 检测有效(ip: 字符串, 响应超时: 整数 = 5) -> 判断:
    请求 = 网络请求('http://' + ip, 无, {'Host': 'cp.cloudflare.com'})
    try:
        答复 = 打开网址(请求, 无, 响应超时)
        结果 = 整数(答复.状态) == 204
        return 结果
    except Http错误:
        return 否
    pass
