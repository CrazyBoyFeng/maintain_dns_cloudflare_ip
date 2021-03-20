from builtins import ValueError as 结果错误
from builtins import dict as 字典
from builtins import str as 字符串
from json import load as 载入json
from urllib.parse import urlencode as url编码字典
from urllib.request import Request as 网络请求
from urllib.request import urlopen as 打开网址

from .api import 域名解析记录

无 = None

请求头部 = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'maintain_dns_cloudflare_ip/0.0.1 (crazyboyfeng@qq.com)'
}


def 请求结果(请求路径: 字符串, 参数: 字典):
    网址 = 'https://dnsapi.cn/' + 请求路径
    编码 = url编码字典(参数)
    数据 = 编码.encode('utf-8')
    请求 = 网络请求(网址, 数据, 请求头部)
    答复 = 打开网址(请求)
    return 载入json(答复)


class DNSPod(域名解析记录):
    def __init__(自身, 账户: 字符串, 密码: 字符串, 主域名: 字符串, 子域名: 字符串 = 无, 线路ip: 字符串 = 无):
        super().__init__(账户, 密码, 主域名, 子域名, 线路ip)
        自身.固定参数 = {
            'login_token': '%s,%s' % (账户, 密码),
            'format': 'json',
            'lang': 'cn',
            'error_on_empty': 'yes',
            'domain': 主域名,
            'sub_domain': 子域名 or '@',
        }
        自身.记录 = {
            'value': 线路ip
        }
        自身.查询()
        pass

    def 查询(自身):
        参数 = 自身.固定参数.copy()
        参数['length'] = '1'
        参数['record_type'] = 'A'
        if 自身.记录['value']:
            参数['keyword='] = 自身.记录['value']
        json = 请求结果('Record.List', 参数)
        if json['status']['code'] != '1':
            raise 结果错误(json['status']['message'])
        记录 = json['records'][0]
        自身.记录 = {
            'record_id': 记录['id'],
            'record_line_id': 记录['line_id'],
            'value': 记录['value'],
            'record_type': 记录['record_type'],
            'mx': 字符串(记录['mx']),
            'ttl': 字符串(记录['ttl']),
        }
        pass

    def ip(自身) -> 字符串:
        return 自身.记录['value']

    def 修改(自身, ip):
        参数 = 自身.固定参数.copy()
        参数.update(自身.记录)
        参数['value'] = ip
        json = 请求结果('Record.Modify', 参数)
        if json['status']['code'] != '1':
            raise 结果错误(json['status']['message'])
        自身.记录['value'] = ip
        pass
