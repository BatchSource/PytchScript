@echo off&cd "%~dp0"
if "%~1"=="" (title Pytch - Console
pytch -c
) else (
title Pytch - "%~1"
pytch -r "%~1"

echo.&echo.Script has ended.
pause >nul
)
exit
