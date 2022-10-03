#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Негафибоначчи.
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a=int(input('Введите число '))
n=-1*a
def negafib(a):
    if a==n:
        return n
    return negafib(a-1)*(a-n)
list=[]
for i in range(n,a+1):
    list.append(negafib(i))
print (list)