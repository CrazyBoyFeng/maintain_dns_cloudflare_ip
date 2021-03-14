# 咱试试用中文写代码，反正开发者和用户都是中文使用者。
# 这样可以不用写注释，沟通效率也更高。
from builtins import IOError as 传输错误
from builtins import ValueError as 结果错误
from builtins import int as 整数
from builtins import print as 提示
from builtins import str as 字符串
from builtins import bool as 判断
from configparser import ConfigParser as 配置解析
from datetime import datetime as 日期时间
from os import chdir as 改变目录
from sys import path as 路径
from sys import stderr as 错误输出
from time import sleep as 挂起
from socket import gethostbyname as 取域名ip

import dns
import cloudflare
import ip

是 = True

改变目录(路径[0])
路径.append('.')


class 维护配置:
    配置解析.读取 = 配置解析.read
    配置解析.取 = 配置解析.get
    配置解析.取整数 = 配置解析.getint
    配置解析.取判断 = 配置解析.getboolean

    def __init__(自身, 文件: 字符串 = '配置.ini'):
        配置参数 = 配置解析()
        配置参数.读取(文件, 'utf-8')
        自身.dns = 配置参数.取('维护', 'dns')
        自身.间隔 = 配置参数.取整数('维护', '间隔')
        自身.响应超时 = 配置参数.取整数('维护', '响应超时')
        自身.强制更新 = 配置参数.取判断('维护', '强制更新')
        自身.解析线路 = 配置参数.取判断('维护', '解析线路')
        自身.账户 = 配置参数.取('DNS', '账户')
        自身.密码 = 配置参数.取('DNS', '密码')
        自身.主域名 = 配置参数.取('DNS', '主域名')
        自身.子域名 = 配置参数.取('DNS', '子域名')
        pass


def 域名解析服务(解析服务: 字符串, 账户: 字符串, 密码: 字符串, 主域名: 字符串, 子域名: 字符串, 线路ip: 字符串):
    提示('解析服务', 解析服务)
    if 'DNSPod' in 解析服务:
        return dns.DNSPod(账户, 密码, 主域名, 子域名, 线路ip)
    if '阿里' in 解析服务:
        return dns.阿里云(账户, 密码, 主域名, 子域名, 线路ip)
    raise 结果错误('不支持的域名解析服务提供商')
    pass


def 选取ip(当前ip: 字符串, 响应超时: 整数) -> 字符串:
    无效ip列表 = [当前ip]
    while 当前ip in 无效ip列表:
        当前ip = ip.随机ipv4(无效ip列表)
        提示('随机地址', 当前ip, end=' ', flush=是)
        if not cloudflare.检测有效(当前ip, 响应超时):
            提示('检测无效')
            无效ip列表.append(当前ip)
    提示('检测有效')
    return 当前ip


def 维护(强制更新: 判断, 响应超时: 判断):
    提示("当前时间", 日期时间.now())
    if not 强制更新:
        提示('当前地址', 域名解析.ip, end=' ', flush=是)
        if cloudflare.检测有效(域名解析.ip(), 响应超时):
            提示('检测有效')
            return
        提示('检测无效')
    随机有效ip = 选取ip(域名解析.ip(), 响应超时)
    提示('更新地址', 随机有效ip, end=' ', flush=是)
    域名解析.修改(随机有效ip)
    提示('执行完毕')
    pass


配置 = 维护配置()
域名记录 = 配置.主域名
if 配置.子域名:
    域名记录 = 配置.子域名 + '.' + 域名记录
提示('域名记录', 域名记录)
线路地址 = ''
if 配置.解析线路:
    线路地址 = 取域名ip(域名记录)
    提示('所在线路', 线路地址)
域名解析 = 域名解析服务(配置.dns, 配置.账户, 配置.密码, 配置.主域名, 配置.子域名, 线路地址)
提示()
while 是:
    try:
        维护(配置.强制更新, 配置.响应超时)
    except (结果错误, 传输错误) as 错误:  # TODO 也许还需要捕获 系统错误 和 超时错误？
        提示(错误, file=错误输出)
    提示()
    提示('下次执行', 配置.间隔, '秒后', end='\r')
    挂起(配置.间隔)
