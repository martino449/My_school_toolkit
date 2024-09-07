import subprocess
import sys

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