#  List Comprehension 

# num = [1,2,3]
# new_list = [n+1 for n in num]
# print(new_list)

# letter = "Mouli"
# new_let = [let for let in letter]
# print(new_let)

# x = [1,2,3,4,5]
# new_x = [2*x[item] for item in range(1,5)]
# print(new_x)

# names = ["Mouli", "Harika", "Dinesh","Arnoldghg", "hdsbfkjghbsf"]
# new_names = [name for name in names if len(name) < 7]
# print(new_names)

# names = ["Mouli", "Harika", "Dinesh","Arnoldghg", "hdsbfkjghbsf"]
# new_names = [name.upper() for name in names if len(name) < 7]
# print(new_names)

# numbers = [1,1,2,3,64,55,45,36,17,18,81,9]
# new_numbers = [num*num for num in numbers]
# print(new_numbers)

# numbers = [1,2,4,6,5,7,8,9,4,33,55,4,42,44,77,88,32]
# new_num = [num for num in numbers if num%2 ==0]
# print(new_num)

#  Dictionary Comprehension
# names = ["Mouli", "Anil", "Harika", "Dinesh", "Mohan"]
# import random

# new_dict = {student:random.randint(1,100) for student in names}
# # print(new_dict)

# passed_dict = {key:value for (key,value) in new_dict.items() if value > 60}
# print(passed_dict)

snetence = "The Greatest gift in life is friendship and i have reveived it"
x = snetence.split()

new_dict = {v:len(v) for v in x}
print(new_dict)