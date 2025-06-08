import random
from hangman_art import stages
from hangman_words import word_list

lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("\nWord to guess: " + placeholder)

game_over = False
correct_letters = []
chosen_letters = []

# Loop through user input until the end of the game
while not game_over:

    print(f"*************************** {lives}/6 LIVES LEFT ***************************")
    guess = input("Guess a letter: ").lower().strip()

    if len(guess) > 1:
        print(f"You entered more than one character! Please enter a single letter.")
        continue

    if not guess.isalpha():
        print(f"You entered '{guess}', which is not a letter! Please try again.")
        continue

    if guess in chosen_letters:
        print(f"You have already chosen letter '{guess}'. Please try again.")
        continue

    # Store the letter
    chosen_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed letter {guess}, which is not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"********************** YOU LOSE *********************")
            print(f"The word you were trying to guess was: {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("*************************** YOU WIN ***************************")

    # Display the hangman image
    print(stages[lives])
