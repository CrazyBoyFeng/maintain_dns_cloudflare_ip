from builtins import ValueError as 结果错误
from builtins import str as 字符串
from json import load as 载入json
from typing import Tuple as 元组
from urllib.request import urlopen as 打开网址
from urllib.request import Request as 网络请求
from .api import 域名解析记录

无 = None

请求头部 = {
    'User-Agent': 'maintain_dns_cloudflare_ip/0.0.1 (crazyboyfeng@qq.com)'
}


def 请求结果(请求路径: 字符串, 参数: 字符串):
    网址 = 'https://dnsapi.cn/' + 请求路径
    数据 = 参数.encode('utf-8')
    请求 = 网络请求(网址, 数据, 请求头部)
    答复 = 打开网址(请求)
    return 载入json(答复)


class DNSPod(域名解析记录):
    def __init__(自身, 账户: 字符串, 密码: 字符串, 域名: 字符串, 域名记录: 字符串):
        super().__init__(账户, 密码, 域名, 域名记录)
        自身.参数 = (
                'login_token=%s,%s' % (账户, 密码)
                + '&format=json'
                + '&lang=cn'
                + '&error_on_empty=no'
                + '&domain=' + 域名
                + '&sub_domain=' + 域名记录
        )
        自身.域名记录 = 域名记录
        自身.ip = 无
        自身.查询()

    def 查询(自身) -> 元组[字符串, 字符串]:
        参数 = 自身.参数 + '&length=1' + '&record_type=A'
        json = 请求结果('Record.List', 参数)
        if json['status']['code'] != '1':
            raise 结果错误(json['status']['message'])
        if 'record' not in 自身.参数:
            自身.参数 += '&record_id=' + json.records[0].id
            自身.参数 += '&record_line_id=' + json.records[0].line_id
        自身.ip = json['records'][0]['value']
        return 自身.域名记录, 自身.ip

    def 修改(自身, ip):
        参数 = 自身.参数 + '&value=' + ip
        json = 请求结果('Record.Ddns', 参数)
        if json['status']['code'] != '1':
            raise 结果错误(json['status']['message'])
