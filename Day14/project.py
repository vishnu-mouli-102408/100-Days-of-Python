#  Higher Lower start game
# importing the random module
import random

# Importing game data
from game_data import data

def format(account):
    account_name = account["name"]  
    account_desc = account["description"]    
    account_country = account["country"] 
    return f"{account_name}, a {account_desc}, from {account_country}"

def ans_check(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0

account_b = random.choice(data)
game_cont = True

while game_cont:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)}")
    print("VS")
    print(f"Against B: {format(account_b)}")


    #  ask user to guess 

    inp = input("Who has more followers. Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = ans_check(inp, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are Right!. Your current score is {score}")
    else:
        print(f"Sorry you are Wrong. Final score is {score}")   
        game_cont = False 