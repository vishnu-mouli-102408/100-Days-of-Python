#  Hangman Project

import random;

from hangman_words import word_list;
from hangman_art import stages, logo;

chosen_word = random.choice(word_list);

print(logo);

lives = 6

display = [];
for _ in range(len(chosen_word)):
    display += "_";
print(display);

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position];
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You have guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1;
        if lives == 0:
            end_of_game = True
            print("You Lose")
            print(f"The correct word is {chosen_word}")   

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(stages[lives]);    