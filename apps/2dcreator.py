import tkinter as tk
from tkinter import scrolledtext
import os
from M_func_toolkit import hide_console
hide_console()
# Funzione per convertire la lista mondo in una stringa
def mondo_to_str(mondo):
    nuovo_mondo = []
    for n in mondo:
        if n == 0:
            nuovo_mondo.append(" ")  # Spazio vuoto
        elif n == 1:
            nuovo_mondo.append("#")  # Simbolo #
        elif n == 2:
            nuovo_mondo.append("*")  # Simbolo *
        elif n == 3:
            nuovo_mondo.append("&")  # Simbolo &
        elif n == 4:
            nuovo_mondo.append("@")  # Simbolo @
        elif n == 5:
            nuovo_mondo.append("%")  # Simbolo %
        elif n == 6:
            nuovo_mondo.append("+")  # Simbolo +
        elif n == 7:
            nuovo_mondo.append("=")  # Simbolo =
        elif n == "\n":
            nuovo_mondo.append("\n")  # Aggiunge newline
    return "".join(nuovo_mondo)

# Funzione per convertire una stringa in lista mondo
def str_to_mondo(text):
    mondo = []
    lines = text.splitlines()
    for line in lines:
        for char in line:
            if char == " ":
                mondo.append(0)
            elif char == "#":
                mondo.append(1)
            elif char == "*":
                mondo.append(2)
            elif char == "&":
                mondo.append(3)
            elif char == "@":
                mondo.append(4)
            elif char == "%":
                mondo.append(5)
            elif char == "+":
                mondo.append(6)
            elif char == "=":
                mondo.append(7)
        mondo.append("\n")  # Aggiunge newline per ogni riga
    return mondo

def update_mondo(event=None):
    """Aggiorna la lista Mondo_aggiornato con il contenuto dell'area di testo."""
    global Mondo_aggiornato
    text_content = text_area.get("1.0", tk.END).strip()
    Mondo_aggiornato = str_to_mondo(text_content)
    print("Mondo aggiornato:", Mondo_aggiornato)  # Puoi rimuovere questa riga se non ti serve per il debug

def save_mondo():
    """Salva la lista Mondo_aggiornato nel file mondo.txt nella cartella data."""
    if not os.path.exists('data'):
        os.makedirs('data')
    
    with open('data/mondo.txt', 'w') as f:
        f.write(text_area.get("1.0", tk.END))
    status_label.config(text="File salvato come mondo.txt nella cartella data")

# Dati iniziali del mondo
mondo = [
    "a", 0, 1, 1, 0, 1, 1, 0, 0, 1, "b", 0, 1, 1, 0, 1, "c", 0, 1, 0, 
    0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, "d", 1, 0, 0, 1, 0, 1, 
    "e", 1, 1, 0, 0, 0, 1, 0, "f", 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 
    "g", 0, 0, 0, 1, 0, "h", 1, 1, 0, 0, 0, 0, "i", 0, 1, 1, 1, 0, 0, 
    0, 0, 0, 1, 1, "j", 0, 1, 1, 0, 1, 1, 0, "k", 0, 1, 1, 0, 1, 1, 0,
    4, 5, 6, 7, 0, 1, 0
]

# Inizializzazione della lista Mondo_aggiornato
Mondo_aggiornato = mondo

# Creazione della finestra principale
root = tk.Tk()
root.title("Modifica e Salva Mondo")

# Area di visualizzazione e modifica del mondo
text_area = scrolledtext.ScrolledText(root, width=50, height=20)
text_area.pack(pady=10)
text_area.insert(tk.END, mondo_to_str(mondo))
text_area.bind("<KeyRelease>", update_mondo)  # Aggiorna Mondo_aggiornato quando una chiave viene rilasciata

# Pulsante di salvataggio
save_button = tk.Button(root, text="Salva in mondo.txt", command=save_mondo)
save_button.pack(pady=5)

# Etichetta di stato
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

# Avvio della GUI
root.mainloop()




#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.