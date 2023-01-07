# 4. Напишите программу, которая по заданному номеру четверти,
#    показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input())

if quarter == 1:
    print("x > 0, y > 0")
elif quarter == 2:
    print("x < 0, y > 0")
elif quarter == 3:
    print("x < 0, y < 0")
elif quarter == 4:
    print("x > 0, y < 0")
else:
    print("Error, wrong number!")

# --------------------------- вариант

quarter = input()

match quarter:
    case "1":
        print("x > 0, y > 0")
    case "2":
        print("x < 0, y > 0")
    case "3":
        print("x < 0, y < 0")
    case "4":
        print("x > 0, y < 0")
    case _:
        print("error")
