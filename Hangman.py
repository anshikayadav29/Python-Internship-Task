import random

words = ['apple', 'banana', 'orange', 'grapes', 'mango']
word = random.choice(words)

guessed_letters = []
attempts = 6
display_word = ['_'] * len(word)

while attempts > 0 and '_' in display_word:
    print(' '.join(display_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1

if '_' not in display_word:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)