@echo off
setlocal

set "current_dir=%~dp0"
set "current_dir=%current_dir:~0,-1%"

start "" "%current_dir%\Application\chrome.exe" --user-data-dir="%current_dir%\User Data" --disk-cache-dir="%current_dir%\cache" --disk-cache-size=51200000

endlocal
exit