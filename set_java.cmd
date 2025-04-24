@echo off

set "SCRIPT_DIR=%~dp0"
echo "Inside CMD SCRIPT_DIR=%SCRIPT_DIR% for %1"

if not defined SHELL (
    rem echo SHELL not set
    for /f "tokens=*" %%a in ('python %SCRIPT_DIR%set_java.py %1') do (
        %%a
    )
    echo Java environment updated to %1
) else (
    echo SHELL is set to %SHELL%
)

