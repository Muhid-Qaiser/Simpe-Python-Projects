# import csv
# with open("weather_data.csv", 'r') as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# data_list = data['temp'].to_list()
# print(data['temp'].mean())
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Calculates color count
gray = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon = len(data[data['Primary Fur Color'] == "Cinnamon"])
black = len(data[data['Primary Fur Color'] == "Black"])

color_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [gray, cinnamon, black]
}

color_data = pandas.DataFrame(color_dict)
color_data.to_csv('squirrel_count.csv')
