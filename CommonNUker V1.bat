@echo off

:main_menu
cls
echo CommonNUker V1
echo Valassz egy lehetoseget:
echo 1. Login
echo 2. Register
echo 3. Kilepes

set /p choice="Kerlek valassz egy lehetoseget: "

if "%choice%"=="1" goto login
if "%choice%"=="2" goto register
if "%choice%"=="3" goto end

echo Hibás választás!
pause
goto main_menu

:login
cls
echo *** Bejelentkezes ***

set /p email="Add meg az email cimed: "
set /p password="Add meg a jelszavad: "

if exist users.txt (
    for /f "tokens=1,2 delims=," %%a in (users.txt) do (
        if "%%a"=="%email%" (
            if "%%b"=="%password%" (
                echo Sikeres bejelentkezes!
                pause
                goto tool_menu
            )
        )
    )
)

echo Hibas email vagy jelszo!
pause
goto main_menu

:register
cls
echo *** Regisztracio ***

set /p email="Add meg az email cimed: "
set /p password="Add meg a jelszavad: "

set found=false
if exist users.txt (
    for /f "tokens=1 delims=," %%a in (users.txt) do (
        if "%%a"=="%email%" (
            set found=true
        )
    )
)

if "%found%"=="true" (
    echo Ez az email cím már regisztrálva van!
    pause
    goto main_menu
) else (
    echo %email%,%password%>> users.txt
    color a
    echo Sikeres regisztráció!
    pause
    goto tool_menu
)

:tool_menu
cls
echo *** CommonNUker Tools ***
echo 1. chanels replace
echo 2. roles create
echo 3. Spammer


set /p tool_choice="Valassz egy lehetoseget: "

if "%tool_choice%"=="1" goto create_channels
if "%tool_choice%"=="2" goto create_roles
if "%tool_choice%"=="3" goto spammer


goto tool_menu

:create_channels
cls
py delchan.py
pause
goto tool_menu

:create_roles
cls
py racre.py
pause
goto tool_menu

:spammer
cls
py spammer.py
pause
goto tool_menu

:end
exit
