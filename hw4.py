# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти


number_q = int(input('Enter number of the quater: '))
if number_q <= 0 or number_q >= 5:
    print('Error, your number quater is invalid! Try again!')
elif number_q == 1:
    print(f'The first quater {number_q} -> x > 0, y > 0')
elif number_q == 2:
    print(f'The second quater {number_q} -> x > 0, y < 0')
elif number_q == 3:
    print(f'The Thirst quater {number_q} -> x < 0, y < 0')
elif number_q == 4:
    print(f'The fourth quater {number_q} -> x < 0, y > 0')
    










