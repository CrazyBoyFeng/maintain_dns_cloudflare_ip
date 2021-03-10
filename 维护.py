#!/usr/bin/env python

# 咱试试用中文写代码，反正开发者和用户都是中文使用者。
# 这样可以不用写注释，沟通效率也更高。
from builtins import ValueError as 结果错误
from builtins import print as 提示
from builtins import str as 字符串
from builtins import int as 整数
from time import sleep as 挂起
from datetime import datetime as 日期时间
import dns
import cloudflare
import ip
from sys import path as 路径
from configparser import ConfigParser as 配置解析
路径.append('.')

是 = True


class 配置项:
    配置解析.读取 = 配置解析.read
    配置解析.取 = 配置解析.get
    配置解析.取整数 = 配置解析.getint
    配置解析.取判断 = 配置解析.getboolean

    def __init__(自身, 文件: 字符串 = '配置.ini'):
        配置 = 配置解析()
        配置.读取(文件, 'utf-8')
        自身.dns = 配置.取('维护', 'dns')
        自身.间隔 = 配置.取整数('维护', '间隔')
        自身.响应超时 = 配置.取整数('维护', '响应超时')
        自身.强制更新 = 配置.取判断('维护', '强制更新')
        自身.账户 = 配置.取('DNS', '账户')
        自身.密码 = 配置.取('DNS', '密码')
        域名 = 配置.取('DNS', '域名')
        域名记录 = 配置.取('DNS', '域名记录')
        自身.域名 = 域名 or 域名记录
        自身.域名记录 = 域名记录 or 域名
        pass


def 域名解析服务(解析服务: 字符串, 账户: 字符串, 密码: 字符串, 域名: 字符串, 域名记录: 字符串):
    提示('解析服务', 解析服务)
    if 'DNSPod' in 解析服务:
        return dns.DNSPod(账户, 密码, 域名, 域名记录)
    # if '阿里' in 解析服务:
    #     return dns.阿里云(账户, 密码, 域名, 域名记录)
    raise 结果错误('不支持域名解析服务提供商')
    pass


def 选取ip(网络地址: 字符串, 响应超时: 整数) -> 字符串:
    无效列表 = [网络地址]
    while 网络地址 in 无效列表:
        网络地址 = ip.随机ipv4(无效列表)
        提示('随机地址', 网络地址)
        if not cloudflare.检测有效(网络地址, 响应超时):
            无效列表.append(网络地址)
    提示('检测有效', 网络地址)
    return 网络地址


def 维护(配置: 配置项):
    域名解析 = 域名解析服务(配置.dns, 配置.账户, 配置.密码, 配置.域名, 配置.域名记录)
    域名记录, 网络地址 = 域名解析.查询()
    提示('域名记录', 域名记录)
    提示('当前地址', 网络地址)
    if (not 配置.强制更新) and cloudflare.检测有效(网络地址, 配置.响应超时):
        return
    网络地址 = 选取ip(网络地址, 配置.响应超时)
    提示('修改地址', 网络地址)
    域名解析.修改(网络地址)
    pass


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
