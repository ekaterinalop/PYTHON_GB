# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n=int(input('Введите десятичное число '))
def tentotwo(dec):
    if dec==0:
        return ''
    return tentotwo(dec//2)+ str(dec%2)
print (tentotwo(n))
