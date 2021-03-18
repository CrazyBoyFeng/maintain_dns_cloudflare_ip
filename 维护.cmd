@Echo off
:: Windows Python 脚本启动器
:: 结束后会暂停以便查看错误信息
SetLocal EnableDelayedExpansion
Title %~n0
CD /D "%~dp0"

Python %~n0.py
Set ExitCode=!ErrorLevel!
Echo.
If Not "!ExitCode!"=="0" (
    Echo ExitCode: !ExitCode!  1>&2
)
Pause
Exit !ExitCode!