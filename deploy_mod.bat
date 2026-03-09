@echo off
echo Deploying dodWorldTheater mod to Victoria 2...

set SOURCE=%~dp0dodWorldTheater
set DEST=G:\SteamLibrary\steamapps\common\Victoria 2\mod\dodWorldTheater

echo Removing old mod directory...
if exist "%DEST%" (
    rmdir /s /q "%DEST%"
    if errorlevel 1 (
        echo ERROR: Failed to remove old mod directory
        pause
        exit /b 1
    )
    echo Old mod directory removed successfully
) else (
    echo No old mod directory found, skipping removal
)

echo.
echo Copying new mod files...
xcopy "%SOURCE%" "%DEST%" /E /I /H /Y
if errorlevel 1 (
    echo ERROR: Failed to copy mod files
    pause
    exit /b 1
)

echo.
echo Mod deployed successfully to:
echo %DEST%
echo.
pause
