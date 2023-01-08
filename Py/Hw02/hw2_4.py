# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

def range_numbers_n():
    n = int(input('Enter your number: '))
    print(*range(-n, n+1))            # * перед range - это оператор РАСПАКОВКИ ДИАПАЗОНА


range_numbers_n()

###НЕ ПОНЯЛ КАК ПРЕОБРАЗОВАТЬ В СПИСОК 
# ????


nums_list = list(range_numbers_n)

list_nums = []
list_nums.append(range_numbers_n)
print(list_nums)
