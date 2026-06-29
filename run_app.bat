@echo off
cd /d "%~dp0"
REM Use project virtualenv python if available, otherwise fallback to system python
if exist "%~dp0\.venv\Scripts\python.exe" (
	"%~dp0\.venv\Scripts\python.exe" app.py >> "%~dp0\startup.log" 2>&1
) else (
	"C:\Users\admin\AppData\Local\Programs\Python\Python314\python.exe" app.py >> "%~dp0\startup.log" 2>&1
)
