# типы данных и переменная 
# int, float, boolean, str, list, None

                        ############# ПЕРВЫЙ РАЗДЕЛ ЛЕКЦИИ ############

# value = None
# print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# # value = 1234
# # print(type(value))
# s = 'Hello "world"' #опострофы заменяют кавычки
# r = "Hello 'world" # чтобы оставить в тексте опостров
# t = 'Hello \'world' # эскейп последовательности
# o = 'Hello \nworld' # с переносом на новую строку

# print(s) #вывод строки
# print(r) #вывод строки
# print(t) #вывод строки
# print(o) #вывод строки
# # также можно сделать вывод с указанием функции PRINT один раз:
# print(a, b, s, r, t, o)

# print(a, ' - ', b, ' - ', s) #можно добавить в функцию вывода строки(или иной текст)

# print('{} - {} - {}'.format(a, b, s)) #можно добавить в функцию вывода форматированный результат

# print(f'{a} - {b} - {s}') #можно добавить интерполяцию

# print('{2} - {0} - {1}'.format(a, b, s)) #можно изменить порядок вывода в {указать индекс массива}

# f = False #логическая переменнная
# print(f)

#/

                            ####### ВТОРОЙ РАЗДЕЛ ЛЕКЦИИ ########

# для того чтобы объявить что-то похожее на массив делаем так:

# list = [1,2,3]
# print(list)

# list = ['1', '2', '3', 'Hello world'] #лист строк 
# print(list)
# # так как в Python динамическа] типизация, то можно миксовать типы в списки
# list = ['1', '2', '3', 'Hello world', 1,2,3,4.5,True] #!!!! ВАЖНО ТАК НЕ ДЕЛАТЬ
# print(list)

# list = ['1', '2', '3'] #!!!! ВАЖНО ЗНАТЬ "ПРОБЕЛ" МОЖЕТ СЛОМАТЬ НАШУ ПРОГРАММУ
# col = ['Hello', 1,2,3.4,True]
# print(list)
# print(col)

                            ########### TRETIY RAZDEL ########
                            # Ввод и вывод данных. ПРЕОБРАЗОВАНИЕ ТИПОВ

# print('Enter a')
# a = input()
# print(' Enter b')
# b = input()
# print(a,b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}') #запись сделана через так называемую интерполяцию строк 
# #ДЛЯ ТОГО ЧТОБЫ ВЫВЕСТИ ЧИСЛОВОЙ ФОРМАТ ИЛИ ВЫРАЖЕНИЕ ЧИСЕЛ НАПРИМЕР:
# print('Enter a');
# a = int(input())
# print(' Enter b');
# b = int(input())

# print(a, ' + ' , b, ' = ',  a+b)

                            ########### 4-Y RAZDEL ########
                        #АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ 
# Без них не получиться написать ни одной программы. МАТЕМАТИКА В ПОМОЩЬ
# ПРИОРИТЕТ ОПЕРАЦИЙ +, -, *, /, %, //,**


exp1 = 2**3 - 10 % 5 + 2*3
exp2 = 2**3 - 10 / 5 + 2*3
print(exp1) # 14.0 или 14
print(exp2) # 12.0 или 12

# Сокращённые операции и операции присваивания
# Демонстрация
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

#                    # УНАРНЫЙ ПЛЮС + или МИНУС -

# a = 123
# b = 312
# c = a + b
# print(c)

# a = + 123
# b = - 312
# c = a + b
# print(c)

# a = + 123
# b = - 312
# c = a - b
# print(c)


# a = 256
# b = 16
# c = a // b #деление в целых числах
# print(c)


# a = 15
# b = 2
# c = a / b #знак деления в нецелочисленных выражениях
# print(c)

# a = 12
# b = 8
# c = a % b #знак деления с остатком
# print(c)

# a = 15
# b = 2
# c = a ** b #знак возведения в степень первого числа во второе
# print(c)

# # a = 1,31231 ## ВЫДАЕТ В ЭТОМ ПРИМЕРЕ ОШИБКУУУУ
# # b = 2
# # c = #round(a * b, 3) #оператор для решения произведения нецелочисленных чисел, что позволяет решить по матем.правилам
# # print(c)

# a = 3
# a =+ 5 #a + 5
# b = 2
# b =+ 2 #b + 2 вместо такой записи записываем =+ (и аналогично любые знаки математических решений)
# c = a / b #присвоение значения а = а 
# print(c)


########### 5-Y RAZDEL ######
#ЛОГИЧЕСКИЕ ОПЕРАЦИИ 

#       >, >=, <, <=, ==, !=
#       not, and, or – не путать с &, |,
#       ^
#       Кое-что ещё: is, is not, in, not in

# a = 1 > 3
# print(a)

# a = 1 < 3
# print(a)

# a = 1 < 4 and 5 > 3
# print(a)

# a = 1 == 3 # знак сравнения == 
# print(a)

# a = 1 != 3 # знак неравенства 
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b) #можно сравнивать и в строковом режиме !!! НО ЕСТЬ СВОИ ТОНКОСТИ
# #НАПРИМЕР: 
# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5 #можно использовать тройные, четверные неравенства !ОСОБЕННОСТЬ ПАЙТОНА
# print(a)
# #ИЛИ 
# func = 1
# T = 4
# x = 123
# print(func<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f) # указывает что 2 в списке ф
# print(not 2 in f) #указывает что 2 не в ф

# is_odd = f[0] % 2 == 0 #проверка на соответвие четности части списка с индексом 0, то есть 1
# print(is_odd) # 1 не четная поэтому FALSE

# is_odd = not f[1] % 2 #также можно проверить четность через ОТРИЦАНИЕ NOT
# print(is_odd)

                                            ######### 6-Y RAZDEL #######
                                            # УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ 
                                            #   if, else и ЦИКЛ while

# if condition:
 # operator 1             ОТСТУПЫ ОЧЕНЬ ВАЖНЫ!!!!!
 # operator 2
 # ...
 # operator n
# else:
 # operator n + 1
 # operator n + 2
 # ...
 # operator n + m

# a = int(input('a = '))            #ПОИСК МАКСИМАЛЬНОГО ЧИСЛА
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!');
# else:
#  print('Привет, ', username);

### ЛОГИЧЕСКИЙ ОПЕРАТОР  проверки нескольких условий 

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

##### ЦИКЛ while

# original = 34
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)
# exit()
# original = 222224
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
#  print(original)
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)

                                ####    FOR   #####
# for i in -1, 1, 2, 3, 4, 5:
#     print(i*(-2)) ## таким образом этим циклом можно беребрать список
# #так же можно записать:
# list = [1,2,3,4,5]
# for i in list:
    # print(i*(5))

# #чтобы перебрать список ДИАПАЗОНОМ от 0 ДДДДООО какой-либо цифры записываем так:
# list = range(10)
# for i in list:
    # print(i)
# # или ТАК:
# for i in range(5):
#     print(i)
# #ИЛИ ТАК:
# for i in range(3, 6):
    # print(i)
# # ЧТОБЫ ИЗМЕНИТЬ ШАГ ДОБАВЛЯЕМ 3-Й АРГУМЕНТ ПРЕРАЩЕНИЯ:
# for i in range(1, 10, 2):
#     print(i)

# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#  print(i)
# 100 80 60 40 20

# #ТАК ЖЕ И ВЫСТРАИВАЕМ РАБОТУ СО СТРОКАМИ в точности до пробелом и любых знаков:
# for i in 'qwe - rty':
#     print(i)

                    ######### БАЗОВОЕ API РАБОТЫ СО СТРОКАМИ ##########

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39 ДАННАЯ ФУНКЦИЯ ИСПОЛЬЗУЕТСЯ ДЛЯ ОПРЕДЕЛЕНИЯ КОЛИЧЕСТВА СИМВОЛОВ В СТРОКЕ
# print('ещё' in text) # True ДАННАЯ ФУНКЦИЯ ИСПОЛЬЗУЕТСЯ ДЛЯ ПРОВЕРКИ НАЛИЧИЯ НУЖНОЙ КОМБИНАЦИИ СИМВОЛОВ В СТРОКЕ
# print(text.isdigit()) # False ДАННАЯ ФУНКЦИЯ ПРОВЕРЯЕТ ЯВЛЯЕТСЯ ЛИ ВСЕ СИМВОЛЫ В СТРОКЕ ЧИСЛАМИ
# print(text.islower()) # True ДАННАЯ ФУНКЦИЯ ПРОВЕРЯЕТ ЯВЛЯЮТСЯ ЛИ СИМВОЛЫ СТРОКИ В НИЖНЕМ РЕГИСТРЕ
# print(text.replace('ещё','ЕЩЁ')) #ДАННАЯ ФУНКЦИЯ НУЖНО ЧТОБЫ КАКИЕ_ТО СИМВОЛЫ ЖЕЛАЕМ ЗАМЕНИТЬ 
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к ВАЖНО НЕ ЗАБЫВАТЬ ЧТО ИНДЕКСАЦИЯ С 0
# print(text[-5]) # б
# print(text[:]) # print(text)  ЗАПИСАНО ВМЕСТО [0:len(text)-1] 
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок ОТ нулевого символа до -2 го "о"
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ..


                ######## РАБОТА СО СПИСКАМИ ########

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran) #преобразуем в другой тип 
# print(type(numbers))

# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

                        ####### РАСШИРЕННЫЙ МЕТОД РАБОТЫ СО СПИСКАМИ ########

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# del colors[0]
# print(colors)


                            #######  РАБОТА С ФУНКЦИЯМИ ########


# def f(x):
#  return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2
# print(f(arg))
# print(type(f(arg)))

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType


