from tkinter import *
import pandas as pd
import random
import os

# Create the main window
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg="#B1DDC6")

# Load images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Load the data, checking if words_to_learn.csv exists
if os.path.exists("data/words_to_learn.csv"):
    data = pd.read_csv("data/words_to_learn.csv")
else:
    data = pd.read_csv("data/french_words.csv")

word_list = data.to_dict(orient="records")

# Global variables
current_english_word = ""
timer = None


# Function to flip the card
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(canvas_text_title, text="English", fill="white")
    canvas.itemconfig(canvas_text_word, text=current_english_word, fill="white")


# Function to pick a new random word
def next_card():
    global timer
    if timer:
        window.after_cancel(timer)

    word_pair = random.choice(word_list)
    french_word = word_pair["French"]
    english_word = word_pair["English"]

    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(canvas_text_title, text="French", fill="black")
    canvas.itemconfig(canvas_text_word, text=french_word, fill="black")

    global current_english_word
    current_english_word = english_word

    timer = window.after(3000, flip_card)


# Function to remove known words
def is_known():
    global word_list
    # Get the current French and English words
    current_french_word = canvas.itemcget(canvas_text_word, "text")

    # Filter out the known word pair
    word_list = [word for word in word_list if word["French"] != current_french_word]

    # Save the updated word list to words_to_learn.csv
    pd.DataFrame(word_list).to_csv("data/words_to_learn.csv", index=False)

    # Show the next card
    next_card()


# Create Canvas for the flashcard
canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas_text_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_text_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Add Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Initialize the first card
next_card()

# Start the Tkinter event loop
window.mainloop()
