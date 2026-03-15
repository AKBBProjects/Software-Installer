
@echo off
title Software Installer

echo ==========================================
echo Software Installer
echo Build by AKBBProject
echo Published by ComputerPoint
echo ==========================================
echo.

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed.
    echo Installing Python...
    winget install -e --id Python.Python.3.11
)

echo Starting Software Installer...
python software_installer.py
pause
