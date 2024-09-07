import json
from tkinter import Tk, simpledialog

def crea_quiz():
    root = Tk()
    root.withdraw()  # Nasconde la finestra principale

    questions = []
    num_questions = simpledialog.askinteger("Configurazione", "Quante domande vuoi aggiungere?")
    for _ in range(num_questions):
        question = simpledialog.askstring("Domanda", "Inserisci la domanda:")
        options = []
        for i in range(4):
            option = simpledialog.askstring("Opzione", f"Inserisci l'opzione {i+1}:")
            options.append(option)
        answer = simpledialog.askstring("Risposta", "Inserisci la risposta corretta:")
        questions.append({"question": question, "options": options, "answer": answer})

    with open("quiz.json", "w") as file:
        json.dump(questions, file)

    root.quit()

if __name__ == "__main__":
    crea_quiz()
