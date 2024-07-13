@echo off
cd /d "%~dp0"
chcp 65001 >nul
setlocal enabledelayedexpansion

del .\unicode.txt

echo 请将字体文件拖放到此窗口(可多个字体，中间用空格分开)，然后按回车:
set /p "fontfile="

:: 执行命令序列
@echo.
echo 使用前请将所有字体文件安装好。安装左下角字体中......
start BottomFont.ttf

.\python\python-3.12.3-embed-amd64\python.exe font.txt.py -i %fontfile%
if %errorlevel% neq 0 (
    echo font.txt.py 执行失败
    pause
    exit /b
)
@echo.
.\python\python-3.12.3-embed-amd64\python.exe unicode.txt.py
if %errorlevel% neq 0 (
    echo unicode.txt.py 执行失败
    pause
    exit /b
)
@echo.
.\python\python-3.12.3-embed-amd64\python.exe unicode.txt.blcolor.py
if %errorlevel% neq 0 (
    echo unicode.txt.blcolor.py 执行失败
    pause
    exit /b
)
@echo.
del unicode.txt
ren processed_unicode.txt unicode.txt

echo Unicode文件处理完成，请按回车继续。如果出现一个 `第 xxxx 行数据格式错误：,"blcolor"` 的内容请忽略它。
pause
@echo.
.\python\python-3.12.3-embed-amd64\python.exe ppt.py
if %errorlevel% neq 0 (
    echo ppt.py 执行失败
    pause
    exit /b
)
@echo.
echo 所有操作已完成。请到新增加的文件夹查看。
pause