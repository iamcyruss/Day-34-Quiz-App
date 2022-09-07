from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # main gui
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # card with white background
        self.card = Canvas(width=300, height=250, highlightthickness=0)
        self.card.grid(column=0, row=1, columnspan=2, pady=50)
        # card joke
        self.joke = self.card.create_text(150,
                                          125,
                                          text="Some question text.",
                                          fill=THEME_COLOR,
                                          font=("Arial", 20, "italic")
                                          )
        # buttons
        self.true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true, command=lambda: self.quiz)
        self.true_button.grid(column=0, row=2)
        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false, command=lambda: self.quiz)
        self.false_button.grid(column=1, row=2)
        # score
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.card.itemconfig(self.joke, text=q_text)
