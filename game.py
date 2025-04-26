from tkinter import *
import random

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("The RPS")
        self.root.wm_geometry("420x540+50+50")
        self.root.configure(background='silver')

        self.user_score = 0
        self.computer_score = 0

        self.l1 = Label(master=self.root, text="Welcome Player", font=('Algerian', 18, 'bold'), background="silver",fg="darkslateblue")
        self.l1.place(x=60, y=10, width=280, height=30)
        self.l2 = Label(master=self.root, text="Choose Rock, Paper, or Scissors:", font=('Centaur', 18, 'bold'), background="silver")
        self.l2.place(x=20, y=55, width=380, height=30)

        self.user_choice_label = Label(master=self.root, text="You chose: ", font=('Calibri', 18), background="silver")
        self.user_choice_label.place(x=20, y=105, width=380, height=30)
        self.computer_choice_label = Label(master=self.root, text="Computer chose: ", font=('Calibri', 18), background="silver")
        self.computer_choice_label.place(x=20, y=145, width=380, height=30)
        self.result_label = Label(master=self.root, text="Result: ", font=('Calibri', 18), background="silver")
        self.result_label.place(x=20, y=185, width=380, height=30)
        self.score_label = Label(master=self.root, text=f"Score - You: {self.user_score}, Computer: {self.computer_score}",
                                 font=('Calibri', 18), background="silver")
        self.score_label.place(x=20, y=225, width=380, height=30)

        self.btr = Button(master=self.root, text="Rock", font=('Consolas', 18, 'bold'), background="darkgoldenrod",
                          command=lambda: self.play("Rock"))
        self.btr.place(x=20, y=300, width=100, height=50)
        self.btp = Button(master=self.root, text="Paper", font=('Consolas', 18, 'bold'), background="ivory",
                          command=lambda: self.play("Paper"))
        self.btp.place(x=150, y=300, width=100, height=50)
        self.bts = Button(master=self.root, text="Scissors", font=('Consolas', 18, 'bold'), background="coral",
                          command=lambda: self.play("Scissors"))
        self.bts.place(x=280, y=300, width=120, height=50)
        self.btre = Button(master=self.root, text="Reset", font=('Consolas', 18, 'bold'), background="darkturquoise",
                           command=self.reset_game)
        self.btre.place(x=120, y=380, width=160, height=50)

    def computer_choice(self):
        return random.choice(['Rock', 'Paper', 'Scissors'])

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == 'Rock' and computer == 'Scissors') or \
                (user == 'Scissors' and computer == 'Paper') or \
                (user == 'Paper' and computer == 'Rock'):
            return "You win!"
        else:
            return "You lose!"

    def play(self, user_choice):
        comp_choice = self.computer_choice()
        result = self.determine_winner(user_choice, comp_choice)

        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.user_choice_label.config(text=f"You chose: {user_choice}")
        self.computer_choice_label.config(text=f"Computer chose: {comp_choice}")
        self.result_label.config(text=f"Result: {result}")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_choice_label.config(text="You chose: ")
        self.computer_choice_label.config(text="Computer chose: ")
        self.result_label.config(text="Result: ")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Gui()
    app.run()