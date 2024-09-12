import tkinter as tk
from tkinter import scrolledtext
import markdown2
from M_func_toolkit import hide_console
hide_console()

def aggiorna_anteprima(event=None):
    testo_markdown = text_editor.get("1.0", tk.END)
    testo_html = markdown2.markdown(testo_markdown)
    preview_area.config(state=tk.NORMAL)
    preview_area.delete("1.0", tk.END)
    preview_area.insert(tk.END, testo_html)
    preview_area.config(state=tk.DISABLED)

# Crea la finestra principale
root = tk.Tk()
root.title("Editor con Anteprima")

# Configura la griglia
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)

# Crea un campo di testo per l'editor Markdown
text_editor = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_editor.grid(row=0, column=0, sticky="nsew")

# Crea un'area di testo per visualizzare l'anteprima Markdown
preview_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="lightgray", state=tk.DISABLED)
preview_area.grid(row=1, column=0, sticky="nsew")

# Collega l'evento di modifica del testo all'aggiornamento dell'anteprima
text_editor.bind("<KeyRelease>", aggiorna_anteprima)

# Avvia l'applicazione
root.mainloop()




#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.