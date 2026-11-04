@echo off
REM ============================================================
REM YONG-NIAN-V1 — Windows Batch Installer
REM ============================================================
setlocal EnableDelayedExpansion

set "APP_DIR=%~dp0"
set "VENV_DIR=%APP_DIR%.venv"
set "PY_FILE=%APP_DIR%yong_nian_v1.py"
set "REQ_FILE=%APP_DIR%requirements.txt"

echo.
echo ============================================================
echo    YONG-NIAN-V1  -  Windows Installer
echo    Ultimate Multi-Platform Pentest Platform
echo ============================================================
echo.

REM ---- Check Python ----
where python >nul 2>nul
if errorlevel 1 (
    echo [x] Python not found on PATH. Install Python 3.8+ from python.org.
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('python --version 2^>^&1') do set "PYVER=%%v"
echo [+] Detected Python %PYVER%

REM ---- Create venv ----
if not exist "%VENV_DIR%" (
    echo [*] Creating virtual environment...
    python -m venv "%VENV_DIR%"
)
call "%VENV_DIR%\Scripts\activate.bat"

REM ---- Upgrade pip ----
python -m pip install --upgrade pip wheel setuptools

REM ---- Install deps ----
echo [*] Installing Python dependencies...
if exist "%REQ_FILE%" (
    pip install -r "%REQ_FILE%"
) else (
    echo [x] requirements.txt not found at %REQ_FILE%
    pause
    exit /b 1
)

REM ---- Sanity check ----
if not exist "%PY_FILE%" (
    echo [x] yong_nian_v1.py not found at %PY_FILE%
    pause
    exit /b 1
)

echo.
echo [+] Installation complete!
echo.
echo   Launch:
echo     call "%VENV_DIR%\Scripts\activate.bat"
echo     python "%PY_FILE%"
echo.
echo   Web dashboard: http://localhost:5000
echo.
pause
