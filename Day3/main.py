#  Check whether the number is odd or even

# number = int(input("Enter a number: "));

# if number % 2 == 0:
#     print("Even"); # If it's divisible by two, then its an Even Number.
# else:
#     print("Odd")


# nested statements and elif     

# height = int(input("Enter a number :"));

# if height >= 120:
#     age = int(input("Enter your age :"))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry! You are not eligible to vote.")


#  upgraded BMI Calculator

# height = float(input("Enter your height :"))
# weight = int(input("Enter your weight :"))

# BMI = round(weight/(height ** 2))

# if BMI < 28:
#     print("You are at the correct BMI")
# elif BMI < 40:
#     print("You are slightly overweight")
# elif BMI < 60:
#     print("You are Overweight")
# else:
#     print("You are obese!")


# print(BMI)
 
#   Finding Leap Year

# year = int(input("Enter a year :"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Its a Leap Year")
#         else:
#             print("Its not a Leap Year")        
#     else:
#         print("It's a leap year");
# else:
#     print("Its not a Leap Year")        
         

# Pizza Delivery Problem

# print("Welcome to the Pizza Delivery")

# size = input("What size pizza do you want? ") #  S , M , L, 
# add_pepporoni = input("Do you want to add pepporoni? ") # Y or N
# extra_cheese = input("Do you want to add extra cheese? ") # Y or N

# final_bill = 0;

# if size == "S":
#     final_bill += 15
# elif size == "M":
#     final_bill += 20
# elif size == "L":
#     final_bill += 25

# if add_pepporoni == "Y":
#     if size == "S":
#         final_bill += 2
#     else:
#         final_bill += 3
# if extra_cheese == "Y":
#     final_bill += 1;

# print(f"Your final bll is {final_bill}")  


# if size == "S":
#     final_bill = 15
#     if add_pepporoni == "Y":
#         final_bill += 2
#     if extra_cheese == "Y":
#         final_bill += 1
#     if add_pepporoni == "N":
#         final_bill = final_bill
#     if extra_cheese == "N":
#         final_bill = final_bill
#     print(f"Your final bll is {final_bill}")    
# elif size == "M":
#     final_bill = 20
#     if add_pepporoni == "Y":
#         final_bill += 3
#     if extra_cheese == "Y":
#         final_bill += 1
#     if add_pepporoni == "N":
#         final_bill = final_bill
#     if extra_cheese == "N":
#         final_bill = final_bill
#     print(f"Your final bll is {final_bill}")     
# else:
#     final_bill = 25
#     if add_pepporoni == "Y":
#         final_bill += 3
#     if extra_cheese == "Y":
#         final_bill += 1
#     if add_pepporoni == "N":
#         final_bill = final_bill
#     if extra_cheese == "N":
#         final_bill = final_bill  
#     print(f"Your final bll is {final_bill}")       
# 
# 
# 
# Love Calculator


print("Welcome to the Love Calculator")

name1 = input("What is your name? ").lower()

name2 = input ("What is your partner name? ").lower()

full_name= name1 + name2

# T = name1.count("t") + name1.count("t")
# R = name1.count("r") + name1.count("r")
# U = name1.count("u") + name1.count("u")
# E = name1.count("e") + name1.count("e")
T = full_name.count("t")
R = full_name.count("r")
U = full_name.count("u")
E = full_name.count("e")
t1 = T + R + U + E

# L = name1.count("l") + name1.count("l")
# O = name1.count("o") + name1.count("o")
# V = name1.count("v") + name1.count("v")
# E = name1.count("e") + name1.count("e")
L = full_name.count("l")
O = full_name.count("o")
V = full_name.count("v")
E = full_name.count("e")
t2 = L + O + V + E

x = str(t1) + str(t2)
total = int(x)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")

if total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together")

else:
    print(f"Your score is {total}")    

print(total)








