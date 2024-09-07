import tkinter as tk
import os

# Funzioni per aprire applicazioni
def open_notepad():
    os.system('notepad')

def open_calculator():
    os.system('calc')

def open_cmd():
    os.system('cmd')

def open_browser():
    os.system('start chrome')

# Creazione della finestra principale
root = tk.Tk()
root.title("App Launcher")

# Etichetta di istruzione
label = tk.Label(root, text="Seleziona l'applicazione da aprire:")
label.pack(pady=10)

# Pulsanti per aprire le applicazioni
btn_notepad = tk.Button(root, text="Notepad", command=open_notepad)
btn_notepad.pack(pady=5)

btn_calculator = tk.Button(root, text="Calcolatrice", command=open_calculator)
btn_calculator.pack(pady=5)


btn_browser = tk.Button(root, text="Apri Browser", command=open_browser)
btn_browser.pack(pady=5)

# Avvio della finestra
root.mainloop()
#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.