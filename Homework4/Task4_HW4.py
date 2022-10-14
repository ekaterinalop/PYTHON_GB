# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень многочлена число k: '))
lst_coef = []
s = ''
for i in range(k+1):
    lst_coef.append(random.randint(0, 100))

    if lst_coef[i] != 0:
        if k != 0:
            s += f'+{lst_coef[i]}x^{k}'
            k -= 1
        else:
            s += f'+{lst_coef[i]}'
            k -= 1
    else:
        k -= 1
s = s[1:]+'=0'
print(f'коэффициенты многочлена: {lst_coef}  {s}')

data = open('hw4.txt', 'w')
data.writelines(s)
data.close()
