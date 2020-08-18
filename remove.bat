@echo OFF

title Uninstalling...
color a
cls

echo Run as administrator!

@RD /S /Q "%appdata%\sqlmap_wcc"
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "Autorun" /f

echo Done!
pause >nul