import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from M_func_toolkit import save, read, log, directory_exists_create

class VotiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Voti")
        self.geometry("600x400")

        self.voti = []

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Add a frame for input and buttons
        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10, fill=tk.X)

        # Voti input
        self.voti_input = ttk.Entry(frame, width=50)
        self.voti_input.grid(row=0, column=0, padx=5, pady=5)

        add_button = ttk.Button(frame, text="Aggiungi Voto", command=self.add_voto)
        add_button.grid(row=0, column=1, padx=5, pady=5)

        save_button = ttk.Button(frame, text="Salva Voti", command=self.salva_voti)
        save_button.grid(row=1, column=0, padx=5, pady=5)

        load_button = ttk.Button(frame, text="Carica Voti", command=self.carica_voti)
        load_button.grid(row=1, column=1, padx=5, pady=5)

        plot_button = ttk.Button(frame, text="Mostra Grafico", command=self.mostra_grafico)
        plot_button.grid(row=2, column=0, columnspan=2, pady=5)

        exit_button = ttk.Button(frame, text="Esci", command=self.quit)
        exit_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Add a label for status messages
        self.status_label = ttk.Label(self, text="")
        self.status_label.pack(pady=10)

        # Ensure the data directory exists
        directory_exists_create("data")

    def add_voto(self):
        try:
            voto = int(self.voti_input.get())
            self.voti.append(voto)
            self.voti_input.delete(0, tk.END)
            self.update_status(f"Voto {voto} aggiunto!")
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero valido")

    def salva_voti(self):
        if not self.voti:
            messagebox.showwarning("Avviso", "Non ci sono voti da salvare")
            return

        filename = "voti.txt"
        for voto in self.voti:
            save(str(voto), filename, folder="data")
        log(f"Salvati {len(self.voti)} voti nel file {filename}", folder="logs")
        self.update_status(f"Voti salvati in {filename}")

    def carica_voti(self):
        filename = "voti.txt"
        content = read(filename, folder="data")
        if content:
            self.voti = [int(voto) for voto in content.splitlines()]
            log(f"Letti {len(self.voti)} voti dal file {filename}", folder="logs")
            self.update_status(f"Voti caricati da {filename}")
        else:
            messagebox.showwarning("Avviso", "Nessun voto trovato da caricare")

    def mostra_grafico(self):
        if not self.voti:
            messagebox.showwarning("Avviso", "Non ci sono voti da mostrare")
            return
        
        media = calcola_media(self.voti)

        fig, ax = plt.subplots()
        ax.plot(self.voti, label="Voti", marker="o")
        ax.axhline(y=media, color='r', linestyle='--', label=f"Media: {media:.2f}")
        ax.set_title("I tuoi voti")
        ax.set_xlabel("Esame")
        ax.set_ylabel("Voto")
        ax.legend()
        ax.grid(True)

        # Display plot in Tkinter window
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Handle the closing of the plot window
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # Destroy the canvas and close the application
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
        self.destroy()

    def update_status(self, message):
        self.status_label.config(text=message)

def calcola_media(voti):
    return sum(voti) / len(voti)

if __name__ == "__main__":
    app = VotiApp()
    app.mainloop()


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.