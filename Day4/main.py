#  Random Modules


import random;

# random_integer = random.randint(1,10)
# print(random_integer);

# random_num = round(random.random() * 5)
# print(random_num)

# #  Heads or Tails

# side = random.randint(0,1)
# if side == 1:
#     print("Head")
# else:
#     print('Tail')

#  Bill Assignment

# x = input("Give the names of the peopel with comma and space :")
# z = x.split(", ");
# random_number = random.randint(0,len(z)-1)
# y = z[random_number];
# print(y)


#  Treasure Island

row1 = ["☐","☐","☐"]
row2 = ["☐","☐","☐"]
row3 = ["☐","☐","☐"]
map = [row1, row2, row3]
position = input("Where do you want to put the treasure? ")

col = int(position[0])
row = int(position[1])

map[row-1][col-1] = "X"
print(f"{row1}\n{row2}\n{row3}")



