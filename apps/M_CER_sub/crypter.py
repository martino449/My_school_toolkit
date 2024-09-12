import rsa
import os

# Funzione per caricare la chiave pubblica
def carica_chiave_pubblica(filepath: str) -> rsa.PublicKey:
    with open(filepath, "rb") as f:
        key_data = f.read()
    return rsa.PublicKey.load_pkcs1(key_data)

# Chiede il messaggio da criptare
message = input("Enter message: ")
message = message.encode()

# Carica la chiave pubblica dalla cartella 'keys'
public_key_path = "keys/public.pem"
if os.path.exists(public_key_path):
    public_key = carica_chiave_pubblica(public_key_path)
else:
    print(f"Chiave pubblica non trovata in {public_key_path}")
    exit(1)

# Cripta il messaggio
encrypted = rsa.encrypt(message, public_key)

# Crea la cartella 'crypted' se non esiste
if not os.path.exists("crypted"):
    os.makedirs("crypted")

# Salva il messaggio criptato in un file nella cartella 'crypted'
with open("crypted/encrypted.bin", "wb") as f:
    f.write(encrypted)

print("Messaggio criptato e salvato in 'crypted/encrypted.bin'.")
#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.