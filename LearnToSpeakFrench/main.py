import os
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFF"
BLACK="#000"
TITLE_FONT = ("Verdana", 26, "italic")
WORD_FONT = ("Verdana", 44, "bold")
CANVAS_X = 850
CANVAS_Y = 570
DELAY_SECONDS = 3

FRENCH_LIST = "./data/french_words.csv"
TO_LEARN_LIST = "./data/words_still_to_learn.csv"

# Cards
FRONT = "./images/card_front.png"
BACK = "./images/card_back.png"
# Buttons
WRONG = "./images/wrong.png"
RIGHT = "./images/right.png"

french_word = ""
english_word = None
timer_control = None
word_index = None

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def generate_random_word():
    global french_word
    global english_word
    global word_index
    previous_french_word = french_word
    # All cards removed?
    if len(french_list) == 0:
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(canvas_title, text="", fill=BLACK)
        canvas.itemconfig(canvas_word, text="There are no\nmore cards left!", fill=BLACK)

    else:
        while True:
            word_index = random.randint(0, len(french_list) - 1)
            french_word = french_list[word_index][0]
            english_word = french_list[word_index][1]
            if french_word != previous_french_word or len(french_list) == 1:
                break

        show_card("French")
        timer(DELAY_SECONDS)

def show_card(country):
    global french_word
    global english_word
    # Update canvas
    if country == "English":
        canvas.itemconfig(canvas_image, image=back_image)
        canvas.itemconfig(canvas_title, text="English", fill=WHITE)
        canvas.itemconfig(canvas_word, text=english_word, fill=WHITE)
    elif country == "French":
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(canvas_title, text="French", fill=BLACK)
        canvas.itemconfig(canvas_word, text=french_word, fill=BLACK)

def save_updated_list_of_words(new_list):
    # Save to file if words left, else delete file
    if len(new_list) > 0:
        with open(TO_LEARN_LIST, mode="w") as csv_file:
            csv_file.write("French,English\n")
            for name in new_list:
                row = f"{name[0]},{name[1]}\n"
                csv_file.write(row)
    else:
        os.remove(TO_LEARN_LIST)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(count_seconds):
    global timer_control
    if count_seconds > 0:
        # Start timer, wait 'count_seconds' seconds
        timer_control = window.after(1000 * count_seconds, timer, 0)
    else:
        # Stop timer
        show_card("English")
        window.after_cancel(timer_control)

# ---------------------------- BUTTON FUNCTIONS ------------------------------- #
def wrong():
    if len(french_list) > 0:
        timer(0)
        generate_random_word()

def remove():
    # Remove card from list and go to next
    if len(french_list) > 0:
        timer(0)
        french_list.pop(word_index)
        save_updated_list_of_words(french_list)
        generate_random_word()

#===============================================#
#================== UI SETUP ===================#
#===============================================#

window = Tk()
window.title("Learn to speak French")
window.config(padx=10, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(height=CANVAS_Y, width=CANVAS_X, bg=BACKGROUND_COLOR, highlightthickness=0)
# Set up the images
front_image = PhotoImage(file=FRONT, height=526, width=800)
back_image = PhotoImage(file=BACK, height=526, width=800)
wrong_image = PhotoImage(file=WRONG, width=100, height=100)
right_image = PhotoImage(file=RIGHT, width=100, height=100)
# Set up the canvas - with an image and text
canvas_image = canvas.create_image(CANVAS_X / 2, CANVAS_Y / 2, image=front_image)
canvas_title = canvas.create_text(CANVAS_X / 2, 180,text="", font=TITLE_FONT, fill=BLACK)
canvas_word = canvas.create_text(CANVAS_X / 2, 280,text="", font=WORD_FONT, fill=BLACK)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_image, width=99, height=99, command=wrong, highlightthickness=0, bd=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, width=99, height=99, command=remove, highlightthickness=0, bd=0)
right_button.grid(row=1, column=1)

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

try:
    data = pandas.read_csv(TO_LEARN_LIST)
except:
    data = pandas.read_csv(FRENCH_LIST)

# Create a Dictionary from word list
french_dict = {row.French: row.English for (index, row) in data.iterrows()}
print(french_dict)
# Convert to a List
french_list = list(french_dict.items())
print(french_list)

generate_random_word()


# Keep at the bottom of the program
window.mainloop()