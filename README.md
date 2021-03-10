# 维护 DNS Cloudflare IP
查找可用 Cloudflare IP 并更新域名解析记录。

目前支持的域名解析服务提供商：
* DNSPod
* 阿里云

## 如何使用
### 安装 Python 运行环境
Windows 用户可于 [Microsoft Store](https://www.microsoft.com/zh-cn/p/python-39/9p7qfqmjrfp7) 便捷安装。  

其它主流桌面操作系统一般自带 Python。  

如果没有自带，或不使用 Microsoft Store 的 Windows 用户，可于[官网](https://www.python.org/downloads)下载安装。

### 配置与执行
0. 下载[项目](https://github.com/CrazyBoyFeng/maintain_dns_cloudflare_ip/archive/main.zip)并解压至任意目录。
1. 登录你的 DNS 解析服务商，设置一个 A 类型的域名解析记录。
2. 修改`配置.ini`，按照要求填写参数。
3. 执行`维护.py`。

## 捐赠与赞助
* [支付宝](https://user-images.githubusercontent.com/1733254/110204402-bbcabc80-7ead-11eb-8bbc-9be2041214c2.png)
* [微信支付](https://user-images.githubusercontent.com/1733254/110204405-bd948000-7ead-11eb-9c8a-13094e252d7a.png)

付款代表您同意就捐赠与赞助事项与我[约定](https://gist.github.com/CrazyBoyFeng/a53994e5cfb129110c150fb6ea802a87#file-donationandsponsorshipagreement-md)。
