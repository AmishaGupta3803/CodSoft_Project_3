from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.question = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Amazon acquired Twith in August",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        right_button_img = PhotoImage(file="images/true.png")
        wrong_button_img = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_button_img, borderwidth=0, highlightthickness=0, command=self.true_button_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong_button_img, borderwidth=0, highlightthickness=0, command=self.false_button_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.question.still_has_questions():
            self.score_label.config(text=f"Score: {self.question.score}")
            qtext = self.question.next_question()
            self.canvas.itemconfig(self.question_text, text=qtext)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button_pressed(self):
        is_right = self.question.check_answer("True")
        self.feedback(is_right)

    def false_button_pressed(self):
        is_right = self.question.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

