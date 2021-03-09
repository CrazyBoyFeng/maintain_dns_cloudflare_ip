#!/usr/bin/env python
from builtins import ValueError as 结果错误
from builtins import print as 输出
from builtins import str as 字符串
from time import asctime as 标准时间
from time import localtime as 本地时间
from time import sleep as 挂起
from time import time as 时间
import dns
import cloudflare
import ipv4
from 组件 import *


class 配置项:
    def __init__(自身, 文件: 字符串 = '配置.ini'):
        配置 = 配置解析()
        配置.读取(文件, 'utf-8')
        自身.dns = 配置.取('维护', 'dns')
        自身.域名记录 = 配置.取('DNS', '域名记录')
        自身.域名 = 配置.取('DNS', '域名')
        自身.账户 = 配置.取('DNS', '账户')
        自身.密码 = 配置.取('DNS', '密码')
        自身.间隔 = 配置.取整数('维护', '间隔')
        自身.强制更新 = 配置.取判断('维护', '强制更新')


def 域名解析服务(域名解析服务提供商: 字符串, 账户: 字符串, 密码: 字符串, 域名: 字符串, 域名记录: 字符串):
    输出('域名解析服务提供商', 域名解析服务提供商)
    if 'DNSPod' in 域名解析服务提供商:
        return dns.DNSPod(账户, 密码, 域名, 域名记录)
    # if '阿里' in 域名解析服务提供商:
    #     return dns.阿里云(账户, 密码, 域名, 域名记录)
    raise 结果错误


def 选取ip(原ip: 字符串) -> 字符串:
    ip = 无
    无效 = 是
    while 无效:
        ip = ipv4.随机ip(原ip)
        输出('随机地址', ip)
        无效 = not cloudflare.检测有效(ip)
    输出('检测有效！')
    return ip


def 维护(配置: 配置项):
    域名解析 = 域名解析服务(配置.dns, 配置.账户, 配置.密码, 配置.域名, 配置.域名记录)
    域名记录, ip = 域名解析.查询()
    输出('域名记录', 域名记录)
    输出('当前地址', ip)
    if not 配置.强制更新:
        if cloudflare.检测有效(ip):
            return
    ip = 选取ip(ip)
    域名解析.修改(ip)


while 是:
    现在 = 标准时间(本地时间(时间()))
    输出("当前时间", 现在)
    输出('读取配置')
    配置 = 配置项()
    try:
        维护(配置)
    except 结果错误 as 错误:
        输出(错误)
    挂起(配置.间隔)
    输出(配置.间隔, '秒后再次尝试')
