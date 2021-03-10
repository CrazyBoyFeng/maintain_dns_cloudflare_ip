from abc import ABCMeta as 抽象基类
from abc import abstractmethod as 抽象方法
from builtins import str as 字符串


class 域名解析记录(metaclass=抽象基类):
    @抽象方法
    def __init__(自身, 账户, 密码, 域名, 域名记录):
        pass

    域名记录: 字符串
    ip: 字符串

    @抽象方法
    def 修改(自身, ip):
        pass
