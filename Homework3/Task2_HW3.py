#  Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
n = int(input('Введите количество элементов списка'))
list = []
for i in range(n):
    list.append(random.randint(1, 10))
print(list)
multlist = []
for i in range(int(len(list)/2)):
    # print(i,list[i],list[-(i+1)])
    multlist.append(list[i]*list[-(i+1)])
if (len(list) % 2):
    multlist.append(list[int(len(list)/2)]**2)
print(multlist)
