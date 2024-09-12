import subprocess
import sys
libraries = [
            'markdown2',
            'datetime',
            'transformers',
            'matplotlib',
            'time',
            'csv',
            'numpy',
            'mpl_toolkits.mplot3d',
            'math'
]

try:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def install_requirements() -> None:

        # Lista delle librerie da installare


        # Funzione per installare una libreria


        # Installazione di tutte le librerie nella lista
        for library in libraries:
            install(library)

    print("Inizializzazione...")

    install_requirements()

    print("Installazione completata!")
    input("Premere invio per chiudere il programma")

except:
    print(f"Errore durante l'installazione delle librerie, preghiamo di installare le librerie manualmente con il comando pip install <libreria>, installare le seguenti librerie: {libraries}")

    input("Premere invio per chiudere il programma")


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.
