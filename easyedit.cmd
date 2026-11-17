@echo off
rem Windows launcher for easyedit.
cd /d "%~dp0"
if exist "%~dp0.venv\Scripts\python.exe" (
  "%~dp0.venv\Scripts\python.exe" -m easyedit %*
  exit /b %ERRORLEVEL%
)
where python3.12 >nul 2>&1 && (
  python3.12 -m easyedit %*
  exit /b %ERRORLEVEL%
)
py -3.12 --version >nul 2>&1 && (
  py -3.12 -m easyedit %*
  exit /b %ERRORLEVEL%
)
py -3 -c "import sys; sys.exit(sys.version_info < (3, 10))" >nul 2>&1 && (
  py -3 -m easyedit %*
  exit /b %ERRORLEVEL%
)
python -c "import sys; sys.exit(sys.version_info < (3, 10))" >nul 2>&1 && (
  python -m easyedit %*
  exit /b %ERRORLEVEL%
)
echo easyedit needs Python 3.10 or newer. Install one from https://www.python.org/downloads/ and run this again. 1>&2
exit /b 1
