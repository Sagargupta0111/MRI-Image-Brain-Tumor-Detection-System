@echo off
REM Complete setup script for MRI Tumor Detection System

echo.
echo ============================================
echo MRI Tumor Detection System - Complete Setup
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    echo Virtual environment created!
) else (
    echo [1/4] Virtual environment already exists
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies from requirements.txt...
pip install -r requirements.txt --quiet

echo.
echo [4/4] Creating MRI tumor detection model...
python create_model.py

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo To run the application:
echo   1. Open PowerShell in this directory
echo   2. Run: .\venv\Scripts\Activate.ps1
echo   3. Run: python main.py
echo.
echo The app will be available at: http://127.0.0.1:5000
echo.
pause
