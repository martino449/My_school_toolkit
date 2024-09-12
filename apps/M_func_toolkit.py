import os
from datetime import datetime
import ctypes
import shutil
import subprocess
import sys
version = "0.2.3"

def M_info() -> None:
    print(f"M_func_toolkit \nAuthor: Mario Pisano \n{version} \nLicense: EUPL 1.2 \nCopyright: 2024 Mario Pisano")

def log(action: str, folder: str = "apps/logs") -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join(folder, "log.txt")

    with open(log_path, "a") as f:
        f.write(f"{timestamp} - {action}\n")

def save(data: str, filename: str, folder: str = "apps/data", mode: str = 'a') -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, filename)

    with open(file_path, mode) as f:
        f.write(data + "\n")

def read(filename: str, folder: str = "apps/data") -> str:
    file_path = os.path.join(folder, filename)
    if not os.path.exists(file_path):
        return ""
    
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        log(f"Errore nella lettura del file {filename}: {e}")
        return ""

def directory_exists(directory: str) -> bool:
    return os.path.exists(directory)

def directory_exists_create(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)

def hide_console() -> None:
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE

def show_console() -> None:
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 5)  # 5 = SW_SHOW


def backup_py_files() -> None:
    # Creare una cartella di backup con timestamp
    backup_folder = 'backup'
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(backup_folder, f'backup_{timestamp}')
    os.mkdir(backup_folder)
    
    # Eseguire il backup di tutti i file .py
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.py'):
            shutil.copy(file_name, backup_folder)
            print(f"Backup eseguito per: {file_name}")
    
    print(f"Backup completato in: {backup_folder}")




def system_info() -> None:
    # Informazioni sul sistema operativo
    print(f"Sistema Operativo: {os.name}")
    print(f"Directory corrente: {os.getcwd()}")
    print(f"Nome utente: {os.getlogin()}")
    print(f"Spazio libero su disco: {shutil.disk_usage(os.getcwd()).free / (1024 * 1024 * 1024):.2f} GB")

def time_info() -> None:
    # Informazioni sulla data e ora corrente
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Data e ora corrente: {current_time}")

def battery_info() -> None:
    # Informazioni sullo stato della batteria (solo per Windows)
    if os.name == 'nt':
        SYSTEM_POWER_STATUS = ctypes.Structure
        class SYSTEM_POWER_STATUS(ctypes.Structure):
            _fields_ = [("ACLineStatus", ctypes.c_byte),
                        ("BatteryFlag", ctypes.c_byte),
                        ("BatteryLifePercent", ctypes.c_byte),
                        ("SystemStatusFlag", ctypes.c_byte),
                        ("BatteryLifeTime", ctypes.c_ulong),
                        ("BatteryFullLifeTime", ctypes.c_ulong)]

        status = SYSTEM_POWER_STATUS()
        if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status)):
            print(f"Percentuale batteria: {status.BatteryLifePercent}%")
        else:
            print("Impossibile ottenere informazioni sulla batteria.")
    else:
        print("Questa funzione è disponibile solo su Windows.")




def cpu_info() -> None:
    # Informazioni sull'uso della CPU
    print("Questa funzione è WIP")
#    if os.name == 'nt':
#        cpu_load = ctypes.c_ulong()
#        ctypes.windll.kernel32.GetSystemTimes(ctypes.byref(cpu_load), None, None)
#        print(f"Utilizzo CPU: {cpu_load.value}%")
#    else:
#        print("Questa funzione è disponibile solo su Windows.")

def ram_info() -> None:
    # Informazioni sulla memoria RAM disponibile
    if os.name == 'nt':
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong),
                        ("dwMemoryLoad", ctypes.c_ulong),
                        ("ullTotalPhys", ctypes.c_ulonglong),
                        ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong),
                        ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong),
                        ("ullAvailVirtual", ctypes.c_ulonglong),
                        ("sullAvailExtendedVirtual", ctypes.c_ulonglong)]
        memory_status = MEMORYSTATUSEX()
        memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))
        total_memory = memory_status.ullTotalPhys / (1024 ** 3)
        available_memory = memory_status.ullAvailPhys / (1024 ** 3)
        print(f"Memoria totale: {total_memory:.2f} GB")
        print(f"Memoria disponibile: {available_memory:.2f} GB")
    else:
        print("Questa funzione è disponibile solo su Windows.")


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_requirements() -> None:

    # Lista delle librerie da installare
    libraries = [
        'os',
        'tkinter',
        'markdown2',
        'datetime',
        'ctypes',
        'shutil',
        'transformers',
        'matplotlib',
        'threading',
        'winsound',
        'time',
        'csv',
        'numpy',
        'mpl_toolkits.mplot3d',
        'math'
    ]

    # Funzione per installare una libreria


    # Installazione di tutte le librerie nella lista
    for library in libraries:
        install(library)

    print("Installazione completata!")


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.
