# Напишите программу, в которой пользователь будет задавать две строки,
# # программа - определять количество вхождений одной строки в другой.

str1 = input('Enter the first word or any frase: ')
str2 = input("введите текст отличающийся на несколько символов или слов меньше чем первая фраза: ")

print(str1.count(str2))