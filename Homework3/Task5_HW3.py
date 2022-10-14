# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Негафибоначчи.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число '))

list = [-1, 1]
for i in range(0, k+1):
    list.append(list[i]+list[i+1])

nega_fib = []
for i in range(0, (len(list)-3)):
    nega_fib.append(list[-1-i]*((-1)**(i+1)))

for i in range(2, k+3):
    nega_fib.append(list[i])
print(nega_fib)
