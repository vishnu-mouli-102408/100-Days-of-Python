# Integer data type

num = 123456;

a = 123_456_567; # instead of commas, we put underscore to seperate numbers;

x = 45.66 # floating numbers

v = True # boolean numbers

# print(str(50) + str(90));

# print(40 + float("123.50"));

#  assignment 1

# number = input("Enter a number\n");

# first = number[0];
# second = number[1];
# result = int(first) + int(second)
# print("The result is: "+ str(result));


##########################################################

# print(3*3+3/3-3);

# assignment 2

# height = input("Enter a number\n");
# weight = input("Enter a number\n");

# float(weight);
# float(height);

# BMI = int(weight) / float(height) ** 2;
# result = int(BMI);
# print(type(BMI));

# print(result)

# print(type(5/3)) # return float
# print(type(5//3)) # returns int

#  Using fstring

num = 9;
sore = 23.5

isHi = True;

#  to print all of these in one line without coverting their datatype we use F-string

# print(f"the num is {num} and the score is {sore} and the istrue is {isHi}");


#  Assignent 3;

num = input("Enter you current age?\n");

num_int = int(num);

years_rem = 90 - num_int;

days_rem = years_rem * 365;

weeks_rem = years_rem * 52;

months_rem = years_rem * 12;

print(f"You have left {months_rem} months, {weeks_rem} weeks and {days_rem} days in your life");

#  ended here