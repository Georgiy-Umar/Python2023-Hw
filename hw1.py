# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


num_day = int(input('Enter number day of week: '))
if (num_day >= 6 and num_day <= 7):
    print("YES! It is holyday: ")
elif (num_day > 0 and num_day < 6): 
    print("NO! It is work day! ")
elif (num_day < 0 or num_day > 7):
    print("Your number is invalid, try again!")
    








