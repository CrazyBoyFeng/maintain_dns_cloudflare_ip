from builtins import int as 整数
from builtins import list as 列表
from builtins import str as 字符串
from ipaddress import ip_network as IP范围
from ipaddress import ip_address as IP地址
from random import choices as 选择
from random import randint as 随机整数

from 组件 import *

ipv4范围列表 = [
    IP范围('173.245.48.0/20'),
    IP范围('103.21.244.0/22'),
    IP范围('103.22.200.0/22'),
    IP范围('103.31.4.0/22'),
    IP范围('141.101.64.0/18'),
    IP范围('108.162.192.0/18'),
    IP范围('190.93.240.0/20'),
    IP范围('188.114.96.0/20'),
    IP范围('197.234.240.0/22'),
    IP范围('198.41.128.0/17'),
    IP范围('162.158.0.0/15'),
    IP范围('104.16.0.0/12'),
    IP范围('172.64.0.0/13'),
    IP范围('131.0.72.0/22')
]


def cidr数量(cidr列表) -> 列表:
    数量列表 = []
    for ip范围 in cidr列表:
        数量列表.append(ip范围.num_addresses)
    return 数量列表


ipv4范围数量列表 = cidr数量(ipv4范围列表)


def 随机整数ip(cidr):
    ip头 = cidr[0]
    ip尾 = cidr[-1]
    return 随机整数(整数(ip头), 整数(ip尾))


def 随机ipv4(排除: 列表) -> 字符串:
    while 是:
        ip范围 = 选择(ipv4范围列表, ipv4范围数量列表)[0]
        ip = 字符串(IP地址(随机整数ip(ip范围)))
        if ip not in 排除:
            return ip
