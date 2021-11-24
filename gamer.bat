@echo off
color a
title Action Refresh

if _%1_==_payload_  goto :payload

:getadmin
    echo %~nx0: elevating self
    set vbs=%temp%\getadmin.vbs
    echo Set UAC = CreateObject^("Shell.Application"^)                >> "%vbs%"
    echo UAC.ShellExecute "%~s0", "payload %~sdp0 %*", "", "runas", 1 >> "%vbs%"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
goto :eof

:payload
cls
ECHO Super Cool Automatic Basic Program Installer version 2.1
ECHO This Software is in Development! Use at Your Own Risk!!!
ECHO Please Contact Your Local Leo for More Information!
ECHO -
PAUSE
ECHO -
SET PATH=C:
set drive=%~dp0


ECHO Running Personalization Script
"%drive%\PersonalizationSetup.reg"

ECHO Installing Chrome and VLC
"%drive%\classic.exe"

ECHO Installing Acrobat Reader
"%drive%\AcrobatReader.exe"
ECHO AdwCleaner Scans Complete

INSTALLS COMPLETE
Pause





