@Echo off
:: Windows Python 脚本启动器
:: 结束后会暂停以查看错误信息
SetLocal EnableDelayedExpansion
Title %~n0
CD /D "%~dp0"

python %~n0.py
Set 退出码=!ErrorLevel!
If Not "!退出码!"=="0" (
    Echo 退出码：!退出码!
)
Pause
Exit !退出码!