# Number Guessing Game
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. your answer is {answer}")  

def difficulty():
    diff = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL    


def game():

    print("Welcome to the Number Guessing Game\n I'm thinking of a Number between 1 and 100")
    answer = randint(1,100)

    turns = difficulty()


    user_guess = 0

    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        user_guess = int(input("Make a Guess: "))

        turns = check_answer(user_guess,answer,turns)

        if turns == 0:
            print("You have run out of attempts. You Lose.")
            return
        elif user_guess != answer:
            print("Guess Again")

game();