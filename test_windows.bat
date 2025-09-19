@echo off
echo ====================================
echo                TESTS
echo ====================================
echo.

echo Test 1: Simple launch with debug
echo ====================================
echo exit | python my_shell.py --debug
echo.
pause

echo.
echo Test 2: Launch with script
echo ====================================
python my_shell.py --script scripts\test_basic.txt
echo.
pause

echo.
echo Test 3: Script with errors
echo ====================================
python my_shell.py --script scripts\test_with_errors.txt
echo.
pause

echo.
echo Test 4: All at once
echo ====================================
python my_shell.py --vfs-path C:\temp\my_vfs --script scripts\test_complex.txt --debug
echo.
pause

echo Все тесты завершены!