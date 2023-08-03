import random;


paper = "✋🏻";
rock = "✊🏿";
scissors = "✌️"

li = [paper, rock, scissors]

number = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. ")
int_number = int(number);

random_number = random.randint(0,2)

print(f"computer choose {random_number}")

if int_number == random_number:
    print(f"You choose {li[int_number -1]} and computer choose {li[random_number -1]}, It's a Tie.")
elif int_number >=3 or int_number <0:
    print("You typed an Invalid Number, You Lose")    
elif int_number == 0 and random_number == 1:
    print ( f"You chose {rock}, Computer chose {paper}. You Lose.")
elif int_number == 0 and random_number == 2:
    print ( f"You chose {rock}, Computer chose {scissors}. You Win.")
elif int_number == 1 and random_number == 0:
    print ( f"You chose {paper}, Computer chose {rock}. You Win.")
elif int_number == 1 and random_number == 2:
    print ( f"You chose {paper}, Computer chose {scissors}. You Lose.")
elif int_number == 2 and random_number == 0:
    print ( f"You chose {scissors}, Computer chose {rock}. You Lose.")
elif int_number == 2 and random_number == 1:
    print ( f"You chose {scissors}, Computer chose {paper}. You Win.")
