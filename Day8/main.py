#  Functions with parameters

# def func(name):
#     print(f"Hello {name}");
#     print(f"How do you do {name}?")

# func("Mouli");    

#  Functions with positional arguments and keywords with two inputs

# def func(name, loc):
#     print(f"Hello {name}");
#     print(f"How do you do {loc}?")

# func("Mouli","Vizag");

#  Painting Problem

# import math;

# test_h = int(input("Enter the height: "))
# test_w = int(input("Enter the width: "))

# coverage = 5

# def print_cans(height, weight, cover):
#     area = height * weight
#     print(math.ceil( area / cover))

# print_cans(test_h, test_w, coverage);

#  Prime number

n = int(input("Enter a number: "))

def prime(number):
    if number == 2:
        print("Prime")
    elif number % 2 == 0:
        print(" Not a Prime Number")
    else:
        print("Prime")   

prime(n)

