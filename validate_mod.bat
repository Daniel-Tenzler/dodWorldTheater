@echo off
setlocal EnableExtensions EnableDelayedExpansion

echo === Victoria 2 Mod Validator ===
echo.

set /a ERRORS=0
set /a WARNINGS=0

REM Check if we're in the right directory
if not exist "dodWorldTheater.mod" (
    echo [ERROR] dodWorldTheater.mod not found in current directory
    echo Please run this script from the parent directory ^(where dodWorldTheater.mod is located^)
    exit /b 1
)

set "MOD_DIR=dodWorldTheater"

if not exist "%MOD_DIR%\" (
    echo [ERROR] dodWorldTheater\ directory not found
    exit /b 1
)

echo [OK] Found dodWorldTheater.mod and dodWorldTheater/ directory
echo.

echo Checking brace balance...
if exist "%MOD_DIR%\events\*.txt" (
    for %%F in ("%MOD_DIR%\events\*.txt") do call :CheckBraceBalance "%%~fF"
)
if exist "%MOD_DIR%\decisions\*.txt" (
    for %%F in ("%MOD_DIR%\decisions\*.txt") do call :CheckBraceBalance "%%~fF"
)
if exist "%MOD_DIR%\common\on_actions.txt" (
    call :CheckBraceBalance "%MOD_DIR%\common\on_actions.txt"
)
if %ERRORS%==0 (
    echo   [OK] All braces balanced
)
echo.

echo Checking spaces around =...
set "BAD_FILES="
if exist "%MOD_DIR%\events\*.txt" (
    for /f "usebackq delims=" %%L in (`powershell -NoProfile -Command "$m = Select-String -Path '%MOD_DIR%/events/*.txt' -Pattern '\S=\S' -ErrorAction SilentlyContinue | Select-Object -First 5; if ($m) { $m | ForEach-Object { '{0}:{1}: {2}' -f $_.Path,$_.LineNumber,$_.Line.Trim() } }"`) do (
        set "BAD_FILES=1"
        if not defined PRINTED_BAD_HEADER echo   [WARN] Lines without spaces around =:
        set "PRINTED_BAD_HEADER=1"
        echo %%L
    )
)
if not defined BAD_FILES if exist "%MOD_DIR%\decisions\*.txt" (
    for /f "usebackq delims=" %%L in (`powershell -NoProfile -Command "$m = Select-String -Path '%MOD_DIR%/decisions/*.txt' -Pattern '\S=\S' -ErrorAction SilentlyContinue | Select-Object -First 5; if ($m) { $m | ForEach-Object { '{0}:{1}: {2}' -f $_.Path,$_.LineNumber,$_.Line.Trim() } }"`) do (
        set "BAD_FILES=1"
        if not defined PRINTED_BAD_HEADER echo   [WARN] Lines without spaces around =:
        set "PRINTED_BAD_HEADER=1"
        echo %%L
    )
)
if defined BAD_FILES (
    set /a WARNINGS+=1
) else (
    echo   [OK] All = have proper spacing
)
set "PRINTED_BAD_HEADER="
echo.

echo Checking for duplicate event IDs...
set "DUP_FOUND="
if exist "%MOD_DIR%\events\*.txt" (
    for /f "usebackq delims=" %%L in (`powershell -NoProfile -Command "$ids = Select-String -Path '%MOD_DIR%/events/*.txt' -Pattern '^\s*id\s*=\s*\d+' -ErrorAction SilentlyContinue | ForEach-Object { [regex]::Match($_.Line,'\d+').Value }; $dups = $ids | Group-Object | Where-Object { $_.Count -gt 1 }; if ($dups) { $dups | ForEach-Object { 'id = ' + $_.Name } }"`) do (
        if not defined DUP_FOUND echo   [ERROR] Duplicate event IDs found:
        set "DUP_FOUND=1"
        echo %%L
    )
)
if defined DUP_FOUND (
    set /a ERRORS+=1
) else (
    echo   [OK] No duplicate event IDs
)
echo.

echo Checking event ID ranges...
set "RESERVED_CONFLICTS="
if exist "%MOD_DIR%\events\*.txt" (
    for /f "usebackq delims=" %%L in (`powershell -NoProfile -Command "$m = Select-String -Path '%MOD_DIR%/events/*.txt' -Pattern '^\s*id\s*=\s*(1\d{4}|2\d{4})\b' -ErrorAction SilentlyContinue | Select-Object -First 3; if ($m) { $m | ForEach-Object { $_.Line.Trim() } }"`) do (
        if not defined RESERVED_CONFLICTS echo   [WARN] Events in vanilla/HPM range ^(10000-29999^):
        set "RESERVED_CONFLICTS=1"
        echo %%L
    )
)
if defined RESERVED_CONFLICTS set /a WARNINGS+=1

set "VANILLA=0"
if exist "%MOD_DIR%\events\*.txt" (
    for /f %%N in ('powershell -NoProfile -Command "$count = 0; Select-String -Path '%MOD_DIR%/events/*.txt' -Pattern '^\s*id\s*=\s*\d+' -ErrorAction SilentlyContinue | ForEach-Object { $id = [int]([regex]::Match($_.Line,'\d+').Value); if ($id -ge 1 -and $id -le 9999) { $count++ } }; $count"') do set "VANILLA=%%N"
)
if %VANILLA% GTR 0 (
    echo   [WARN] %VANILLA% events use vanilla ID range ^(1-9999^)
    set /a WARNINGS+=1
)
echo.

echo Checking required files...
for %%F in (
    "%MOD_DIR%\common\countries.txt"
    "%MOD_DIR%\common\defines.lua"
    "%MOD_DIR%\common\buildings.txt"
    "%MOD_DIR%\common\goods.txt"
    "%MOD_DIR%\common\cb_types.txt"
    "%MOD_DIR%\localisation\0_common.csv"
) do (
    if exist "%%~F" (
        echo   [OK] %%~F
    ) else (
        echo   [WARN] %%~F - Not found ^(may be optional^)
    )
)
echo.

echo Checking localization files...
if exist "%MOD_DIR%\localisation\*.csv" (
    for %%F in ("%MOD_DIR%\localisation\*.csv") do call :CheckCsvSemicolons "%%~fF"
)

set "CSV_CHECK=0"
set "CSV_FILES=0"
if exist "%MOD_DIR%\localisation\*.csv" (
    for /f %%N in ('powershell -NoProfile -Command "$files = Get-ChildItem -Path '%MOD_DIR%/localisation' -Filter '*.csv' -ErrorAction SilentlyContinue; $ok = 0; foreach ($f in $files) { $line = Get-Content -LiteralPath $f.FullName | Where-Object { $_ -notmatch '^\s*#' -and $_.Trim() -ne '' } | Select-Object -First 1; if ($line -and (($line.ToCharArray() | Where-Object { $_ -eq ';' }).Count -eq 14)) { $ok++ } }; $ok"') do set "CSV_CHECK=%%N"
    for /f %%N in ('powershell -NoProfile -Command "(Get-ChildItem -Path '%MOD_DIR%/localisation' -Filter '*.csv' -ErrorAction SilentlyContinue).Count"') do set "CSV_FILES=%%N"
)
if %CSV_FILES% GTR 0 if %CSV_CHECK%==%CSV_FILES% (
    echo   [OK] CSV files appear properly formatted
)
echo.

echo Checking province ID references...
set "PROV_TMP=%TEMP%\validate_mod_provs_%RANDOM%_%RANDOM%.txt"
if exist "%PROV_TMP%" del /q "%PROV_TMP%" >nul 2>nul

if exist "%MOD_DIR%\events\*.txt" (
    powershell -NoProfile -Command "$ids = Select-String -Path '%MOD_DIR%/events/*.txt' -Pattern '\bowns\s*=\s*\d+\b' -ErrorAction SilentlyContinue | ForEach-Object { [regex]::Match($_.Line,'\d+').Value } | Sort-Object -Unique | Select-Object -First 5; $ids | Set-Content -LiteralPath '%PROV_TMP%'" >nul
)
if not exist "%PROV_TMP%" if exist "%MOD_DIR%\decisions\*.txt" (
    powershell -NoProfile -Command "$ids = Select-String -Path '%MOD_DIR%/decisions/*.txt' -Pattern '\bowns\s*=\s*\d+\b' -ErrorAction SilentlyContinue | ForEach-Object { [regex]::Match($_.Line,'\d+').Value } | Sort-Object -Unique | Select-Object -First 5; $ids | Set-Content -LiteralPath '%PROV_TMP%'" >nul
)

if exist "%PROV_TMP%" (
    echo   Sample province IDs found in events/decisions:
    for /f "usebackq delims=" %%I in ("%PROV_TMP%") do (
        if not "%%~I"=="" (
            powershell -NoProfile -Command "if (Select-String -Path '%MOD_DIR%/map/definition.csv' -Pattern '^%%~I,' -Quiet -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }" >nul
            if !errorlevel! equ 0 (
                echo     [OK] Province %%~I exists
            ) else (
                echo     [ERROR] Province %%~I not found in definition.csv
                set /a ERRORS+=1
            )
        )
    )
) else (
    echo   No province references found to validate
)
if exist "%PROV_TMP%" del /q "%PROV_TMP%" >nul 2>nul
echo.

echo Checking decision file structure...
if exist "%MOD_DIR%\decisions\*.txt" (
    for %%F in ("%MOD_DIR%\decisions\*.txt") do call :CheckDecisionStructure "%%~fF"
)
echo.

echo === Validation Summary ===
echo.

if %ERRORS%==0 if %WARNINGS%==0 (
    echo [OK] All checks passed!
    echo Your mod is ready for testing.
    exit /b 0
)

if %ERRORS%==0 if %WARNINGS% GTR 0 (
    echo [WARN] %WARNINGS% warning^(s^) found
    echo Review the warnings above, but your mod should still load.
    exit /b 0
)

echo [ERROR] %ERRORS% error^(s^) found
echo Please fix the errors above before testing.
exit /b 1

:CheckBraceBalance
set "FILE=%~1"
set "OPEN=0"
set "CLOSE=0"

for /f "tokens=1,2 delims=|" %%A in ('powershell -NoProfile -Command "$c = Get-Content -Raw -LiteralPath '%~1' -ErrorAction SilentlyContinue; if ($null -eq $c) { $c = '' }; $o = ($c.ToCharArray() | Where-Object { $_ -eq '{' }).Count; $cl = ($c.ToCharArray() | Where-Object { $_ -eq '}' }).Count; Write-Output ($o.ToString() + '|' + $cl.ToString())"') do (
    set "OPEN=%%A"
    set "CLOSE=%%B"
)

if not "%OPEN%"=="%CLOSE%" (
    echo   [ERROR] %~1 - Unbalanced braces ^({%OPEN% vs }%CLOSE%^)
    set /a ERRORS+=1
)
exit /b 0

:CheckCsvSemicolons
set "CSV_FILE=%~1"
set "HAS_BAD=0"
for /f "usebackq delims=" %%L in (`powershell -NoProfile -Command "$bad = @(); Get-Content -LiteralPath '%~1' | ForEach-Object { if ($_ -match '^\s*#' -or $_.Trim() -eq '') { return }; $sc = ($_.ToCharArray() | Where-Object { $_ -eq ';' }).Count; if ($sc -ne 14) { $bad += $_ } }; $bad | Select-Object -First 3"`) do (
    if !HAS_BAD! equ 0 echo   [WARN] %~1 - Lines with wrong semicolon count:
    set "HAS_BAD=1"
    echo %%L
)
if %HAS_BAD%==1 set /a WARNINGS+=1
exit /b 0

:CheckDecisionStructure
set "DEC_FILE=%~1"
for /f "usebackq delims=" %%M in (`powershell -NoProfile -Command "$c = Get-Content -Raw -LiteralPath '%~1' -ErrorAction SilentlyContinue; if ($null -eq $c) { $c = '' }; if ($c -notmatch 'political_decisions\s*=\s*\{') { 'political_decisions' }; if ($c -notmatch 'potential\s*=\s*\{') { 'potential' }; if ($c -notmatch 'allow\s*=\s*\{') { 'allow' }; if ($c -notmatch 'effect\s*=\s*\{') { 'effect' }"`) do (
    if "%%M"=="political_decisions" echo   [WARN] %~1 - May not be wrapped in political_decisions block
    if "%%M"=="potential" echo   [WARN] %~1 - May be missing 'potential' block
    if "%%M"=="allow" echo   [WARN] %~1 - May be missing 'allow' block
    if "%%M"=="effect" echo   [WARN] %~1 - May be missing 'effect' block
    set /a WARNINGS+=1
)
exit /b 0
