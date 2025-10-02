@echo off
REM Simple launcher script for the Brain Training Game (Windows)

echo Starting Brain Training Game...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% equ 0 (
    python brain_training_game.py
) else (
    echo Error: Python is not installed!
    echo Please install Python 3.6 or higher to play this game.
    pause
    exit /b 1
)
