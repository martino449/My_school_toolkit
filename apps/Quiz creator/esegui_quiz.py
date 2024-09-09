import json
import tkinter as tk
from tkinter import messagebox
import os

class QuizApp:
    def __init__(self, root, quiz_files):
        self.root = root
        self.root.title("Quiz Grafico")
        
        self.questions = []
        for quiz_file in quiz_files:
            with open(quiz_file, "r") as file:
                self.questions.extend(json.load(file))
        
        self.current_question = 0
        self.score = 0
        
        self.setup_ui()
        self.update_question()
    
    def setup_ui(self):
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        self.options = []
        for _ in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.var, value="")
            rb.pack(anchor="w")
            self.options.append(rb)
        
        self.submit_button = tk.Button(self.root, text="Invia", command=self.check_answer)
        self.submit_button.pack(pady=20)
    
    def check_answer(self):
        selected_option = self.var.get()
        if selected_option == self.questions[self.current_question]["answer"]:
            self.score += 1
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            messagebox.showinfo("Risultato", f"Hai risposto correttamente a {self.score} domande su {len(self.questions)}")
            self.root.quit()
    
    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question]["question"])
        self.var.set(None)
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            self.options[i].config(text=option, value=option)

if __name__ == "__main__":
    root = tk.Tk()
    quiz_folder = "quiz_generati"
    quiz_files = [os.path.join(quiz_folder, file) for file in os.listdir(quiz_folder) if file.endswith(".json")]
    app = QuizApp(root, quiz_files)
    root.mainloop()




#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.