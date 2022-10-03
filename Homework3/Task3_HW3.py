# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from asyncio import mixins
import random
list = []
for i in range(5):
    list.append(random.uniform(0, 10))

min = list[0]-int(list[0])
max = list[0]-int(list[0])
for item in list:
    if item-int(item) <= min:
        min = item-int(item)
    if item-int(item) >= max:
        max = item-int(item)
res = 0
res = max-min
print(
    f'В списке {list}, \nмакс и мин дробная часть {max} и {min}, их разница {res}')
