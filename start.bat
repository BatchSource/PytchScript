@echo off&cd "%~dp0"
if "%~1"=="" (title Pytch - Console
python pytch.py -c
) else (
title Pytch - "%~1"
python pytch.py -r "%~1"

echo.&echo.Script has ended.
pause >nul
)
exit