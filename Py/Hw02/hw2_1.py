#  Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# # Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = float(input('Enter any non-integer number: '))
l = len(str(number)) 
int_n = number * 10 ** (l - 2)
n = int(int_n)
sum = 0 

print(f'Your number was rounded up: {n}')
while n > 0:
    dig = n % 10
    sum = sum + dig
    n = n // 10
print(f'Sum of digits from your number is: {sum}')



# number = float(input('Enter any non-integer number > 100: '))
# n = int(number) # преобразование в целое число с окргулением
# sum = 0 # переменная для цикла +1 +1 и тд...
# print(f'Your number is: {number}')                        ##### не верное решение ######
# print(f'Your number was rounded up: {n}')
# while n > 0:
#     dig = n % 10
#     sum = sum + dig
#     n = n // 10
# print(f'Sum of digits from your number is: {sum}')

