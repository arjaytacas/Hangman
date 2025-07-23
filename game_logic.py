from wordlist import wordlist
import random
import string
from tkinter import *
from tkinter import messagebox

class Hangman:
    def __init__(self, window):
        self.window = window
        self.window.title("Hangman")
        self.window.configure(bg='white')

        # initialize game
        self.player_life = 1
        self.word_to_guess = random.choice(wordlist).upper()
        self.word_display_list = []
        self.guessed_letters = []

        self.setup_ui()

    def setup_ui(self):
        for letter in self.word_to_guess:
            self.word_display_list.append("_")
        self.title = Label(self.window, text="Hangman", bg='white', font=('arial', 20))
        self.title.grid(column=0, row=0, columnspan=2)
        self.word_label = Label(self.window, text=" ".join(self.word_display_list), bg='white', font=('arial', 20))
        self.word_label.grid(column=0, row=2)
        self.img = PhotoImage(file=f"images/{self.player_life}.png")
        self.image_display = Label(self.window, image=self.img, bg='white')
        self.image_display.grid(column=0, row=1)

        self.create_buttons()

    def guess_letter(self, guess_letter, btn):
        if guess_letter in self.guessed_letters:
            pass
        elif guess_letter in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess_letter:
                    self.word_display_list[i] = guess_letter
                    self.guessed_letters.append(guess_letter)
                    btn.config(state=DISABLED)
            self.word_label.config(text=" ".join(self.word_display_list))
            if "_" not in self.word_display_list:
                messagebox.showinfo(title="You Won!", message="Congrats!")
        else:
            btn.config(state=DISABLED)
            self.player_life += 1
            self.img = PhotoImage(file=f"images/{self.player_life}.png")
            self.image_display.config(image=self.img)
            if self.player_life >= 7:
                messagebox.showinfo(title="Game Over", message=f"The word is {self.word_to_guess}")

    def create_buttons(self):
        self.button_frame = Frame(self.window, bg='white')
        self.button_frame.grid(column=0, row=3, pady=20)

        letters = string.ascii_uppercase
        first = letters[:13]
        second = letters[13:]

        for index, letter in enumerate(first):
            btn = Button(self.button_frame, text=letter, bg='white', fg='black', font=('arial', 20))
            btn.config(command=lambda l=letter, b=btn: self.guess_letter(l, b))
            btn.grid(column=index, row=0)

        for index, letter in enumerate(second):
            btn = Button(self.button_frame, text=letter, bg='white', fg='black', font=('arial', 20))
            btn.config(command=lambda l=letter, b=btn: self.guess_letter(l, b))
            btn.grid(column=index, row=1)