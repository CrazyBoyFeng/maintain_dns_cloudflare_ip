# 咱试试用中文写代码，反正开发者和用户都是中文使用者。
# 这样可以不用写注释，沟通效率也更高。

from builtins import str as 字符串
from configparser import ConfigParser as 配置解析
from http.client import HTTPResponse as Http答复
from urllib.request import Request as 网络请求

字符串.小写 = 字符串.lower
字符串.编码 = 字符串.encode

配置解析.读取 = 配置解析.read
配置解析.取 = 配置解析.get
配置解析.取整数 = 配置解析.getint

网络请求.添加包头 = 网络请求.add_header
Http答复.状态 = Http答复.getcode

无 = None
是 = True
否 = False

# 翻译完毕
