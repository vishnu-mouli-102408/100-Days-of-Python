print("Welcome to Treasure Island\n Your mission is to find the Treasure")

x = input("You are at cross roads. where do you wanna go? Left or Right : ").lower()

if x == "left":
    y = input("You are at a lake.There is an Island in the middle of the lake.Type 'wait' to wait for a boat.Type 'swim' to swim across. ").lower()
    if y == "wait":
        z = input("you arrive at the Island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose? ").lower()
        if z == "yellow":
            print("Yay! you won. Congratulations")
        else:
            print("You entered into a beast. Game Over") 
    else:
        print("Oops! Sorry. Game Over")
else:
    print("Oops! Sorry. Game Over")                  
