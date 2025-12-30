@echo off
REM Movie Website - Quick Start Script for Windows

echo.
echo ============================================
echo     Movie Website - Quick Start
echo ============================================
echo.

REM Check if running from correct directory
if not exist "backend" (
    echo Error: Please run this script from the project root directory
    echo Current directory: %cd%
    pause
    exit /b 1
)

echo [1/4] Setting up Backend...
cd backend

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error creating virtual environment
        pause
        exit /b 1
    )
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing backend dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo Error installing dependencies
    pause
    exit /b 1
)

echo Backend setup complete!
echo.

echo [2/4] Setting up Frontend...
cd ..\frontend

echo Installing frontend dependencies...
call npm install
if errorlevel 1 (
    echo Error installing npm packages
    pause
    exit /b 1
)

echo Frontend setup complete!
echo.

echo ============================================
echo     Setup Complete!
echo ============================================
echo.
echo To start the application:
echo.
echo Terminal 1 (Backend):
echo   1. cd backend
echo   2. .\venv\Scripts\Activate.ps1
echo   3. python app.py
echo.
echo Terminal 2 (Frontend):
echo   1. cd frontend
echo   2. npm start
echo.
echo The application will open at: http://localhost:3000
echo.
pause
