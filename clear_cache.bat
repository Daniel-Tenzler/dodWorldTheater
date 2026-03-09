@echo off
echo ========================================
echo Victoria 2 Cache Clearer
echo ========================================
echo.

set GAME_DIR=G:\SteamLibrary\steamapps\common\Victoria 2
set USER_DIR=C:\Users\%USERNAME%\Documents\Paradox Interactive\Victoria II

echo Checking for cache folders...
echo.

REM Check game installation directory
if exist "%GAME_DIR%\cache" (
    echo Found cache in game directory: %GAME_DIR%\cache
    echo Deleting...
    rmdir /s /q "%GAME_DIR%\cache"
    echo Cache deleted from game directory.
    echo.
)

REM Check map cache
if exist "%GAME_DIR%\map\cache" (
    echo Found map cache: %GAME_DIR%\map\cache
    echo Deleting...
    rmdir /s /q "%GAME_DIR%\map\cache"
    echo Map cache deleted.
    echo.
)

REM Check user documents directory
if exist "%USER_DIR%" (
    echo Checking user directory: %USER_DIR%
    for /d %%D in ("%USER_DIR%\cache*") do (
        echo Found cache folder: %%D
        echo Deleting...
        rmdir /s /q "%%D"
        echo Deleted.
    )
    echo.
)

REM Check for gfx cache files
if exist "%GAME_DIR%\gfx\flags\cache" (
    echo Found flag cache: %GAME_DIR%\gfx\flags\cache
    echo Deleting...
    rmdir /s /q "%GAME_DIR%\gfx\flags\cache"
    echo Flag cache deleted.
    echo.
)

echo ========================================
echo Cache clearing complete!
echo ========================================
echo.
echo IMPORTANT: Start a NEW game - do NOT load old saves!
echo Old saves will not work correctly with the new goods.
echo.
pause
