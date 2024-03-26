@ECHO OFF
echo Checking for python...
FOR /F %%i IN ('py -V ^| call lib\grep.exe -c "Python 3"') DO set /A PYTHONINSTALLED=%%i
if %PYTHONINSTALLED%==1 (
  echo Python detected!
  echo:
  goto :PYTHON_EXISTS
) else (
  echo Python not detected! Please install Python v3.10 or higher.
  echo:
  pause
  goto :EOF
)



:PYTHON_EXISTS
echo Checking for venv...
if exist venv\ (
  echo Venv already set up!
) else (
  echo Venv not found, installing...
  @ECHO ON
  py -m venv venv
  @ECHO OFF
)
echo:



echo Checking if libraries are installed...
call venv/Scripts/activate.bat
FOR /F %%i IN ('pip list --disable-pip-version-check ^| call lib\grep.exe -c Pillow') DO set /A PIPSTATUS=%%i
if %PIPSTATUS%==1 (
  echo Libraries already installed!
) else (
  echo Installing libraries...
  pip install --disable-pip-version-check -r requirements.txt
)
echo:
goto :END


:END
echo Done!
pause

