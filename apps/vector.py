import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import acos, degrees
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class Vettore3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def somma(self, vettore2):
        return Vettore3D(self.x + vettore2.x, self.y + vettore2.y, self.z + vettore2.z)

    def sottrai(self, vettore2):
        return Vettore3D(self.x - vettore2.x, self.y - vettore2.y, self.z - vettore2.z)

    def moltiplica_per_scalare(self, scalare):
        return Vettore3D(self.x * scalare, self.y * scalare, self.z * scalare)

    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def prodotto_scalare(self, vettore2):
        return self.x * vettore2.x + self.y * vettore2.y + self.z * vettore2.z

    def prodotto_vettoriale(self, vettore2):
        x = self.y * vettore2.z - self.z * vettore2.y
        y = self.z * vettore2.x - self.x * vettore2.z
        z = self.x * vettore2.y - self.y * vettore2.x
        return Vettore3D(x, y, z)

    def angolo_tra_vettori(self, vettore2):
        dot_product = self.prodotto_scalare(vettore2)
        mag1 = self.modulo()
        mag2 = vettore2.modulo()
        cos_theta = dot_product / (mag1 * mag2)
        angolo_radiani = acos(np.clip(cos_theta, -1.0, 1.0))  # Clip to handle numerical errors
        return degrees(angolo_radiani)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def render(self, vettore2=None, operazione=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Disegna il primo vettore
        ax.quiver(0, 0, 0, self.x, self.y, self.z, color='r', label=f'Vettore 1 ({self.x}, {self.y}, {self.z})')

        if vettore2:
            # Disegna il secondo vettore
            ax.quiver(0, 0, 0, vettore2.x, vettore2.y, vettore2.z, color='b', label=f'Vettore 2 ({vettore2.x}, {vettore2.y}, {vettore2.z})')

            if operazione == 'somma':
                v_sum = self.somma(vettore2)
                ax.quiver(0, 0, 0, v_sum.x, v_sum.y, v_sum.z, color='g', label=f'Somma ({v_sum.x}, {v_sum.y}, {v_sum.z})')

            elif operazione == 'sottrazione':
                v_diff = self.sottrai(vettore2)
                ax.quiver(0, 0, 0, v_diff.x, v_diff.y, v_diff.z, color='m', label=f'Sottrazione ({v_diff.x}, {v_diff.y}, {v_diff.z})')

            elif operazione == 'prodotto_scalare':
                prod_scalare = self.prodotto_scalare(vettore2)
                print(f"Prodotto Scalare: {prod_scalare}")

            elif operazione == 'prodotto_vettoriale':
                v_prod_vettoriale = self.prodotto_vettoriale(vettore2)
                ax.quiver(0, 0, 0, v_prod_vettoriale.x, v_prod_vettoriale.y, v_prod_vettoriale.z, color='c', label=f'Prodotto Vettoriale ({v_prod_vettoriale.x}, {v_prod_vettoriale.y}, {v_prod_vettoriale.z})')

            elif operazione == 'angolo':
                angolo = self.angolo_tra_vettori(vettore2)
                print(f"Angolo tra i vettori: {angolo:.2f} gradi")

        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Visualizzazione dei Vettori e delle loro Operazioni')
        ax.legend()
        plt.show()

# Inizializzazione della lista dei vettori
vettori = []

def salva_vettori(filepath="data/vettori_salvati.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Crea la cartella se non esiste
    with open(filepath, "w") as f:
        for v in vettori:
            f.write(f"{v.x},{v.y},{v.z}\n")
    print(f"Vettori salvati su {filepath}")

def carica_vettori(filepath="data/vettori_salvati.txt"):
    vettori_caricati = []
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            for line in f:
                x, y, z = map(float, line.strip().split(","))
                vettori_caricati.append(Vettore3D(x, y, z))
        print(f"Vettori caricati da {filepath}")
    return vettori_caricati

def mostra_vettori():
    if not vettori:
        messagebox.showwarning("Attenzione", "Non ci sono vettori creati.")
        return
    vettori_str = "\n".join([f"{i}. {vett}" for i, vett in enumerate(vettori)])
    messagebox.showinfo("Vettori", f"Vettori disponibili:\n{vettori_str}")

def somma_vettori():
    mostra_vettori()
    if len(vettori) < 2:
        messagebox.showwarning("Attenzione", "Devi creare almeno due vettori per sommarli.")
        return
    idx1 = int(simpledialog.askstring("Input", "Seleziona il primo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    idx2 = int(simpledialog.askstring("Input", "Seleziona il secondo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
        v1 = vettori[idx1]
        v2 = vettori[idx2]
        v_sum = v1.somma(v2)
        v1.render(vettore2=v2, operazione='somma')
        messagebox.showinfo("Somma", f"Somma: {v_sum}")
    else:
        messagebox.showwarning("Attenzione", "Indici non validi.")

def sottrai_vettori():
    mostra_vettori()
    if len(vettori) < 2:
        messagebox.showwarning("Attenzione", "Devi creare almeno due vettori per sottrarli.")
        return
    idx1 = int(simpledialog.askstring("Input", "Seleziona il primo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    idx2 = int(simpledialog.askstring("Input", "Seleziona il secondo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
        v1 = vettori[idx1]
        v2 = vettori[idx2]
        v_diff = v1.sottrai(v2)
        v1.render(vettore2=v2, operazione='sottrazione')
        messagebox.showinfo("Sottrazione", f"Sottrazione: {v_diff}")
    else:
        messagebox.showwarning("Attenzione", "Indici non validi.")

def moltiplica_vettore_per_scalare():
    mostra_vettori()
    if not vettori:
        messagebox.showwarning("Attenzione", "Non ci sono vettori creati.")
        return
    idx = int(simpledialog.askstring("Input", "Seleziona il vettore da moltiplicare (indice da 0 a {}):".format(len(vettori) - 1)))
    if 0 <= idx < len(vettori):
        v = vettori[idx]
        scalare = float(simpledialog.askstring("Input", "Inserisci il valore dello scalare:"))
        v_scaled = v.moltiplica_per_scalare(scalare)
        v.render(operazione='moltiplicazione_per_scalare')
        messagebox.showinfo("Moltiplicazione per Scalare", f"Vettore moltiplicato per {scalare}: {v_scaled}")
    else:
        messagebox.showwarning("Attenzione", "Indice non valido.")

def prodotto_scalare_vettori():
    mostra_vettori()
    if len(vettori) < 2:
        messagebox.showwarning("Attenzione", "Devi creare almeno due vettori per calcolare il prodotto scalare.")
        return
    idx1 = int(simpledialog.askstring("Input", "Seleziona il primo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    idx2 = int(simpledialog.askstring("Input", "Seleziona il secondo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
        v1 = vettori[idx1]
        v2 = vettori[idx2]
        prod_scalare = v1.prodotto_scalare(v2)
        messagebox.showinfo("Prodotto Scalare", f"Prodotto scalare: {prod_scalare}")
    else:
        messagebox.showwarning("Attenzione", "Indici non validi.")

def prodotto_vettoriale_vettori():
    mostra_vettori()
    if len(vettori) < 2:
        messagebox.showwarning("Attenzione", "Devi creare almeno due vettori per calcolare il prodotto vettoriale.")
        return
    idx1 = int(simpledialog.askstring("Input", "Seleziona il primo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    idx2 = int(simpledialog.askstring("Input", "Seleziona il secondo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
        v1 = vettori[idx1]
        v2 = vettori[idx2]
        v_prod_vettoriale = v1.prodotto_vettoriale(v2)
        v1.render(vettore2=v2, operazione='prodotto_vettoriale')
        messagebox.showinfo("Prodotto Vettoriale", f"Prodotto vettoriale: {v_prod_vettoriale}")
    else:
        messagebox.showwarning("Attenzione", "Indici non validi.")

def angolo_vettori():
    mostra_vettori()
    if len(vettori) < 2:
        messagebox.showwarning("Attenzione", "Devi creare almeno due vettori per calcolare l'angolo.")
        return
    idx1 = int(simpledialog.askstring("Input", "Seleziona il primo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    idx2 = int(simpledialog.askstring("Input", "Seleziona il secondo vettore (indice da 0 a {}):".format(len(vettori) - 1)))
    if 0 <= idx1 < len(vettori) and 0 <= idx2 < len(vettori):
        v1 = vettori[idx1]
        v2 = vettori[idx2]
        angolo = v1.angolo_tra_vettori(v2)
        messagebox.showinfo("Angolo", f"Angolo tra i vettori: {angolo:.2f} gradi")
    else:
        messagebox.showwarning("Attenzione", "Indici non validi.")

def aggiungi_vettore():
    try:
        x = float(simpledialog.askstring("Input", "Inserisci la componente X del vettore:"))
        y = float(simpledialog.askstring("Input", "Inserisci la componente Y del vettore:"))
        z = float(simpledialog.askstring("Input", "Inserisci la componente Z del vettore:"))
        vettori.append(Vettore3D(x, y, z))
        messagebox.showinfo("Aggiungi Vettore", "Vettore aggiunto con successo.")
    except ValueError:
        messagebox.showwarning("Attenzione", "Componente non valida. Assicurati di inserire numeri.")

def on_aggiungi():
    aggiungi_vettore()

def on_somma():
    somma_vettori()

def on_sottrai():
    sottrai_vettori()

def on_scalare():
    moltiplica_vettore_per_scalare()

def on_prodotto_scalare():
    prodotto_scalare_vettori()

def on_prodotto_vettoriale():
    prodotto_vettoriale_vettori()

def on_angolo():
    angolo_vettori()



def on_carica():
    global vettori
    vettori = carica_vettori()

def on_mostra():
    mostra_vettori()


def on_salva():
    salva_vettori()
    exit()

def menu_principale():
    # Carica vettori automaticamente all'avvio
    global vettori
    vettori = carica_vettori()

    root = tk.Tk()
    root.title("Gestione Vettori 3D")

    # Pulsanti per ogni operazione
    tk.Button(root, text="Crea Nuovo Vettore", command=on_aggiungi).pack(pady=5)
    tk.Button(root, text="Somma Vettori", command=on_somma).pack(pady=5)
    tk.Button(root, text="Sottrai Vettori", command=on_sottrai).pack(pady=5)
    tk.Button(root, text="Moltiplica per Scalare", command=on_scalare).pack(pady=5)
    tk.Button(root, text="Prodotto Scalare", command=on_prodotto_scalare).pack(pady=5)
    tk.Button(root, text="Prodotto Vettoriale", command=on_prodotto_vettoriale).pack(pady=5)
    tk.Button(root, text="Angolo tra Vettori", command=on_angolo).pack(pady=5)
    tk.Button(root, text="Mostra Vettori", command=on_mostra).pack(pady=5)
    tk.Button(root, text="Salva ed Esci", command=on_salva).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    menu_principale()





#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.