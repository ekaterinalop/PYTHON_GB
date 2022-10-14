# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
import collections

data = []
for i in range(10):
    data.append(random.randint(0, 10))
print(data)

newdata = data[:]
newdata.sort()

res = []
for i in range(1, len(newdata)):
    if newdata[i] != newdata[i-1]:
        res.append(newdata[i-1])
print(res)


