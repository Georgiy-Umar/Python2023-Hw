# # Напишите программу, которая принимает на вход число N
# # и выдает набор произведений чисел от 1 до N в виде списка.
# # 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# # - 4 -> [1, 2, 6, 24]
# # - 6 -> [1, 2, 6, 24, 120, 720]

m = int(input("Enter number: "))
def fact (n):
    if n == 0:
       return 1
    return fact (n-1) * n 
list = []
for e in range (1,m): 
     list. append (fact (e)) 
print (list) 