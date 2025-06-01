import tkinter as tk

class AIGuessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Tebak Angka")
        self.reset_game()

        # UI Elements
        self.label = tk.Label(root, text="Pikirkan angka dari 1 sampai 100", font=("Arial", 14))
        self.label.pack(pady=10)

        self.guess_label = tk.Label(root, text="", font=("Arial", 20))
        self.guess_label.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.smaller_btn = tk.Button(btn_frame, text="Terlalu besar 🔽", command=self.too_big)
        self.smaller_btn.grid(row=0, column=0, padx=10)

        self.correct_btn = tk.Button(btn_frame, text="Benar ✅", command=self.correct)
        self.correct_btn.grid(row=0, column=1, padx=10)

        self.bigger_btn = tk.Button(btn_frame, text="Terlalu kecil 🔼", command=self.too_small)
        self.bigger_btn.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(root, text="", font=("Times New Roman", 14))
        self.result_label.pack(pady=10)

        self.history_label = tk.Label(root, text="", font=("Courier", 10))
        self.history_label.pack()

        self.stats_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.stats_label.pack(pady=10)

        self.restart_btn = tk.Button(root, text="Main Lagi 🔄", command=self.restart_game, state=tk.DISABLED)
        self.restart_btn.pack(pady=10)

        self.make_guess()

    def reset_game(self):
        self.min = 1
        self.max = 100
        self.guess = None
        self.history = []
        self.attempts = 0

    def make_guess(self):
        if self.min > self.max:
            self.guess_label.config(text="Kamu curang ya? 😅")
            return
        self.guess = (self.min + self.max) // 2
        self.history.append(self.guess)
        self.attempts += 1
        self.guess_label.config(text=f"AI menebak: {self.guess}")
        self.history_label.config(text="Riwayat tebakan: " + ', '.join(map(str, self.history)))

    def too_small(self):
        self.min = self.guess + 1
        self.make_guess()

    def too_big(self):
        self.max = self.guess - 1
        self.make_guess()

    def correct(self):
        self.guess_label.config(text=f"Yay! AI benar: {self.guess} 🎉")
        self.smaller_btn.config(state=tk.DISABLED)
        self.bigger_btn.config(state=tk.DISABLED)
        self.correct_btn.config(state=tk.DISABLED)
        self.restart_btn.config(state=tk.NORMAL)

        # Tampilkan statistik
        self.show_stats()

    def show_stats(self):
        accuracy = round(1 / self.attempts, 3) if self.attempts > 0 else 0
        stats = (
            f"📊 Statistik:\n"
            f"- Jumlah tebakan: {self.attempts}\n"
            f"- Rentang terakhir: {self.min} - {self.max}\n"
            f"- Akurasi tebakan: {accuracy}"
        )
        self.stats_label.config(text=stats)

    def restart_game(self):
        self.reset_game()
        self.smaller_btn.config(state=tk.NORMAL)
        self.bigger_btn.config(state=tk.NORMAL)
        self.correct_btn.config(state=tk.NORMAL)
        self.result_label.config(text="")
        self.stats_label.config(text="")
        self.history_label.config(text="")
        self.restart_btn.config(state=tk.DISABLED)
        self.make_guess()

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AIGuessApp(root)
    root.mainloop()
