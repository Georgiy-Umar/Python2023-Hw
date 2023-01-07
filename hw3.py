# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_location = int(input("Enter your any infotmation of coordinates of the X: "))
y_location = int(input("Enter your anyinfotmation of coordinates of the Y: "))

if (x_location > 0 and y_location > 0):
    print(f'X = {x_location} Y = {y_location}, Your point on the first quater of the location!')
elif (x_location > 0 and y_location <= 0):
    print(f'X = {x_location} Y = {y_location}, Your point on the second quater of the location!')
elif (x_location < 0 and y_location < 0):
    print(f'X = {x_location} Y = {y_location}, Your point on the thirt quater of the location!')
elif (x_location < 0 and y_location > 0):
    print(f'X = {x_location} Y = {y_location}, Your point on the fourth quater of the location!')