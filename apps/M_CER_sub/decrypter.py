import rsa
import os

# Funzione per caricare la chiave privata
def carica_chiave_privata(filepath: str) -> rsa.PrivateKey:
    with open(filepath, "rb") as f:
        key_data = f.read()
    return rsa.PrivateKey.load_pkcs1(key_data)

# Carica la chiave privata dalla cartella 'keys'
private_key_path = "keys/private.pem"
if os.path.exists(private_key_path):
    private_key = carica_chiave_privata(private_key_path)
else:
    print(f"Chiave privata non trovata in {private_key_path}")
    exit(1)

# Chiede il messaggio cifrato da decriptare
with open("crypted/encrypted.bin", "rb") as f:
    encrypted = f.read()

# Decripta il messaggio
message = rsa.decrypt(encrypted, private_key)

# Crea la cartella 'decrypted' se non esiste
if not os.path.exists("decrypted"):
    os.makedirs("decrypted")

# Salva il messaggio decriptato in un file nella cartella 'decrypted'
with open("decrypted/message.txt", "wb") as f:
    f.write(message)

print("Messaggio decriptato e salvato in 'decrypted/message.txt'.")
#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.