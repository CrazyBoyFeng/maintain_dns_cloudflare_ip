@Echo off
:: Windows Python �ű�������
:: ���������ͣ�Բ鿴������Ϣ
SetLocal EnableDelayedExpansion
Title %~n0
CD /D "%~dp0"

python %~n0.py
Set �˳���=!ErrorLevel!
If Not "!�˳���!"=="0" (
    Echo �˳��룺!�˳���!
)
Pause
Exit !�˳���!