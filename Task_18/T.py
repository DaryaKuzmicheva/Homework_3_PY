#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#1 2 3 4 5
#6-> 5

import random
n = int(input("Введите число N:"))
array = [n]
for x in range(n):
    array.append(random.randint(1, 20))
print(array)
x = int(input("Введите число x:"))
array_append = array.append(x)
print(array)
number = 0
for i in range(len(array)):
    if (x - array[i]) < x - number and x - array[i] > 0:
        number = i
print(array[number])




