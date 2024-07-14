@echo off
chcp 65001 >nul

ffmpeg -i unicode_flash_mob_1.wmv -stream_loop -1 -i DUTM.ogg -c:v libx264 -crf 18 -c:a aac -b:a 192k -shortest unicode_flash_mob.mp4
if %errorlevel% neq 0 (
    echo ffmpeg 执行失败
    pause
    exit /b
)

echo 转换完成！
pause
