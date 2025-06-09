from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BLACK = "#000"
CANVAS_X = 350
CANVAS_Y = 450
SCORE_FONT = ("Arial", 12, "normal")
QUESTION_FONT = ("Arial", 14, "italic")
TIME_DELAY = 1000  # milliseconds


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, padx=5, pady=10)
        self.score_label.grid(row=0, column=1)

        # White canvas for question text
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        # Question text
        self.canvas_question = self.canvas.create_text(150, 125, text="", font=QUESTION_FONT, width=280, fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)  # add padding above and below the canvas

        # Create images for the buttons
        tick_image = PhotoImage(file="./images/true.png", height=97, width=100)
        cross_image = PhotoImage(file="./images/false.png", height=97, width=100)

        # Buttons
        self.true_button = Button(image=tick_image, width=100, height=97, command=self.answer_true, highlightthickness=0, bd=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=cross_image, width=100, height=97, command=self.answer_false, highlightthickness=0, bd=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.questions_total}")

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text=question_text)
        else:
            self.canvas.itemconfig(self.canvas_question, text="You've reached the end of the quiz!")
            self.score_label.config(text=f"Final score: {self.quiz.score} / {self.quiz.questions_total}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        background_colour =  "green" if is_right else "red"
        self.canvas.config(bg=background_colour)

        self.window.after(TIME_DELAY, self.get_next_question)
