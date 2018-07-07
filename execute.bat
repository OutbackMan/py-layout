@echo off

REM Title        execute
REM Description  Create directory structure for gnu-linux C project
REM Usage        execute -d/-r (defaults to debug) (also have .exe generator)

REM Copyright (C) 2018, Ryan McClue
REM License:
REM	This file is subject to the terms and conditions defined in
REM	'LICENSE.md', which is part of this source code package.


REM maybe introduce a pep8 linter

SET CURRENT_EXECUTE_MODE="debug"

REM add unit testing
FOR %%A IN (%*) DO (
  IF "%%A"=="/debug" SET CURRENT_EXECUTE_MODE="debug" 
  IF "%%A"=="/release" SET CURRENT_EXECUTE_MODE="release" 
)

WHERE /Q python || ECHO. Could not find python on PATH. && EXIT /B %ERRORLEVEL%
FOR /F "tokens=* USEBACKQ" %%F IN (
  `python -c "import sys; print(''.join(map(str, sys.version_info[:3])))"`
) DO (
SET PYTHON_VERSION=%%F
)

IF %PYTHON_VERSION% LSS	370 echo. Python version is too low. && EXIT /B %ERRORLEVEL% 

WHERE /Q mypy || ECHO. Could not find mypy on PATH. && EXIT /B %ERRORLEVEL%


IF %CURRENT_EXECUTE_MODE%=="debug" (
  mypy ui.py || python -mpdb ui.py
) ELSE (
  mypy ui.py || python -OO ui.py
)

EXIT /B %ERRORLEVEL%
