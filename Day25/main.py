from pathlib import Path
x = str(Path.cwd()) + "/Day25/weather-data.csv"

# with open(x) as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open(x) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
#     print(temperatures)    


import pandas as pd

# data = pd.read_csv(x)
# print(data)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

# data_dict = {
#     "students": ["Amy", "Angela", "Mouli"],
#     "scores":  [23,34,45]
# }

# data = pd.DataFrame(data_dict)
# print(data)

data = pd.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_sq)
# print(cinnamon_sq)
# print(black_sq)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq, cinnamon_sq, black_sq]
}

# print(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv("new_sq_count.csv")
