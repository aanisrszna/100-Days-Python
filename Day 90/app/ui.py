import tkinter as tk
from app.timer import WritingTimer

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        self.root.geometry("600x400")

        self.text_widget = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text_widget.pack(expand=True, fill="both", padx=10, pady=10)
        self.text_widget.bind("<KeyPress>", self.reset_timer)

        self.timer = WritingTimer(self.clear_text)
        self.timer.start_timer()

    def reset_timer(self, event=None):
        """Resets the timer whenever a key is pressed"""
        self.timer.start_timer()

    def clear_text(self):
        """Clears the text area when time runs out"""
        self.text_widget.delete("1.0", tk.END)
