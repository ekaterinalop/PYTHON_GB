# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#num = int(input('Введите десятичное число '))

def tentotwo(n):
    
    if n == 0:
        return ''
    return tentotwo(n//2) + str(n % 2)
    
num = int(input('Введите десятичное число '))
print(tentotwo(num))
