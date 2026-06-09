@echo off
REM ─── Job Hunt Pipeline Launcher ──────────────────────────────────────────────
REM Entry point for Windows Task Scheduler (Mon-Fri at midnight).
REM Starts Ollama if not already running, then runs the full pipeline.

setlocal

set "PYTHON=C:\Users\jdhum\AppData\Local\Python\pythoncore-3.14-64\python.exe"
set "PIPELINE=%~dp0run_pipeline.py"
set "LOG=%~dp0..\logs\launcher.log"
set PYTHONIOENCODING=utf-8

REM Ensure logs directory exists
if not exist "%~dp0..\logs" mkdir "%~dp0..\logs"

REM ── Start Ollama if it's not already running ──────────────────────────────────
tasklist /FI "IMAGENAME eq ollama.exe" 2>nul | find /I "ollama.exe" >nul
if %ERRORLEVEL% neq 0 (
    echo [%date% %time%] Ollama not running -- starting it >> "%LOG%"
    start /B "" "C:\Users\jdhum\AppData\Local\Programs\Ollama\ollama.exe"
    timeout /t 8 /nobreak >nul
) else (
    echo [%date% %time%] Ollama already running >> "%LOG%"
)

REM ── Run pipeline ─────────────────────────────────────────────────────────────
echo [%date% %time%] Pipeline starting >> "%LOG%"
"%PYTHON%" "%PIPELINE%"
echo [%date% %time%] Pipeline exited (code %ERRORLEVEL%) >> "%LOG%"

endlocal
