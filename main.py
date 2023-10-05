# # with open("weather_data.csv") as data:
# #     print(data.readlines())
#
# import csv
#
# with open("weather_data.csv") as data:
#     data_in_file=csv.reader(data)
#     temperature=[]
#     for each_data in data_in_file:
#         if each_data[1]=="temp":
#             pass
#         else:
#             temperature.append(int(each_data[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
temp_list=data["temp"].to_list()
# s=0
# l=len(temp_list)
# for d in temp_list:
#     s=s+d
# avg = s/l
# print(avg)
# sum(temp_list)/len(temp_list)
# max_temp=data["temp"].max()
# print(data[data["temp"]>data["temp"].max()])
monday=data[data.day=="Monday"]
temp=monday["temp"]
f_temp=(temp*1.8)+32
print(f_temp)