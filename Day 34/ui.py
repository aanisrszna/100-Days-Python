from tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Main window setup
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14))
        self.score_label.grid(row=0, column=1)

        # Canvas for Question Text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # Allow text wrapping
            text="",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Load images for buttons
        true_image_path = os.path.join("images", "true.png")
        false_image_path = os.path.join("images", "false.png")

        true_image = PhotoImage(file=true_image_path)
        false_image = PhotoImage(file=false_image_path)

        # True Button
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.image = true_image  # To prevent garbage collection
        self.true_button.grid(row=2, column=0)

        # False Button
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.image = false_image
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):

        """Fetch the next question and display it on the canvas."""
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz!"
            )
            # Disable buttons when the quiz ends
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Handles the True button press."""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Handles the False button press."""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Provide feedback to the user and fetch the next question."""
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")  # Update score label
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_canvas)

    def reset_canvas(self):
        """Reset the canvas color and fetch the next question."""
        self.canvas.config(bg="white")
        self.get_next_question()
