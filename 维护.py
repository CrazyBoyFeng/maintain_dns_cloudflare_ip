#!/usr/bin/env python
from builtins import ValueError as 结果错误
from builtins import print as 提示
from builtins import str as 字符串
from time import sleep as 挂起
from datetime import datetime as 日期时间
import dns
import cloudflare
import ipv4
from 组件 import *


class 配置项:
    def __init__(自身, 文件: 字符串 = '配置.ini'):
        配置 = 配置解析()
        配置.读取(文件, 'utf-8')
        自身.dns = 配置.取('维护', 'dns')
        自身.间隔 = 配置.取整数('维护', '间隔')
        自身.强制更新 = 配置.取判断('维护', '强制更新')
        自身.账户 = 配置.取('DNS', '账户')
        自身.密码 = 配置.取('DNS', '密码')
        域名 = 配置.取('DNS', '域名')
        域名记录 = 配置.取('DNS', '域名记录')
        自身.域名 = 域名 or 域名记录
        自身.域名记录 = 域名记录 or 域名


def 域名解析服务(解析服务: 字符串, 账户: 字符串, 密码: 字符串, 域名: 字符串, 域名记录: 字符串):
    提示('解析服务', 解析服务)
    if 'DNSPod' in 解析服务:
        return dns.DNSPod(账户, 密码, 域名, 域名记录)
    # if '阿里' in 解析服务:
    #     return dns.阿里云(账户, 密码, 域名, 域名记录)
    raise 结果错误('不支持域名解析服务提供商')


def 选取ip(ip: 字符串) -> 字符串:
    无效列表 = [ip]
    while ip in 无效列表:
        ip = ipv4.随机ip(无效列表)
        提示('随机地址', ip)
        if cloudflare.检测有效(ip):
            break
        else:
            无效列表.append(ip)
    提示('检测有效', ip)
    return ip


def 维护(配置: 配置项):
    域名解析 = 域名解析服务(配置.dns, 配置.账户, 配置.密码, 配置.域名, 配置.域名记录)
    域名记录, ip = 域名解析.查询()
    提示('域名记录', 域名记录)
    提示('当前地址', ip)
    if (not 配置.强制更新) and cloudflare.检测有效(ip):
        return
    ip = 选取ip(ip)
    提示('修改地址', ip)
    域名解析.修改(ip)


while 是:
    提示("当前时间", 日期时间.now())
    配置 = 配置项()
    try:
        维护(配置)
    except 结果错误 as 错误:
        提示(错误)
    提示(配置.间隔, '秒后将再次执行')
    挂起(配置.间隔)
    提示()
