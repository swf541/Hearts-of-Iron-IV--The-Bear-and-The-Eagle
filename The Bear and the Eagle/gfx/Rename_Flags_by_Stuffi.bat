@Echo off
echo.
echo Welcome to the Flags Rename Script
timeout /t 2 > NUL
echo.
echo Make sure that this .bat script has been put into your gfx folder!
echo.
timeout /t 3 > NUL
:start
cls
echo.
set /p originalflag=Which flag name would you like to rename and copy? (ex.: USA_conservative.tga) 
echo.
set /p newflag=What should the new name be? (ex.: USA_socialist.tga) 
echo.
set /p another=Another new name? ("yes" or "no") 
echo.
if %another% == yes goto another1
echo --------------------------------
echo        Your choice:
echo.
echo    Old Flag name = %originalflag%
echo    New Flag name = %newflag%
echo.
echo --------------------------------
PAUSE

for /f "delims=" %%i in ('dir /s /b /a-d "%originalflag%"') do ( copy "%%i" "%%~dpi\%newflag%" )

PAUSE
cls
goto anotherflagend

:anotherflagend
echo.
set /p again=Another Flag? ("yes" or "no")
if %again% == yes goto start else goto end


:end
exit


:another1
set /p newflag1=What should the second new name be? (ex.: USA_liberal.tga) 
echo.
set /p another1=Another new name? ("yes" or "no")
echo.
if %another1% == yes goto another2
echo --------------------------------
echo        Your choice:
echo.
echo    Old Flag name    = %originalflag%
echo    First Flag name  = %newflag%
echo    Second Flag name = %newflag1%
echo.
echo --------------------------------
PAUSE

for /f "delims=" %%i in ('dir /s /b /a-d "%originalflag%"') do ( copy "%%i" "%%~dpi\%newflag%" )
for /f "delims=" %%i in ('dir /s /b /a-d "%originalflag%"') do ( copy "%%i" "%%~dpi\%newflag1%" )

PAUSE
cls
goto anotherflagend


:another2
set /p newflag2=What should the third new name be? (ex.: USA_centrist.tga) 
echo.
echo --------------------------------
echo        Your choice:
echo.
echo    Old Flag name    = %originalflag%
echo    First Flag name  = %newflag%
echo    Second Flag name = %newflag1%
echo    Third Flag name  = %newflag2%
echo.
echo --------------------------------
PAUSE

for /f "delims=" %%i in ('dir /s /b /a-d "%originalflag%"') do ( copy "%%i" "%%~dpi\%newflag%" )
for /f "delims=" %%i in ('dir /s /b /a-d "%originalflag%"') do ( copy "%%i" "%%~dpi\%newflag1%" )
for /f "delims=" %%i in ('dir /s /b /a-d "%originalflag%"') do ( copy "%%i" "%%~dpi\%newflag2%" )

PAUSE
cls
goto anotherflagend
