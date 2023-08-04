#  Loops

# x = ["Mouli", "King", "Dinesh"]
# for i in x:
#     print(i)


# Calculating the average height


# x = input("Enter the heights of the students? ").split()
# for i in range(0, len(x)):
#     x[i] = int(x[i])
# print(x);

# print(f"Average Height is: {round(sum(x)/len(x))}" )

#  Finding highest score of students

# scores = input("Enter the scores of students? ").split(" ")
# print(scores);
# for i in range(0,len(scores)):
#     scores[i] = int(scores[i])

# max = scores[0]
# for i in scores:
#     if i > max:
#         max = i

# print(max);

#  Adding numbers from 1 to 100

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)    

#  Adding even numbers from 1 to 100

# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum += i
# print(sum) 


# sum = 0
# for i in range(2,101,2):
#     sum += i
# print(sum)    
# 


#  FizzBuzz Challenge

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"  
    print(i)      