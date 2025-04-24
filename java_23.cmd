@echo off
set "SCRIPT_DIR=%~dp0"
echo "SCRIPT_DIR=%SCRIPT_DIR%"

if not defined SHELL (
    echo SHELL not set
    for /f "tokens=*" %%a in ('python %SCRIPT_DIR%set_java.py java23') do (
        %%a
    )
    echo Java environment updated to Java 23
) else (
    echo SHELL is set to %SHELL%
)

