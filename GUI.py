import tkinter as tk
import os
import subprocess
import ctypes



def hide_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE

hide_console()


def show_console() -> None:
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 5)  # 5 = SW_SHOW



# Percorso alla cartella contenente gli script Python
apps_folder = "./apps/"


def run_ADC() -> None:
    show_console()
    script_path = os.path.join(apps_folder, 'ADC.py')
    subprocess.run(['python', script_path])

def run_quiz() -> None:
    show_console()
    script_path = os.path.join(apps_folder, 'quiz_creator_app.py')
    subprocess.run(['python', script_path])
def run_2dcreator() -> None:
    script_path = os.path.join(apps_folder, '2dcreator.py')
    subprocess.run(['python', script_path])

def run_editor() -> None:
    script_path = os.path.join(apps_folder, 'editor.py')
    subprocess.run(['python', script_path])

def run_media_voti() -> None:
    script_path = os.path.join(apps_folder, 'media_voti.py')
    subprocess.run(['python', script_path])

def run_pomodoro() -> None:
    script_path = os.path.join(apps_folder, 'pomodoro.py')
    subprocess.run(['python', script_path])

def run_reacions() -> None:
    script_path = os.path.join(apps_folder, 'reacions.py')
    subprocess.run(['python', script_path])

def run_vector() -> None:
    script_path = os.path.join(apps_folder, 'vector.py')
    subprocess.run(['python', script_path])

# Creazione della finestra principale
root = tk.Tk()
root.title("Python Script Launcher")

# Etichetta di istruzione
label = tk.Label(root, text="Seleziona lo script Python da eseguire:")
label.pack(pady=10)

# Pulsanti per eseguire gli script Python
btn_2dcreator = tk.Button(root, text="Esegui 2DCreator", command=run_2dcreator)
btn_2dcreator.pack(pady=5)

btn_editor = tk.Button(root, text="Esegui Editor", command=run_editor)
btn_editor.pack(pady=5)

btn_media_voti = tk.Button(root, text="Esegui Media Voti", command=run_media_voti)
btn_media_voti.pack(pady=5)

btn_pomodoro = tk.Button(root, text="Esegui Pomodoro", command=run_pomodoro)
btn_pomodoro.pack(pady=5)

btn_reacions = tk.Button(root, text="Esegui Reactions", command=run_reacions)
btn_reacions.pack(pady=5)

btn_vector = tk.Button(root, text="Esegui Vector", command=run_vector)
btn_vector.pack(pady=5)

btn_vector = tk.Button(root, text="Esegui Quiz Creator", command=run_quiz)
btn_vector.pack(pady=5)

btn_vector = tk.Button(root, text="Apri ambiente di comando (solo utenti avanzati)", command=run_ADC)
btn_vector.pack(pady=5)

# Avvio della finestra
root.mainloop()


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.
