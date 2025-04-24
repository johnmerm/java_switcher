Write-Output "Inside PS"

$JavaVersion = $args[0]

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
Write-Output "SCRIPT_DIR=$SCRIPT_DIR"

if (-not $env:SHELL) {
    Write-Output "SHELL not set"

    $output = python "$SCRIPT_DIR\set_java.py" $JavaVersion
    foreach ($line in $output) {
        Invoke-Expression $line
    }
    Write-Output "Java environment updated to $JavaVersion"
} else {
    Write-Output "SHELL is set to $($env:SHELL)"
}