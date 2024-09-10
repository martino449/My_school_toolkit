#CODICE
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Percorso della cartella
cartella = 'M_CER_sub'

# Esegui file Python specifici
file1 = os.path.join(cartella, 'crypter.py')
file2 = os.path.join(cartella, 'decrypter.py')
file3 = os.path.join(cartella, 'create_keys.py')

def start_crypter() -> None:
    if os.path.isfile(file1):
        subprocess.run(['python', file1])
    else:
        messagebox.showerror("Errore", f"Il file {file1} non esiste nella cartella {cartella}")

def start_decrypter() -> None:
    if os.path.isfile(file2):
        subprocess.run(['python', file2])
    else:
        messagebox.showerror("Errore", f"Il file {file2} non esiste nella cartella {cartella}")

def generate_keys() -> None:
    if os.path.isfile(file3):
        subprocess.run(['python', file3])
    else:
        messagebox.showerror("Errore", f"Il file {file3} non esiste nella cartella {cartella}")


if __name__ == "__main__":   

    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Gestione File Python")

    # Creazione dei pulsanti
    btn_crypter = tk.Button(root, text="Avvia Crypter", command=start_crypter)
    btn_crypter.pack(pady=10)

    btn_decrypter = tk.Button(root, text="Avvia Decrypter", command=start_decrypter)
    btn_decrypter.pack(pady=10)

    btn_keys = tk.Button(root, text="Genera Chiavi", command=generate_keys)
    btn_keys.pack(pady=10)

    # Avvio del loop principale della GUI
    
    root.mainloop()


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.