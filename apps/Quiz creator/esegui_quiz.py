import json
import tkinter as tk
from tkinter import messagebox
import ctypes



def hide_console() -> None:
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE
 
 
hide_console()



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Grafico")
        
        with open("quiz.json", "r") as file:
            self.questions = json.load(file)
        
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
    app = QuizApp(root)
    root.mainloop()





#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.