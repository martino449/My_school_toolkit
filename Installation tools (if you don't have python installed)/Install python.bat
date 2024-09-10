@echo off

:: Personalizza le seguenti variabili
set PYTHON_VERSION=3.11.4
set PYTHON_DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe


:: Scarica l'installer di Python
echo Scaricamento di Python...
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_DOWNLOAD_URL%' -OutFile python.exe"

:: Installa Python
echo Installazione di Python...
start /wait python.exe /quiet InstallAllUsers=1
echo Installazione completata!
