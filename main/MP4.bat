@echo off
chcp 65001 >nul

REM 1.将 GIF 转换为 MP4
ffmpeg -i unicode_flash_mob_1.gif -movflags faststart -pix_fmt yuv420p -vf "fps=12" temp_output.mp4 -stats
if %errorlevel% neq 0 (
    echo ffmpeg 执行失败
    pause
    exit /b
)
REM 2.将音频添加到 MP4
ffmpeg -stream_loop -1 -i DUTM.ogg -i temp_output.mp4 -c:v copy -c:a aac -shortest unicode_flash_mob.mp4 -stats

REM 删除临时文件
del temp_output.mp4

echo 转换完成！
pause