@ECHO OFF

FOR /F %%i IN ('py -V ^| call lib\grep.exe -c "Python 3"') DO set /A PYTHONINSTALLED=%%i
if %PYTHONINSTALLED%==1 (
  goto :PYTHON_EXISTS
) else (
  echo Python not detected! Please install Python v3.9 or higher.
  goto :EOF
)
  
:PYTHON_EXISTS
if exist venv\ (
  start "SBSBatchExporter" cmd /k call "%~dp0venv/scripts/activate.bat"
) else (
  echo Venv not found!
  echo Please run install.bat to install the required environment.
  pause
)


