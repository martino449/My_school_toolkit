import os
from M_func_toolkit import M_info, log, save, read, directory_exists_create, backup_py_files, directory_exists, system_info, time_info, battery_info, cpu_info, ram_info, install_requirements, hide_console
from M_CER import start_crypter, start_decrypter, generate_keys

p_actions = {
    "M_info": M_info,
    "backup_py": backup_py_files,
    "system_info": system_info,
    "time_info": time_info,
    "battery_info": battery_info,
    "cpu_info": cpu_info,
    "ram_info": ram_info,
    "install_requirements": install_requirements,
    "start_crypter": start_crypter,
    "start_decrypter": start_decrypter,
    "generate_keys": generate_keys
}


def default() -> None:
    print("Comando non riconosciuto.")


if __name__ == "__main__":
    M_info()
    log("start")
    while True:
        comando = input(">")
        if comando == "exit":
            hide_console()
            break
        elif comando == "help":
            print("Comandi disponibili: \n" + "\n".join(p_actions.keys()) + "\nclear\n" + "dir\n" + "help\n" + "exit" + "\n" + "log\n" + "save\n" + "read\n" + "directory_exists\n" + "directory_exists_create")

        elif comando == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif comando == "dir":
            print(os.getcwd())

        elif comando == "log":
            action_to_log = input("Comando da loggare: ")
            log(action_to_log)

        elif comando == "save":
            filename = input("Nome del file: ")
            data = input("Dati da salvare: ")
            save(data, filename)
            log("save")
            log(filename)
            log(data)
        elif comando == "read":
            try:
                filename = input("Nome del file: ")
                data = read(filename)
                print(data)
                log("read")
                log(filename)
                log(data)
            except Exception as e:
                print(f"Un'errore ha impedito la lettura del fiel: {e}")
                log(e)

        elif comando == "directory_exists":
            directory = input("Inserisci la directory: ")
            print(directory_exists(directory))
            log(directory_exists(directory))
        

        elif comando == "directory_exists_create":
            directory = input("Inserisci la directory: ")
            directory_exists_create(directory)
            log("directory_exists_create")
            log(directory)


        
        
        else:
            action = p_actions.get(comando, default)
            action()
            log(action)




#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.