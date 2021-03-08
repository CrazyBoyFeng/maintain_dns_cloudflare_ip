from 内置 import *
from ipaddress import IPv4Network as IPv4地址
from random import randint as 随机整数
from random import choice as 范围
from builtins import int as 整数
from typing import Tuple as 元组


def 整数边界(cidr: 字符串) -> 元组[整数, 整数]:
    地址 = IPv4地址(cidr)
    return 整数(地址[0]), 整数(地址[-1])


def 整数范围() -> 范围:
    return 范围([
        整数边界('173.245.48.0/20'),
        整数边界('103.21.244.0/22'),
        整数边界('103.22.200.0/22'),
        整数边界('103.31.4.0/22'),
        整数边界('141.101.64.0/18'),
        整数边界('108.162.192.0/18'),
        整数边界('190.93.240.0/20'),
        整数边界('188.114.96.0/20'),
        整数边界('197.234.240.0/22'),
        整数边界('198.41.128.0/17'),
        整数边界('162.158.0.0/15'),
        整数边界('104.16.0.0/12'),
        整数边界('172.64.0.0/13'),
        整数边界('131.0.72.0/22')
    ])


ip范围 = 整数范围()


def 随机ip(排除: 字符串) -> 字符串:
    ip = 排除
    while ip is 排除:
        整数ip = 随机整数(*ip范围)
        ip = 字符串(IPv4地址(整数ip))
    return ip
