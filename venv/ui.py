from tkinter import *
from data import question_data
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        # main gui
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # card with white background
        self.card = Canvas(width=300, height=250, highlightthickness=0)
        self.card.grid(column=0, row=1, columnspan=2)
        # card joke
        self.joke = self.card.create_text(150, 125, text="", font=("Arial", 20, "italic"))
        # buttons
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true, command=QuizBrain().next_question)
        self.false_button = Button(image=self.false, command=QuizBrain().next_question)
        # score
        self.score = Label(text="Score: 0")
        self.score.grid(columnspan=1, row=0)


        self.window.mainloop()

