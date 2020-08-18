@echo OFF

pushd %~dp0

title sqlmap_wcc
color a
cls

python cdn.py
cls
py cdn.py
cls
python3 cdn.py
cls

pause >nul