@Echo off
:: Windows Python �ű�������
:: ���������ͣ�Բ鿴������Ϣ
SetLocal EnableDelayedExpansion
Title %~n0
CD /D "%~dp0"

Python %~n0.py
Set �˳���=!ErrorLevel!
Echo.
If Not "!�˳���!"=="0" (
    Echo �˳��룺!�˳���!  1>&2
)
Pause
Exit !�˳���!