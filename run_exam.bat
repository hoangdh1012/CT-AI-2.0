@echo off
REM Navigate to the directory where this batch file is located
cd /d "%~dp0"

REM Activate virtual environment if it exists, otherwise use system Python
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
    python istqb_exam_v2.py
) else (
    REM Fallback to system Python if virtual environment doesn't exist
    python istqb_exam_v2.py
)

pause
