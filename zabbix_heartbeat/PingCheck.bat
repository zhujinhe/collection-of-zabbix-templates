@echo off
::filename:PingCheck.bat
::%1 is the first parameter of the script.
::CLIUsage:PingCheck.bat 10.10.10.14

setlocal enabledelayedexpansion

for /f "tokens=1,2 delims=(%%" %%a in ('ping -n 2 %1^|find "%%"') do (
   if not defined packet_loss_rate set packet_loss_rate=%%b
)
echo !packet_loss_rate!