# import tkinter as tk
from tkinter import *

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def on_click(char):
    current = user_entry.get()
    user_entry.delete(0, END)
    user_entry.insert(0, current + char)

def clear():
    user_entry.delete(0, END)

def calculate():
    try:
        result = eval(user_entry.get())
        user_entry.delete(0, END)
        user_entry.insert(0, str(result))
    except:
        user_entry.delete(0, END)
        user_entry.insert(0, "Error")


#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

# GUI setup
window = Tk()
window.title("Calculator")
window.geometry("340x450")

user_entry = Entry(window, font=("Arial", 20), borderwidth=8, justify='right')
user_entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Layout the keyboard
row = 1
col = 0
for button in buttons:
    action = lambda x=button: calculate() if x == '=' else on_click(x)
    Button(window, text=button, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 2

# Add space above 'Clear' button
status_label = Label(window, text="")
status_label.grid()

Button(window, text="Clear", width=22, height=2, font=("Arial", 14), command=clear).grid(row=row, column=0, columnspan=4)

window.mainloop()
