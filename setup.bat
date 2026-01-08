@echo off
REM Setup script for MRI Tumor Detection System

echo ============================================
echo MRI Tumor Detection System - Setup Script
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created!
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete! To run the application:
echo 1. Run: venv\Scripts\activate.bat
echo 2. Run: python main.py
echo.
echo The app will be available at: http://127.0.0.1:5000
echo.
pause
