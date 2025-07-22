from wordlist import wordlist
import random
from tkinter import *
from tkinter import messagebox
import string

def guess_letter(guess_letter, button):
    global img
    global player_life
    if guess_letter in guessed_letters:
        pass
    elif guess_letter in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess_letter:
                word_display_list[i] = guess_letter
                guessed_letters.append(guess_letter)
                button.config(state=DISABLED)
        word_label.config(text=" ".join(word_display_list))
        if "_" not in word_display_list:
            messagebox.showinfo(title="You Won!", message="Congrats!")
    else:
        button.config(state=DISABLED)
        player_life += 1
        img = PhotoImage(file=f"images/{player_life}.png")
        image_display.config(image=img)
        if player_life >= 7:
            messagebox.showinfo(title="Game Over", message=f"The word is {word_to_guess}")

player_life = 1
word_to_guess = random.choice(wordlist).upper()
word_display_list = []
guessed_letters = []

for letter in word_to_guess:
    word_display_list.append('_')

window = Tk()
window.title("Hangman")
window.configure(bg='white')

title = Label(window, text="Hangman", bg='white', font=('arial', 20))
title.grid(column=0, row=0, columnspan=2)

word_label = Label(window, text=" ".join(word_display_list), bg='white', font=('arial', 20))
word_label.grid(column=0, row=2)
img = PhotoImage(file=f"images/{player_life}.png")
image_display = Label(window, image=img, bg='white')
image_display.grid(column=0, row=1)

button_frame = Frame(window, bg='white')
button_frame.grid(column=0, row=3, pady=20)

letters = string.ascii_uppercase
first = letters[:13]
second = letters[13:]

for index, letter in enumerate(first):
    btn = Button(button_frame, text=letter, bg='white', fg='black', font=('arial', 20))
    btn.config(command = lambda l=letter, b=btn: guess_letter(l, b))
    btn.grid(column=index, row=0)

for index, letter in enumerate(second):
    btn = Button(button_frame, text=letter, bg='white', fg='black', font=('arial', 20))
    btn.config(command=lambda l=letter, b=btn: guess_letter(l, b))
    btn.grid(column=index, row=1)

window.mainloop()