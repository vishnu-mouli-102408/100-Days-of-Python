#  Tip Calculator

print("Welcome to the Tip Calculator");

x = input("What was the total bill?");

x_int = float(x);

tip = input("What percentage tip would you like to give? 10, 12 or 15?");

tip_int = float(tip);

people = input("How many people to split the bill?")

people_int = int(people);
x = ((x_int * tip_int) / 100)

total_amount = round( (x_int + x) / people_int, 2);

print(f"Each one should pay: {total_amount}");
