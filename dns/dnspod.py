from 内置 import *
from .api import 域名解析记录
from urllib.request import urlopen as 打开网址
from json import load as 载入json
from builtins import LookupError as 查询错误
from builtins import ValueError as 结果错误


class DnsPod(域名解析记录):
    def __init__(自身, 账户: 字符串, 密码: 字符串, 域名: 字符串, 域名记录: 字符串):
        super().__init__(账户, 密码, 域名, 域名记录)
        自身.请求头 = ('login_token=%s,%s' % (账户, 密码)
                  + '&format=json'
                  + '&lang=cn'
                  + '&error_on_empty=no'
                  + '&domain=' + 域名
                  + '&sub_domain=' + 域名记录
                  )
        自身.查询()
        自身.域名记录 = 域名记录
        自身.ip = None

    def 查询(自身) -> 字符串:
        数据: 字符串 = (自身.请求头
                   + '&length=1'
                   + '&record_type=A'
                   )
        答复 = 打开网址('https://https://dnsapi.cn/Record.List', 数据.编码('utf-8'))
        json = 载入json(答复)
        if json.status.code is not '1':
            raise 查询错误(json.status.message)
        if 'record' not in 自身.请求头:
            自身.请求头 += '&record_id=' + json.records[0].id
            自身.请求头 += '&record_line_id=' + json.records[0].line_id
        自身.ip = json.records[0].value
        return 自身.ip

    def 修改(自身, ip):
        数据: 字符串 = (自身.请求头
                   + '&value=' + ip
                   )
        答复 = 打开网址('https://dnsapi.cn/Record.Ddns', 数据.编码())
        json = 载入json(答复)
        if json.status.code is not '1':
            raise 结果错误(json.status.message)
