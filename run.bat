if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0" %*
goto :EOF

:minimized

title Scheduled Death Announcer

python scheduled_death_announcer.py