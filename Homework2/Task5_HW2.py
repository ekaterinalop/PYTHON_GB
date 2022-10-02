#  Реализуйте алгоритм перемешивания списка.

import random
list = []
for i in range(6):
    list.append(random.randint(-100, 100))
print('оригинальный список', list)
random.shuffle(list)
print('перемешанный список', list)
