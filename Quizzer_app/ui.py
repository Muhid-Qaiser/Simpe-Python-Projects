from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(string='Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, highlightthickness=0,
                                 fg='white', font=('Courier', 20, 'normal'))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(
            150, 124,
            width=280,
            text='Some text here',
            fill='black',
            font=('Ariel', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg='green')
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)
