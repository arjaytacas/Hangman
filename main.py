from wordlist import wordlist
import random

player_life = 6
word_to_guess = random.choice(wordlist).lower()
word_display_list = []
guessed_letters = []

for letter in word_to_guess:
    word_display_list.append('_')

print(f'word: {"".join(word_display_list)}')
print(f'You have {player_life} live/s.')

while '_' in word_display_list:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in guessed_letters:
        pass
    elif guess_letter in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess_letter:
                word_display_list[i] = guess_letter
    else:
        player_life -= 1
        if player_life <= 0:
            break

    word_display = ''.join(word_display_list).upper()
    print(f'Word: {word_display}')
    print(f'You have {player_life} live/s.')

if '_' not in word_display_list:
    print('Congrats, you won!')
else:
    print('Sorry, you lost!')
    print(f'The word was: {word_to_guess}')