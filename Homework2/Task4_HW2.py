#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = int(input('Введите N:'))
list = []
for i in range(n):
    list.append(random.randint(-n, n))
print('наш список', list)

key = []
path = 'file.txt'
with open(path, 'r') as data:
    for line in data:
        key.append(int(line))
print('номера позиций из файла', key)

result = []
for i in range(len(key)):
    if key[i] < len(list):
        result.append(list[key[i]])
print('выбранные позиции', result)

mult = 1
for i in range(len(result)):
    mult *= result[i]
print('их произведение', mult)
