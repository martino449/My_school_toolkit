import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from M_func_toolkit import hide_console

hide_console()
# Percorso della cartella
cartella = 'Quiz creator'

# Esegui file Python specifici
file1 = os.path.join(cartella, 'quiz.py')
file2 = os.path.join(cartella, 'esegui_quiz.py')

def start_file1() -> None:
    # Controlla se il file esiste e eseguilo
    if os.path.isfile(file1):
        subprocess.run(['python', file1])
    else:
        messagebox.showerror("Errore", f"Il file {file1} non esiste nella cartella {cartella}")

def start_file2() -> None:
    # Controlla se il file esiste e eseguilo
    if os.path.isfile(file2):
        subprocess.run(['python', file2])
    else:
        messagebox.showerror("Errore", f"Il file {file2} non esiste nella cartella {cartella}")

# Creazione della finestra principale
root = tk.Tk()
root.title("Quiz Creator")

# Creazione dei pulsanti
button1 = tk.Button(root, text="Esegui quiz.py", command=start_file1)
button1.pack(pady=10)

button2 = tk.Button(root, text="Esegui esegui_quiz.py", command=start_file2)
button2.pack(pady=10)

# Avvio del loop principale di Tkinter
root.mainloop()




#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.