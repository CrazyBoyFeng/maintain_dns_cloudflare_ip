from base64 import b64encode as base64编码
from builtins import IndexError as 索引错误
from builtins import ValueError as 结果错误
from builtins import dict as 字典
from builtins import sorted as 排序
from builtins import str as 字符串
from datetime import datetime as 日期时间
from hashlib import sha1
from hmac import new as hmac消息验证
from json import load as 载入json
from json.decoder import JSONDecodeError as Json解码错误
from urllib.error import HTTPError as Http错误
# from urllib.parse import quote_plus as url加强编码 # 空格变加号；'/'不变
from urllib.parse import quote as url编码  # 空格变 '%20'；'/' 变 '%27'
from urllib.parse import urlencode as url编码字典
from urllib.request import urlopen as 打开网址
from uuid import uuid4 as uuid4随机数

from .api import 域名解析记录

无 = None

网址 = 'https://alidns.aliyuncs.com'
请求头部 = {
    'Content-Type': 'application/x-www-form-urlencoded'
}


def 请求(签名参数: 字典) -> 字典:
    编码参数 = url编码字典(签名参数)
    数据 = 编码参数.encode('utf-8')
    try:
        答复 = 打开网址(网址, 数据)
    except Http错误 as 错误:
        try:
            结果 = 载入json(错误)['Message']
            raise 结果错误(结果)
        except Json解码错误:
            raise 结果错误(错误)
    return 载入json(答复)


class 阿里云(域名解析记录):
    def 签名参数(自身, 操作: 字符串, 参数1: 字典[字符串, 字符串] = {}, **参数2: 字符串) -> 字典:  # 计算签名,返回签名后的查询参数
        参数字典: 字典 = 自身.固定参数.copy()
        参数字典.update(参数1)
        参数字典.update(参数2)
        参数字典['Action'] = 操作
        参数字典['Timestamp'] = 日期时间.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        参数字典['SignatureNonce'] = 字符串(uuid4随机数())  # 时间戳或随机数有一个就够了，再加一个纯属脱裤子放屁
        参数列表 = 排序(参数字典.items())
        编码参数 = url编码字典(参数列表, quote_via=url编码)  # ' ' 变 '%20'
        签名请求 = ('POST'  # 难道服务器不知道请求方式需要我特别告诉它？
                + '&' + url编码('/', '')  # %27
                + '&' + url编码(编码参数, '')  # 其实可以不设置 safe 忽略，因为此处已经没有 '/'
                ).encode('utf-8')  # 对已经编码过的请求再次编码处理 '=&%' 又一次脱裤子放屁
        签名密钥 = (自身.secret + '&').encode('utf-8')  # 为什么要加个符号？
        签名摘要 = hmac消息验证(签名密钥, 签名请求, sha1).digest()  # 摘要
        参数字典['Signature'] = base64编码(签名摘要).strip()
        return 参数字典  # 其实后面发送的时候还得再编一次码

    def __init__(自身, 账户: 字符串, 密码: 字符串, 主域名: 字符串, 子域名: 字符串 = 无, 线路ip: 字符串 = 无):
        super().__init__(账户, 密码, 主域名, 子域名, 线路ip)
        自身.固定参数 = {
            'Format': 'json',
            'Version': '2015-01-09',
            'AccessKeyId': 账户,
            'SignatureMethod': 'HMAC-SHA1',
            'SignatureVersion': '1.0',
            'DomainName': 主域名,
            'Lang': 'zh',
            'Type': 'A'
        }
        自身.secret = 密码
        自身.记录 = {
            'RR': 子域名 or '@',
            'Value': 线路ip
        }
        自身.查询()
        pass

    def 查询(自身):
        参数 = 自身.签名参数(
            'DescribeDomainRecords',
            KeyWord=自身.记录['Value'],
            RRKeyWord=自身.记录['RR']
        ) if 自身.记录['Value'] else 自身.签名参数(
            'DescribeDomainRecords',
            SubDomain=自身.记录['RR'] + '.' + 自身.固定参数['DomainName']
        )
        json = 请求(参数)
        try:
            记录 = json['DomainRecords']['Record'][0]
        except 索引错误:
            raise 结果错误('子域名 查询失败')
        自身.记录 = {
            'RR': 记录['RR'],
            'RecordId': 记录['RecordId'],
            'Type': 记录['Type'],
            'Value': 记录['Value']
        }
        pass

    def ip(自身) -> 字符串:
        return 自身.记录['Value']

    def 修改(自身, ip: 字符串):
        参数 = 自身.签名参数('UpdateDomainRecord', 自身.记录, Value=ip)
        请求(参数)
        自身.记录['Value'] = ip
        pass
