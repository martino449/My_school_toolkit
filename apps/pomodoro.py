import tkinter as tk
from tkinter import messagebox
import threading
import winsound
import os
import time

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.study_time = 25  # Default study time in minutes
        self.break_time = 5   # Default break time in minutes
        self.sessions = 4     # Default number of sessions

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Pomodoro Timer", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Subject Entry
        self.subject_label = tk.Label(self.root, text="Materia:")
        self.subject_label.pack(pady=5)
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.pack(pady=5)

        # Study Time
        self.study_time_label = tk.Label(self.root, text="Tempo di studio (minuti):")
        self.study_time_label.pack(pady=5)
        self.study_time_entry = tk.Entry(self.root)
        self.study_time_entry.insert(0, str(self.study_time))
        self.study_time_entry.pack(pady=5)

        # Break Time
        self.break_time_label = tk.Label(self.root, text="Tempo di pausa (minuti):")
        self.break_time_label.pack(pady=5)
        self.break_time_entry = tk.Entry(self.root)
        self.break_time_entry.insert(0, str(self.break_time))
        self.break_time_entry.pack(pady=5)

        # Number of Sessions
        self.sessions_label = tk.Label(self.root, text="Numero di sessioni:")
        self.sessions_label.pack(pady=5)
        self.sessions_entry = tk.Entry(self.root)
        self.sessions_entry.insert(0, str(self.sessions))
        self.sessions_entry.pack(pady=5)

        # Time Remaining
        self.time_remaining_label = tk.Label(self.root, text="Tempo rimanente: N/A")
        self.time_remaining_label.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(self.root, text="Stato: Inattivo")
        self.status_label.pack(pady=10)

        # Start Button
        start_button = tk.Button(self.root, text="Inizia", command=self.start_pomodoro)
        start_button.pack(pady=20)

    def start_pomodoro(self):
        try:
            self.study_time = int(self.study_time_entry.get())
            self.break_time = int(self.break_time_entry.get())
            self.sessions = int(self.sessions_entry.get())

            if self.study_time <= 0 or self.break_time <= 0 or self.sessions <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Errore", "Per favore, inserisci valori numerici positivi validi.")
            return
        
        subject = self.subject_entry.get()
        if not subject:
            messagebox.showerror("Errore", "Per favore, inserisci una materia.")
            return

        self.status_label.config(text="Stato: In corso")
        self.sessions_remaining = self.sessions
        self.run_next_session(subject)

    def run_next_session(self, subject):
        if self.sessions_remaining > 0:
            self.run_pomodoro_session(subject, self.study_time, self.break_time)
        else:
            self.status_label.config(text="Stato: Completato")
            messagebox.showinfo("Pomodoro", "Hai completato tutte le sessioni!")

    def run_pomodoro_session(self, subject, study_time, break_time):
        self.current_phase = "study"
        self.phase_time = study_time * 60
        self.update_time_remaining()

        def run_session():
            while self.phase_time > 0:
                if self.current_phase == "study":
                    time.sleep(1)
                    self.phase_time -= 1
                else:
                    time.sleep(1)
                    self.phase_time -= 1

            self.play_sound('sounds\\alarm.wav')
            if self.current_phase == "study":
                self.current_phase = "break"
                self.phase_time = break_time * 60
                self.show_message(f"Tempo di studio per '{subject}' terminato. Inizio pausa di {break_time} minuti.")
            else:
                self.current_phase = "study"
                self.phase_time = study_time * 60
                self.show_message("Pausa terminata. Inizio nuova sessione di studio.")
                self.sessions_remaining -= 1
                self.run_next_session(subject)
                
        threading.Thread(target=run_session).start()

    def update_time_remaining(self):
        if self.current_phase == "study":
            phase_label = "Studio"
        else:
            phase_label = "Pausa"

        minutes, seconds = divmod(self.phase_time, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        self.time_remaining_label.config(text=f"Tempo rimanente ({phase_label}): {time_str}")
        self.root.after(1000, self.update_time_remaining)

    def play_sound(self, file_path):
        if os.path.exists(file_path):
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        else:
            messagebox.showerror("Errore", f"Il file {file_path} non è stato trovato.")

    def show_message(self, message):
        self.root.after(0, lambda: messagebox.showinfo("Pomodoro", message))

# Crea la finestra principale
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.