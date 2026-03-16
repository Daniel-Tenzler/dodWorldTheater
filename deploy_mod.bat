@echo off
setlocal enabledelayedexpansion

echo Deploying dodWorldTheater mod to Victoria 2...
echo.

set "CONFIG_FILE="
set "SOURCE="
set "DEST="

REM Check for local config first (gitignored), then example config
if exist "%~dp0deploy.config.local" (
    set "CONFIG_FILE=%~dp0deploy.config.local"
    echo Using config: deploy.config.local
) else if exist "%~dp0deploy.config" (
    set "CONFIG_FILE=%~dp0deploy.config"
    echo Using config: deploy.config
) else (
    echo WARNING: No config file found!
    echo Create deploy.config.local from deploy.config.example
    echo.
    echo Using default values...
    set "SOURCE=%~dp0dodWorldTheater"
    set "DEST=D:\SteamLibrary\steamapps\common\Victoria 2\mod\dodWorldTheater"
)

REM Read config file if it exists
if defined CONFIG_FILE (
    for /f "usebackq tokens=1,2 delims==" %%a in ("%CONFIG_FILE%") do (
        REM Skip comments and empty lines
        echo %%a | findstr /r "^#" >nul
        if errorlevel 1 (
            if not "%%a"=="" (
                if "%%a"=="SOURCE" set "SOURCE=%%b"
                if "%%a"=="DEST" set "DEST=%%b"
            )
        )
    )
)

REM Convert relative SOURCE path to absolute (if not already absolute)
if defined SOURCE (
    echo %SOURCE% | findstr /r "^[A-Za-z]:.*" >nul
    if errorlevel 1 (
        set "SOURCE=%~dp0%SOURCE%"
    )
)

REM Validate paths
echo.
echo Configuration:
echo   Source: %SOURCE%
echo   Dest:   %DEST%
echo.

if not exist "%SOURCE%" (
    echo ERROR: Source directory does not exist: %SOURCE%
    echo.
    echo Please check your deploy.config.local file
    pause
    exit /b 1
)

REM Warn if DEST doesn't exist (parent directory check)
for %%F in ("%DEST%") do set "PARENT=%%~dpF"
if not exist "%PARENT%" (
    echo WARNING: Destination parent directory does not exist: %PARENT%
    echo.
)

echo Removing old mod directory...
if exist "%DEST%" (
    rmdir /s /q "%DEST%"
    if errorlevel 1 (
        echo ERROR: Failed to remove old mod directory
        echo.
        echo Possible causes:
        echo   - Victoria 2 is currently running
        echo   - Files are in use
        echo   - Insufficient permissions
        pause
        exit /b 1
    )
    echo Old mod directory removed successfully
) else (
    echo No old mod directory found, skipping removal
)

echo Copying new mod files...

REM Use robocopy for silent fast copy
REM /E    - Copy subdirectories, including empty ones
REM /NFL  - No file list
REM /NDL  - No directory list
REM /NP   - No progress (too fast to see on SSD)
REM /NJH  - No job header
REM /NJS  - No job summary
REM /R:0  - 0 retries on failure
REM /W:0  - Wait 0 seconds between retries
REM /MT   - Use multi-threaded copying (faster)
robocopy "%SOURCE%" "%DEST%" /E /NFL /NDL /NP /NJH /NJS /R:0 /W:0 /MT >nul

REM Robocopy returns various exit codes:
REM 0 = No files copied, no errors
REM 1 = Files copied successfully
REM 2 = Extra files or dirs in destination
REM 3 = Combination of 1 and 2
REM 4+ = Errors occurred
if %ERRORLEVEL% LEQ 3 (
    echo.
    echo ========================================
    echo Mod deployed successfully!
    echo ========================================
    echo.
) else (
    echo.
    echo ERROR: Deployment failed with error code %ERRORLEVEL%
    pause
    exit /b 1
)
pause
