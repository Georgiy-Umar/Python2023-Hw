# 5. Напишите программу, которая принимает на вход координаты двух точек и
# # находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

x1 = float(input("Enter any coordinate for the first point of x: "))
y1 = float(input("Enter any coordinate for the first point of y: "))
x2 = float(input("Enter any coordinate for the second point of x: "))
y2 = float(input("Enter any coordinate for the second point of y: "))

len_segment = ((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)) ** 0.5
print(len_segment)








