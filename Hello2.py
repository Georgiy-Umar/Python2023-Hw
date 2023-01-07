                        ############### .  РАБОТА С ФАЙЛАМИ ################
# # Хранение данных
# Передача данных в клиент-серверных проектах Хранение конфигов
# Логирование действий

# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a – открытие для добавления данных (что-то можно дописать)
# r – открытие для чтения данных (только считывание)
# w – открытие для записи данных ()
# w+, r+

# with open('file.txt', 'w') as data:
#      data.write('line 1\n')
#      data.write('line 2\n')

# colors = ['red', 'green', 'blue'] #Список
# data = open('file.txt', 'w') # текстовая переменная data связывается с текстовым файлом с указанием пути к файлу и 
#                               # указваем режим работы "а" - появляется новый файл и вносится в него данные
#                               # также параметр "а" используется для добавления в теккущий файл данных 
#                              # если заменить параметр "а" на "w" происходит перезапись (то есть заново вносится параметр)
#                              # или "r" то тогда            
# data.writelines(colors) # разделителей не будет
# data.close() # ЗАКРЫТИЕ ПОДКЛЮЧЕНИЕ ДЛЯ ОСВОБОЖДЕНИЯ ПАМЯТИ И чтобы в дальнейших процессах данный файл не учавствовал

#                                    # В ХОДЕ ЗАПУСКА ДАННОГО КОДА ПОЯВЛЯЕТСЯ НОВЫЙ ФАЙЛ ТЕКСТОВЫЙ ГДЕ ВНЕСЕНЫ ДАННЫЕ ИЗ colors
#                                    # и если повторять запуск то в данный файл будет добавляться текст из переменной
# exit() # данная функция останавливает работу последующего кода
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#      print(line) 
# data.close()

                                        #### ТАКЖЕ МОЖНО ВНОСИТЬ ДАННЫЕ В ФАЙЛ ИЗМЕНЯЮ ПАРАМЕТРЫ ВНЕСЕНИЯ ДАННЫХ ######

# colors = ['red\n', 'green\n', 'blue\n'] 
# data = open('file.txt', 'a') # текстовая переменная data связывается с текстовым файлом с указанием пути к файлу и 
#                               # указваем режим работы "а" - появляется новый файл и вносится в него данные
#                               # также параметр "а" используется для добавления в теккущий файл данных 
#                              # если заменить параметр "а" на "w" происходит перезапись (то есть заново вносится параметр)
#                              # или "r" то тогда            
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 123\n')
# data.writelines('Bobrik\n')
# data.write('LINE 1111\n')
# data.close() # ЗАКРЫТИЕ ПОДКЛЮЧЕНИЕ ДЛЯ ОСВОБОЖДЕНИЯ ПАМЯТИ И чтобы в дальнейших процессах данный файл не учавствовал

#                                    # В ХОДЕ ЗАПУСКА ДАННОГО КОДА ПОЯВЛЯЕТСЯ НОВЫЙ ФАЙЛ ТЕКСТОВЫЙ ГДЕ ВНЕСЕНЫ ДАННЫЕ ИЗ colors
#                                    # и если повторять запуск то в данный файл будет добавляться текст из переменной
# exit() # данная функция останавливает работу последующего кода

                                  ###### ТАКЖЕ МЕТОД ВНЕСЕНИЯ ДАННЫХ ########

# with open('file.txt', 'a') as data:     
#      data.write('\nline 1\n')
#      data.write('line 2\n')
                              # в данном формате написания кода не нужно делать закрытие файла через: data.close() 
                              # так как тут делается все автоматически
                              
                                   
                                   #####РАССМОТРИМ МЕТОД ЧТЕНИЯ ДАННЫХ ИЗ ФАЙЛА####

# path = 'file.txt' ### УКАЗЫВАЕМ ПУТЬ К ПАПКЕ И ФАЙЛУ
# data = open(path, 'r') ### УКАЗЫВАЕМ РЕЖИМ РАБОТЫ: 'r' - режим чтения 
# for line in data: ### через цикл пробежим по файлу и считаем все строки
#      print(line) 
# data.close() ## и после работы закрываем его
# exit() # данная функция останавливает работу последующего кода

###### ВСЕ ДАННЫЕ В ФАЙЛАХ ХРАНЯТСЯ В ТЕКСТОВОМ ФОРМАТЕ, 
# и ЧТОБЫ ИХ ХРАНИТЬ КАК ЧИСЛА НЕОБХОДИМО ИХ КОНВЕРТИРОВАТЬ В ЧИСЛА
# использую функцию (int, float, double)

                    ####### ФУНКЦИИ ########
                    # Это фрагмент программы, используемый многократно

# МОЖНО ИМПОРТИРОВАТЬ РАБОТУ ФУНКЦИЙ ИЗ ФАЙЛА УКАЗАНИЕМ ССЫЛКИ НА НЕГО:
# ТАКИМ ОБРАЗОМ МЫ МОЖЕМ УПРОЩАТЬ СВОЮ ПРОГРАММУ ЧЕРЕЗ РАЗДЕЛЕНИЕ ФАЙЛОВ 
# И ИСПОЛЬЗОВАТЬ КОД ФУНКЦИЙ ИЗ РАЗНЫХ ФАЙЛОВ
# import hello
# print(hello.f(1))

# ### ТАКЖЕ МОЖНО ЗАПИСАТЬ ТАК:

# import hello as h
# print(h.f(1))

                         ##### РАБОТА С ТЕКСТОМ_СТРОКАМИ_ЧИСЛАМИ И ДЕЙСТВИЯМИ В СТРОКЕ #####

# def new_string(symbol, count):
#      return symbol * count #перемножаем символы с числами в строке
# print(new_string('!', 5))   # !!!!!
# # print(new_string('!'))      # TypeError missing 1 required ... так нет второго аргумента


# def new_string(symbol, count = 3): # задаем во втором аргументе числовое значени
#      return symbol * count
# print(new_string('!', 5)) 
# print(new_string('!')) 
# print(new_string(4)) 
# # !!!!!
# # !!!
# # 12


               ##### Через функции можно передавать неограниченное количество аргументов ####

# def concatenatio (*params) : # можем указать неограниченное количество аргументов
#      res: int = "" #тут указываем тип данных строка или инт 
#      for item in params:
#           res += item
#      return res

# print (concatenatio ('a', 's', 'd', 'w')) # asdw
# print (concatenatio ('5\n'*2, '1\n', '9\n', '2\n')) # ald2 \ 55192
# # print (conatenatio (1, 2, 3, 4)) # TypeError:

                                             
                                             ##### РЕКУРСИЯ #####
 
# n = int(input("Enter number: "))
# def fib (n):       #b FIBONACCI ПРИМЕР это когда к последующей цифре прибавляем текущую
#      if n in [1, 2]:
#        return 1
#      else:
#           return fib (n-1) + fib (n-2) 
# list = []
# for e in range (1,6): #тут задается диапозон для отображения в терминале на котором хотим узнать данные фибоначи
#      list. append (fib (e)) 
# print (list) # 1 1 2 3 5 8 13 21 34

                         
                         
                         ####### Кортеж - это неизменяемый "список"#######
                         # ЭТО СПИСОК А НЕ ЧИСЛОВЫЕ РЯДЫ

# t = ()
# print (type (t))  # tuple
# t = (1,)
# print (type (t)) # tuple
# t = (1)
# print (type (t)) #int
# t = (28, 9, 1990)
# print (type (t)) # tuple
# colors = ['red', 'green', 'blue']
# print (colors) # ['red','green', 'blue']
# print (type(colors))
# t = tuple (colors)
# print (t)  # ('red', 'green', 'blue')


# a = (3, 4, 1, 43)
# print(a)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[-4])



# t = tuple (['red', 'green', 'blue'])
# print (t [0])       # red
# print (t [2])       # blue
# # print (t [101)    # IndexError: tuple index out of range
# print (t [-2])
# # green
# # print (t[-200]) # IndexError: tuple index out of range
# for e in t:
#      print (e)      # red green blue
# t[0] = 'black'
# # TypeError: 'tuple' object does not support item assignment

# a = (3, 4, 5)

# for item in a:
#      print(item)

                                        ##### РАСПАКОВКА КОРТЕЖА В ОТДЕЛЬНЫЕ ПЕРЕМЕННЫЕ ######

# t = tuple (['red', 'green','blue'])
# red, green, blue = t
# print ('r: {} g: {} b: 1]'. format (red, green, blue)) # в {} будет вставляться по очереди данные переменных (red, green, blue)
# # r:red g:green b:blue
  




                                                                 ###### СЛОВАРИ #######
                                        # СЛОВАРИ - Неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}  
# dictionary = \
#      {
#           'up': '↑',
#           'left': '←',
#           'down': '↓',
#           'right': '→'
#      }  # ОБРАТНЫЙ \ нужен чтобы длинную строку вписать в несколько коротких строк
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
#  # типы ключей могут отличаться

# for k in dictionary.keys(): # обращение к ключам
#      print(k)

# for k in dictionary.values(): # обращение к значения в ключах
#      print(k)



# print(dictionary['up'])   # ↑
#  # типы ключей могут отличаться

# dictionary['left'] = '⇐' 
# print(dictionary['left']) # ⇐ 
# #print(dictionary['type']) # KeyError: 'type' 
# del dictionary['left'] # удаление элемента
# for item in dictionary:       # for (k,v) in dictionary.items():
#      print('{}: {}'.format(item, dictionary[item]))
#  # up: ↑
#  # down: ↓
#  # right: →




                                                       ###### МНОЖЕСТВА #######
                                                       # Неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))  # set
# print(type(b))  # set

# a = {1, 2, 3, 5, 8}
# print(a)
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # set
# print(type(b))  # set
# print(type(c))  # set
# a = {1, 1, 1, 1, 1}
# print(a)  # {1}


# colors = {'red', 'green', 'blue'}
# {'red', 'green', 'blue'}
# {'red', 'green', 'blue'}
# {'red', 'green', 'blue','gray'}

# print(colors) #прикол множества в ТОМ ЧТО ПРИ ВЫВОДЕ НА ПЕЧАТЬ ДАННЫЕ НЕ СТАТИЧНЫ И МОГУ МЕНЯТЬ ПОРЯДОК В ОТЛИЧИИ ОТ СПИСКОВ И МАССИВОВ
# exit()
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)       # {'green', 'blue','gray'}

# # colors.remove('red') # KeyError: 'red'

# colors.discard('red')  # ok
# print(colors)
# colors.clear() #очистка значения переменной множества
# print(colors)
# # {'green', 'blue','gray'}
# # { }
# # set()


# a = {1, 2, 3, 5, 8}   
# print(a)
# b = {2, 5, 8, 13, 21}
# print(b)
# c = a.copy()             # c = {1, 2, 3, 5, 8}
# print(c)
# u = a.union(b)           # u = {1, 2, 3, 5, 8, 13, 21} объединяет в одно множество
# print(u)
# i = a.intersection(b)    # i = {8, 2, 5} выводит только совпадающие данные
# print(i)
# dl = a.difference(b)     # dl = {1, 3} не совпадающие по а
# print(dl)
# dr = b.difference(a)     # dr = {13, 21} не совпадающие по б
# print(dr)
# q = a \
#      .union(b) \
#      .difference(a.intersection(b))
# print(q)
# # {1, 21, 3, 13}




                                             ###### СПИСКИ ######

# list2 = [1,2,3,4,51]
# list1 = [1,2,3,4,51]

# l = list2

# print(l)

# print(l.append(77))
# print(l)

# print(list1.insert(2, 11)) #замена элемента с индексом 2 (3 на 11)
# print(list1)

# print(len(list1)) # МЕТОD POP с каждым выводом удаляет последний элемент списка

# print(list1.pop(3)) # ТАКИМ ОБРАЗОМ УДАЛЯЕТСЯ КОНКРЕТНЫЙ ЭЛЕМЕНТ СПИСКА С ИНДЕКСОМ 3

# print(list1.pop())
# print(list1)
# print (list1.pop())
# print (list1)
# print(list1.pop() )
# print (list1)              



