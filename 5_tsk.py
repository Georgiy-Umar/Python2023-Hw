  # 5. Напишите программу, которая принимает на вход число и проверяет,
                            # кратно ли оно 5 и 10 или 15, (и) но не 30.

num = int(input("Enter your number: "))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print('YES')
else:
    print('NO')