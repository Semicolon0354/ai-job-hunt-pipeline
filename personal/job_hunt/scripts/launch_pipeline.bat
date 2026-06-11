@echo off
REM ─── Job Hunt Pipeline Launcher ──────────────────────────────────────────────
REM Entry point for Windows Task Scheduler (Mon-Thu at 1am).
REM Starts Ollama if not already running, then runs the full pipeline.

setlocal

REM ── Configure paths for your machine ─────────────────────────────────────────
REM If 'python' is on your PATH, leave PYTHON as-is.
REM Otherwise set it to your python.exe full path, e.g.:
REM   set "PYTHON=C:\Users\YourName\AppData\Local\Python\pythoncore-3.14-64\python.exe"
set "PYTHON=python"

REM If 'ollama' is on your PATH, leave OLLAMA_EXE as-is.
REM Otherwise set it to your ollama.exe full path, e.g.:
REM   set "OLLAMA_EXE=C:\Users\YourName\AppData\Local\Programs\Ollama\ollama.exe"
set "OLLAMA_EXE=ollama"

set "PIPELINE=%~dp0run_pipeline.py"
set "LOG=%~dp0..\logs\launcher.log"
set PYTHONIOENCODING=utf-8

REM Ensure logs directory exists
if not exist "%~dp0..\logs" mkdir "%~dp0..\logs"

REM ── Start Ollama if it's not already running ──────────────────────────────────
tasklist /FI "IMAGENAME eq ollama.exe" 2>nul | find /I "ollama.exe" >nul
if %ERRORLEVEL% neq 0 (
    echo [%date% %time%] Ollama not running -- starting it >> "%LOG%"
    start /B "" "%OLLAMA_EXE%"
    timeout /t 8 /nobreak >nul
) else (
    echo [%date% %time%] Ollama already running >> "%LOG%"
)

REM ── Run pipeline ─────────────────────────────────────────────────────────────
echo [%date% %time%] Pipeline starting >> "%LOG%"
"%PYTHON%" "%PIPELINE%"
echo [%date% %time%] Pipeline exited (code %ERRORLEVEL%) >> "%LOG%"

endlocal
