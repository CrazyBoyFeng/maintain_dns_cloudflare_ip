from abc import ABCMeta as 抽象基类
from abc import abstractmethod as 抽象方法
from builtins import str as 字符串
from builtins import property as 属性

无 = None


class 域名解析记录(metaclass=抽象基类):
    @抽象方法
    def __init__(自身, 账户: 字符串, 密码: 字符串, 主域名: 字符串, 子域名: 字符串 = 无, 线路ip: 字符串 = 无):
        pass

    @属性
    @抽象方法
    def ip(自身) -> 字符串:
        pass

    @抽象方法
    def 修改(自身, ip: 字符串):
        pass
