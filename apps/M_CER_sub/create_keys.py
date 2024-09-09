import rsa
import os

# Genera le chiavi
public_key, private_key = rsa.newkeys(512)

# Stampa le chiavi
print(public_key, "\n", private_key)

# Chiede se salvare le chiavi
salvare = input("Salvare le chiavi? (y/n)")
if salvare == "y":
    # Crea la cartella 'keys' se non esiste
    if not os.path.exists("keys"):
        os.makedirs("keys")
    
    # Salva le chiavi nella cartella 'keys'
    with open("keys/public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("keys/private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))
    
    print("Chiavi salvate con successo nella cartella 'keys'.")
else:
    print("Funzione non ancora implementata")
#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.