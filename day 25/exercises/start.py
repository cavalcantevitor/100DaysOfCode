# # with open("weather_data.csv") as data:
# #     file = data.readlines()
# #
# # print(file)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(f"Max: {data["temp"].max()}")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
print(fur_color)

gray = 0
cinnamon = 0
black = 0


for row in fur_color:
    if row == "Gray":
        gray += 1
    elif row == "Cinnamon":
        cinnamon += 1
    elif row == "Black":
        black += 1

print(gray)
print(cinnamon)
print(black)