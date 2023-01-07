# Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно

list_n = []
n = int(input('Enter your N: '))
for i in range(1, n+1):
    list_n.append (i * 3 + 1)
print(list_n)






