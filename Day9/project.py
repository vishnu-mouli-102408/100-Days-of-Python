#  Auction Bidding



x = {}
bidding_finished = False


def highest_bid(x):
    high = 0;
    winner = ""
    for key in x:
        if x[key] > high:
            high = x[key]
            winner = key;
    print(f"The winner is {winner} and the Highest bid is {high}")


while not bidding_finished:
    name = input("Enter your name: ")
    bid = int(input("Enter you Bid Amount: "))

    x[name] = bid;
    y = input("Would you like to add another user. Type 'Yes' or 'No': ").lower()
    if y == "no":
        bidding_finished = True
        highest_bid(x);







