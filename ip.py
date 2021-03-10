from builtins import int as 整数
from builtins import list as 列表
from builtins import str as 字符串
from ipaddress import IPv4Network as IPv4网络
from ipaddress import ip_address as IP地址
from ipaddress import ip_network as IP网络
from random import choices as 选择
from random import randint as 随机整数

是 = True

IPv4网络.地址数量 = IPv4网络.num_addresses

ipv4范围列表 = [
    IP网络('173.245.48.0/20'),
    IP网络('103.21.244.0/22'),
    IP网络('103.22.200.0/22'),
    IP网络('103.31.4.0/22'),
    IP网络('141.101.64.0/18'),
    IP网络('108.162.192.0/18'),
    IP网络('190.93.240.0/20'),
    IP网络('188.114.96.0/20'),
    IP网络('197.234.240.0/22'),
    IP网络('198.41.128.0/17'),
    IP网络('162.158.0.0/15'),
    IP网络('104.16.0.0/12'),
    IP网络('172.64.0.0/13'),
    IP网络('131.0.72.0/22')
]


def cidr数量(cidr列表: 列表[IP网络]) -> 列表:
    数量列表 = []
    for ip网络 in cidr列表:
        数量列表.append(ip网络.地址数量)
    return 数量列表


ipv4范围数量列表 = cidr数量(ipv4范围列表)


def 随机ip(cidr: IP网络) -> 字符串:
    return 字符串(IP地址(随机整数(整数(cidr[0]), 整数(cidr[-1]))))


def 随机ipv4(排除: 列表[字符串]) -> 字符串:
    while 是:
        ip = 随机ip(选择(ipv4范围列表, ipv4范围数量列表)[0])
        if ip not in 排除:
            return ip
    pass