import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample texts for typing test
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language used for various applications.",
    "Typing speed tests help improve your accuracy and efficiency.",
    "Consistent practice leads to better typing performance over time."
]


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.start_time = None

        # Label for instruction
        self.label = tk.Label(root, text="Type the text below as fast as you can:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Display sample text
        self.text_label = tk.Label(root, text=self.sample_text, font=("Arial", 12), wraplength=500, justify="center")
        self.text_label.pack(pady=10)

        # Entry widget for user input
        self.text_entry = tk.Text(root, height=5, width=60, font=("Arial", 12))
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<FocusIn>", self.start_timer)

        # Submit button
        self.submit_button = tk.Button(root, text="Check Speed", command=self.calculate_speed)
        self.submit_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showwarning("Warning", "Start typing to begin the test!")
            return

        end_time = time.time()
        elapsed_time = end_time - self.start_time
        user_text = self.text_entry.get("1.0", tk.END).strip()

        word_count = len(user_text.split())
        wpm = round((word_count / elapsed_time) * 60)

        self.result_label.config(text=f"Your typing speed: {wpm} words per minute")

        self.start_time = None  # Reset timer for next test


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
