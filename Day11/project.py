#  BlackJack Project -> CapStone Project


import random;

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0;
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards);


def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10];
    card = random.choice(cards)
    return card;

def compare_scores(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose! Opponent has BlackJack."
    elif user_score == 0:
        return "Wins! with a BlackJack"
    elif user_score > 21:
        return "You went Over. You Lose."
    elif comp_score > 21:
        return "Opponent went Over. You Win."
    elif user_score > comp_score:
        return "You Win"
    else:
        return "you Lose"



def play_game():
    user_cards = [];
    computer_cards = [];
    is_game_over = False

    for _ in range(2):
        new_card = deal_cards()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are {user_cards} and your score is {user_score}")
        print(f"computer first card is {computer_cards[0]}");
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True;
        else:
            user_should_deal = input("Type 'y' for another card or 'n' for pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True;        

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards are {user_cards} and Final score is {user_score}")
    print(f"Computer cards are {computer_cards} and Final score is {computer_score}")
    print(compare_scores(user_score, computer_score))  


while input("Do you want to Playa game of BlackJack. Type 'y' to play: ") == 'y':
    play_game();